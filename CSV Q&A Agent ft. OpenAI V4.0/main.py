from langchain_experimental.agents import create_csv_agent
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Streamlit app
def main():
    # Set Streamlit page configuration
    st.set_page_config(
        page_title="Passionfruit CSV Q&A Agent",
        page_icon="🍍",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    # Header section
    st.markdown(
        """
        <style>
        .header-title {
            font-size: 2rem;
            font-weight: bold;
            color: #6B3E26; /* Passionfruit-like color */
            text-align: center;
        }
        .sub-header {
            color: #FF8C42;
            text-align: center;
        }
        </style>
        <h1 class="header-title">Passionfruit CSV Q&A Agent 🍍</h1>
        <p class="sub-header">Upload a CSV file and ask GPT-powered questions about your data.</p>
        """,
        unsafe_allow_html=True
    )

    # File uploader
    csv_file = st.file_uploader(
        label="📤 Upload your CSV file:",
        type="csv",
        help="The file should be a processed CSV for optimal results."
    )

    # File validation and agent creation
    if csv_file is not None:
        # Show a success message when a file is uploaded
        st.success("✅ CSV file uploaded successfully!")
        
        # Create the agent
        agent = create_csv_agent(
            
            # Models tested:
            # gpt-4o-mini-2024-07-18 = Poor Result, gets stuck in look mostly
            # gpt-3.5-turbo = Very good perfromanc with almost all correct answers, also when info outside database need.
            # These two are the flagship cheap models to be used with asnwer in seconds.

            ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2),
            csv_file,
            verbose=True,
            allow_dangerous_code=True
        )

        # Input for user questions
        user_question = st.text_input(
            "💬 Ask a question about your CSV:",
            placeholder="E.g., What is the average value in column X?"
        )

        if user_question:
            # Process the query
            with st.spinner("🤔 Analyzing your question..."):
                try:
                    response = agent.run(user_question)
                    st.markdown("### ✨ Response:")
                    st.write(response)
                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")
    else:
        # Show a message if no file is uploaded
        st.warning("⚠️ Please upload a CSV file to get started.")

    # Footer
    st.markdown(
        """
        <hr style="border: 1px solid #FF8C42;">
        <p style="text-align: center; color: #6B3E26;">
            Powered by <strong>Passionfruit 🍍</strong>
        </p>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
