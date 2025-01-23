# Smart CSV Q&A Agent featuring PandasAI and BambooLLM

## Overview
The **PandasAI Agent with BambooLLM** is a proof-of-concept (POC) designed to showcase the potential of developing an intelligent Q&A system for querying CSV files. The system processes user-uploaded CSV files, optimizes them for interaction with a large language model (LLM), and enables users to ask natural language questions about the data. A flagship feature of this method is the ability to train and customize the agent for specific use cases, providing unparalleled flexibility and adaptability. The project highlights the capabilities of **PandasAI**, one of the most renowned libraries for managing CSVs, combined with the state-of-the-art **BambooLLM**, which integrates seamlessly with PandasAI.

---

## Features

### CSV Preprocessing
- **Flexible File Handling**: Handles unconventional CSV formats with unusual delimiters (e.g., `|`) and normalizes them into a standard format.
- **Dynamic Column Handling**: Automatically detects and adjusts rows with varying column counts to create a uniform and efficient DataFrame.
- **Tested Optimization**: Preprocessing steps were refined through multiple testing rounds to achieve the most compatible structure for the LLM.

### PandasAI Integration
- **BambooLLM**: Selected for its compatibility with PandasAI, BambooLLM provides robust natural language processing and conversational querying capabilities.
- **SmartDataframe**: Facilitates natural language interaction with the preprocessed CSV data.
- **Dynamic Q&A**: Users can input questions, and the system responds with accurate answers extracted from the data.

### Interactive Querying
- **Simple Interface**: Uses Streamlit to provide an intuitive interface for uploading files, interacting with the chatbot, and viewing responses.
- **Chat History**: Stores conversation context for enhanced user experience.

---

## Versions

The system includes two application versions:

### App (Version 1)
- **Pre-Processed Data Input**: This version assumes the data has already been pre-processed using the provided script (`data_processing.py`) to ensure an optimized structure for the LLM.
- **Query-Only Functionality**: With the pre-processing handled separately, this version focuses solely on querying the LLM, minimizing potential data loss or confusion.
- **Efficiency**: By bypassing the in-app preprocessing, the LLM can process queries more efficiently and effectively.

### App v2 (Version 2)
- **Integrated Pre-Processing and Querying**: This version includes both pre-processing and querying within the same code.
- **Convenience**: Enables users to upload raw CSV files directly and handles preprocessing before querying.
- **Trade-Off**: While convenient, combining preprocessing and querying in the same workflow can occasionally result in minor data loss or confusion during LLM interactions.

For best results, we recommend using **App Version 1** with pre-processed data files. The script used to process the data, `data_processing.py`, is included in the repository for easy use.

---

## Setup Instructions

### API Key Configuration
To use **BambooLLM**, you need an API key:
1. Sign up for an API key at [BambooLLM](https://pandabi.ai).
2. Store the API key in a `.env` file in the root directory:
   ```env
   BAMBOO_API_KEY=your_bamboo_api_key_here
   ```
3. Alternatively, you can directly input the API key in the script where BambooLLM is initialized.

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
   streamlit run app.py  # For Version 1
   streamlit run app_v2.py  # For Version 2
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

---

## Current Limitations
1. **Reasoning and Complex Queries**:
   - While PandasAI excels at answering direct questions about the data, it struggles with reasoning-based or complex queries due to limitations of the base model and the current lack of fine-tuning.
   - The system performs well for direct data lookups but requires advanced configurations for multi-step reasoning.

2. **POC-Level Implementation**:
   - As a POC, the system lacks advanced features such as fine-tuned responses, fallback methods, and extensive customization.
   - It uses the free version of BambooLLM without additional optimizations.

3. **Temporary File Storage**:
   - Processed files are stored temporarily in the local filesystem, which limits scalability. Future versions will integrate cloud storage solutions.

---

## Future Work

1. **Agent Training**:
   - Train the PandasAI agent using various methods such as Q&A datasets, instruction-based training, or vector datasets. This will allow the system to provide highly customized responses tailored to specific domains.

2. **Custom Responses**:
   - Add fallback methods, error handling, and personalized responses to enhance the user experience and reinforce brand identity.

3. **Advanced Query Capabilities**:
   - Implement skills and functions in PandasAI for handling complex, multi-step queries.

4. **Cloud Integration**:
   - Move file processing and storage to the cloud (e.g., Azure), ensuring scalability and persistent data storage.

5. **Interface Enhancements**:
   - Develop a more user-friendly and visually appealing interface aligned with Passion Fruit's branding.

6. **Experimentation with LLMs**:
   - Test other LLMs supported by PandasAI to identify the best-performing model for specific datasets.

7. **Natural Conversation Flow**:
   - Transition from a simple Q&A system to a conversational agent that can simulate a natural dialogue experience.

---

## Acknowledgments
- **Streamlit**: For creating the interactive user interface.
- **Pandas**: For efficient data manipulation.
- **PandasAI**: For enabling natural language interaction with DataFrames.
- **BambooLLM**: For powering the system's natural language processing capabilities.

---

## Copyright

*Case developed by Raihan Karim for Passionfruit. © 2025 Raihan Karim. All rights reserved.*
