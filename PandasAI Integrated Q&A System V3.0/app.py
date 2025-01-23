import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import BambooLLM

# Initialize BambooLLM with your API key
# llm = BambooLLM(api_key="your_bamboo_api_key_here") 

llm = BambooLLM()       # If you have saved the API KEY in your .env variable, the code will fetch it automatically

# Streamlit app
st.title("PandasAI Chatbot with BambooLLM")
st.subheader("Ask questions about the uploaded CSV file!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    # Load the uploaded CSV into a pandas DataFrame
    df = pd.read_csv(uploaded_file)
    st.write("CSV successfully loaded!")

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

# Display chat history
for message in st.session_state.messages:
    st.markdown(f"**You:** {message['user']}")
    st.markdown(f"**Bot:** {message['bot']}\n")
