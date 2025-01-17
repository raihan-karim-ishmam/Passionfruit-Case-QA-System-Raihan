# REspective imports
import streamlit as st
import pandas as pd

def process_bar_separated_file(file):       #Preprocessing the file to mak it efficient for the llm (metrics derived after multiple tests)
    try:
        # Read the file line by line
        lines = file.getvalue().decode("utf-8").splitlines()

        # Split each line by the bar ('|') separator
        rows = [line.strip().split('|') for line in lines]

        # Find the maximum number of columns in any row
        max_columns = max(len(row) for row in rows)

        # Ensure all rows have the same number of columns by padding with None
        normalized_rows = [row + [None] * (max_columns - len(row)) for row in rows]

        # Convert to a DataFrame, using the first row as column names
        df = pd.DataFrame(normalized_rows[1:], columns=normalized_rows[0])

        # Convert DataFrame to CSV
        return df.to_csv(index=False)
    except Exception as e:
        st.error(f"Error processing file: {e}")
        return None

def main():
    st.title("Passionfruit Intelligent Q & A System")

    # Subsection for CSV Processor
    st.header("CSV Data Pre-processor")
    st.write("Upload your CSV file below and download the processed version compitable for upload to the agent.")

    # File uploader for CSV files
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        # Process the uploaded CSV
        processed_csv = process_bar_separated_file(uploaded_file)

        if processed_csv:
            # Display processed CSV content in a text area
            st.text_area("Processed CSV Data (Comma Separated)", processed_csv, height=200)

            # Provide a download button for the processed CSV
            st.download_button(
                "Download Processed CSV Data", 
                data=processed_csv, 
                file_name="Processed.csv"
            )
        else:
            st.error("Failed to process the CSV file.")

    # Subsection for Chat with the Agent
    st.header("Chat with Our Agent PassionFruity")
    st.write("Upload the data and start querying with the agent below.")

    # Embed the QandA pipeline created via vectorshift (N.B. SDK not used due to time limitations)
    st.markdown(
        """
        <iframe src="https://app.vectorshift.ai/forms/embedded/678958e9a0e46a1d83cf0d5f" 
        width="1000px" height="900px" allow="clipboard-read; clipboard-write; microphone"></iframe>
        """,
        unsafe_allow_html=True,     #Optional Security Trigger
    )

if __name__ == "__main__":
    main()
