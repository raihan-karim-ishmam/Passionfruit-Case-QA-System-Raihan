import streamlit as st
import pandas as pd
from io import StringIO
import tempfile
from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
import os

# Path to the vector store (Used FAISS as good with numerical data)
DB_FAISS_PATH = "vectorstore/db_faiss"

def process_bar_separated_file(file):
    # Preprocessing the file to make it efficient for the LLM (processing parameters elected by testing outcomes)
    try:
        lines = file.getvalue().decode("utf-8").splitlines()
        rows = [line.strip().split('|') for line in lines]
        max_columns = max(len(row) for row in rows)
        normalized_rows = [row + [None] * (max_columns - len(row)) for row in rows]
        df = pd.DataFrame(normalized_rows[1:], columns=normalized_rows[0])      # Advanced dataframes to be implemented in future versions
        return df.to_csv(index=False)
    except Exception as e:
        st.error(f"Error processing file: {e}")
        return None

# Streamlit app
st.title("LLM based CSV Q&A System ft. Llama by Meta")

# File input
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file:
    processed_csv = process_bar_separated_file(uploaded_file)
    if processed_csv:
        # Save the processed CSV to a temporary file (cloud in the future for optimizing)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
            temp_file.write(processed_csv.encode('utf-8'))
            temp_file_path = temp_file.name

        # Load the processed CSV file
        loader = CSVLoader(file_path=temp_file_path, encoding="utf-8", csv_args={'delimiter': ','})
        data = loader.load()
        st.write("File loaded and processed successfully!")
        print(data)  # Debugging output to check loaded data (for developer insight)

        # Split the text into chunks (to fit in token size as usual toke size Llama can't be run efficiently in local PC)
        st.info("Splitting text into chunks...")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
        text_chunks = text_splitter.split_documents(data)
        st.write(f"Number of chunks created: {len(text_chunks)}")

        # Create embeddings (vectorizing to create knowledge base, more usefull for semantic data then tabular data, but no better
        # short option for tabular data)
        st.info("Generating vectors for the data...")
        embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

        # Generate FAISS Knowledge Base
        docsearch = FAISS.from_documents(text_chunks, embeddings)

        # Save FAISS database locally
        docsearch.save_local(DB_FAISS_PATH)
        st.success("FAISS knowledge base created and saved locally.")

        # Load LLM
        llm = CTransformers(

            # Llama is used in GGML format as it is a huge model with billion parameters, so not runnable on our personal PCs locally,
            # and would cost extensive runing hours (ecpecially setting up cloud infrastructure not viable in this time). That also brings, token
            # restrictions, explained in the README.

            model="models/llama-2-7b-chat.ggmlv3.q4_0.bin",    
            model_type="llama",
            max_new_tokens=512,
            temperature=0
        )

        # Create Conversational Retrieval Chain
        qa = ConversationalRetrievalChain.from_llm(llm, retriever=docsearch.as_retriever())

        # Chat functionality
        chat_history = []
        query = st.text_input("Ask a question about the data:")

        if query:
            with st.spinner("Finding the best answer for your query..."):
                result = qa({"question": query, "chat_history": chat_history})
                chat_history.append((query, result['answer']))
                st.success("Response generated successfully!")
                st.write("Response:", result['answer'])

        # Cleanup the temporary file (to manage memroy overload for the POC)
        os.remove(temp_file_path)
