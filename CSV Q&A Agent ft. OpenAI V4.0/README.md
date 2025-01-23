# Passionfruit CSV Q&A Agent featuring OpenAI and Langchain

## Overview
The **Passionfruit CSV Q&A Agent** is a proof-of-concept (POC) tool that leverages OpenAI's GPT-powered capabilities to query CSV files. This POC is designed to provide quick and accurate insights into your data by combining the flexibility of natural language processing with a seamless interface. Built using **LangChain** and **Streamlit**, the system enables users to upload CSV files and ask questions about the data, receiving instant, precise responses. The project highlights the effectiveness of OpenAI and LangChain as a widely recognized combination for creating advanced AI applications.

A significant aspect of this development was optimizing the cost structure. Initially, the system processed the entire CSV file as input tokens for every query, incurring significant costs. This was resolved by modifying the workflow to upload the CSV file once and store it temporarily for subsequent queries, significantly reducing token consumption and costs. In production, the system will leverage cloud storage (e.g., Azure, AWS, or Google Cloud) to eliminate temporary file dependencies and enhance scalability.

---

## Features

### CSV Querying

- **Natural Language Interface**: Ask questions about your CSV data in plain English, and get precise, context-aware answers.
- **Support for Complex Queries**: Handles both simple questions (e.g., "What is the average value in column X?") and more advanced data exploration.
- **Context-Aware Responses**: Combines information from the CSV and external sources (when necessary) to provide complete answers.

### Powered by GPT Models

- **Model Comparisons**:
  - **GPT-3.5-turbo**: Performed exceptionally well, offering fast, accurate, and cost-effective results. It effectively combined external and internal data to answer queries accurately.
  - **GPT-3.5-turbo-0613**: Demonstrated good performance but faced potential depreciation issues, making it less viable for long-term use.
  - **GPT-4o-mini-2024**: Struggled with locating data in CSV files and frequently entered querying loops, ultimately failing to deliver reliable results.
  - **Text-Da-Vinci**: Underperformed but provided valuable insights for research purposes.
- **Optimized Token Usage**: The system was adjusted to process the CSV file once during upload, reducing costs by querying only the necessary data for each user input.

### Streamlined User Experience

- **Interactive Interface**: Built with Streamlit, offering a clean and visually appealing user interface with a Passionfruit-inspired theme.
- **Custom Design**: Added a touch of brand identity to the interface, including themed colors and dynamic elements.

---

## Requirements

### Python Version

- Python 3.8 or above

### Dependencies

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

The dependencies include:

- `streamlit`
- `langchain`
- `openai`
- `python-dotenv`

---

## Setup Instructions

### API Key Configuration

To use this application, you need an OpenAI API key:

1. Sign up for an API key at [OpenAI](https://platform.openai.com/signup/).
2. Store the API key in a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### Installation

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:

   ```bash
   streamlit run app.py
   ```

4. Open your browser and navigate to:

   ```
   http://localhost:8501
   ```

---

## How It Works

1. **Upload a CSV File**:

   - Users can upload a pre-processed CSV file for querying.

2. **Ask Questions**:

   - Input natural language queries about the data (e.g., "What is the total sum of column Y?").

3. **Receive Responses**:

   - The agent processes the query using the GPT model and provides an accurate answer.

4. **Error Handling**:

   - If an issue occurs during processing, the system provides meaningful feedback.

---

## Current Limitations

1. **Token Usage**: While optimized, token usage remains a cost factor for GPT-based systems.
2. **Temporary File Storage**: Currently uses temporary files for the CSV, which will be replaced with cloud storage in future versions.
3. **Free Tier Constraints**: Restricted by OpenAI’s API usage limitations for the free tier.
4. **Model Limitations**: More complex, reasoning-heavy queries may require advanced fine-tuning and model upgrades.
5. **No Source Referencing**: The model currently does not reference the source of the information in its responses. Adding this feature is a key priority for future development.

---

## Future Work

1. **Fine-Tuning**:

   - Train the system to better handle reasoning-heavy queries and improve performance.

2. **Function Calling**:

   - Implement function calls for direct querying of secure or proprietary datasets not included in the CSV file.

3. **Cloud Migration**:

   - Move file processing and storage to a cloud-based platform to improve scalability and efficiency.

4. **Custom Features**:

   - Add attributes for conversational tone customization and brand-specific interactions.

5. **Bigger Models**:

   - Experiment with advanced models like GPT-4 for enhanced reasoning and accuracy.

6. **Enhanced Interface**:

   - Improve the interface to offer a more friendly and dynamic experience, including brand-themed customization.

7. **Source Referencing**:

   - Enable the model to reference and indicate the source of the information used to generate responses, ensuring transparency and user trust.

---

## Acknowledgments

- **Streamlit**: For creating the interactive user interface.
- **LangChain**: For the seamless integration of language models.
- **OpenAI**: For providing the GPT models powering the agent.

---

*Case developed by Raihan Karim for Passionfruit. © 2025 Raihan Karim. All rights reserved.*