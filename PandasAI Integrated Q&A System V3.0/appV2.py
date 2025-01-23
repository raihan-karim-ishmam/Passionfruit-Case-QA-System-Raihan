import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import BambooLLM
import tempfile

# Initialize BambooLLM with your API key
# llm = BambooLLM(api_key="your_bamboo_api_key_here") 

llm = BambooLLM()       # If you have saved the API KEY in your .env variable, the code will fetch it automatically

# Function to preprocess uploaded CSV file to fit into right format for the LLM
def preprocess_file(file):
    """
    Preprocess the NEVO file to ensure:
    - Proper column headers are added.
    - Consistent row structure.
    - Saved as a clean CSV.
    """
    try:
        st.info("Reading and preprocessing the uploaded file...")
        lines = file.getvalue().decode("utf-8").splitlines()
        rows = [line.strip().split('|') for line in lines]

        # Use the first row as headers
        headers = rows[0]
        data = rows[1:]

        # Find the maximum number of columns in any row
        max_columns = max(len(row) for row in data)

        # Normalize rows by padding with None to match the maximum column count
        normalized_rows = [row + [None] * (max_columns - len(row)) for row in data]

        # Create a DataFrame
        df = pd.DataFrame(normalized_rows, columns=headers)

        st.success("File preprocessed successfully!")
        return df
    except Exception as e:
        st.error(f"Error during preprocessing: {e}")
        return None

# Streamlit app
st.title("PandasAI Chatbot with BambooLLM")
st.subheader("Ask questions about the uploaded CSV file!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Upload CSV
uploaded_file = st.file_uploader("Upload your NEVO CSV file", type=["csv"])
if uploaded_file:
    try:
        # Preprocess the uploaded file
        df = preprocess_file(uploaded_file)
        if df is not None:
            st.write("CSV successfully loaded and preprocessed!")

            # Save the preprocessed CSV to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
                df.to_csv(temp_file.name, index=False)
                temp_file_path = temp_file.name

            # Initialize SmartDataframe with BambooLLM
            smart_df = SmartDataframe(df, config={"llm": llm})

    # At this stage a very simple and straightforward question and answer is setup for the Q&A POC, on the bigger 
    # time frame, advanced options form pandasai will be added such as Response Structure definition, Query training,
    # default response and more.

            # User input
            user_input = st.text_input("You:", "")
            if st.button("Send") and user_input.strip():
                try:
                    # Query the CSV with SmartDataframe
                    csv_response = smart_df.chat(user_input)
                except Exception as e:
                    csv_response = f"Error processing CSV query: {str(e)}"

                # Store messages
                st.session_state.messages.append({"user": user_input, "bot": csv_response})

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Display chat history
for message in st.session_state.messages:
    st.markdown(f"**You:** {message['user']}")
    st.markdown(f"**Bot:** {message['bot']}\n")
