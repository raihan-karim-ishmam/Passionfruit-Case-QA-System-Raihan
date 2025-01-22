# LLM-Based CSV Q&A System Featuring Llama 2 by Meta

## Overview
The **LLM-Based CSV Q&A System** is a demonstration of how a personal, open-source LLM-based approach can be used to develop Q&A systems. The primary goal of this project is to showcase a proprietary development methodology where the entire system is built using open-source components, ensuring full ownership, customizability, and the potential for trademarking and patenting. By exclusively using open-source LLMs, embeddings, and databases, this approach eliminates dependency on external tools, extensions, or recurring costs, making it a completely autonomous solution.

### Disclaimer
This project is a **proof of concept (POC)** designed to illustrate the structure and feasibility of such a system. Due to constraints such as limited hardware resources, time, and the use of a reduced LLM in GGML format, the current implementation has significant limitations:
- **Accuracy**: The model's accuracy is low because the data is chunked to fit the constraints of the reduced LLM version, which is not ideal for tabular data.
- **Performance**: The reduced LLM format limits the ability to process the entire dataset cohesively, resulting in disconnected and often incorrect answers.
- **Purpose**: The current system is not intended for production use but to demonstrate how this methodology can be scaled and improved with additional resources.

Despite these limitations, this POC provides a foundation for building a robust, fully proprietary Q&A system in the future.

## Features
### CSV Preprocessing
- **Delimiter Normalization**: Converts bar-separated (`|`) CSV files into standard comma-separated format (`.csv`).
- **Error Handling**: Ensures consistent column lengths by normalizing rows, handling irregular delimiters, and managing missing values.
- **Temporary File Management**: Utilizes temporary files for efficient in-memory operations and cleanup to optimize system resources.

### Knowledge Base Generation
- **Text Chunking**: Splits text into manageable chunks using **RecursiveCharacterTextSplitter**, ensuring efficient LLM tokenization and response generation.
- **Embeddings**: Creates vector representations using **HuggingFace Embeddings** (`sentence-transformers/all-MiniLM-L6-v2`), optimized for semantic similarity and context understanding.
- **FAISS Vector Store**: Selected for its efficiency with numerical and tabular data, FAISS provides a robust solution for fast and scalable vector storage and querying.

### LLM Integration
- **Meta's Llama 2 Model**: Utilized in GGML format for efficient local inference on limited hardware. Llama 2 is one of the top-performing open-source LLMs, making it a natural choice for this system.
- **Conversational Retrieval Chain**: Combines vector-based retrieval and LLM-powered response generation, enabling context-aware and conversational querying.
- **Token Optimization**: Implements chunking and token limits to accommodate local hardware constraints.

### Interactive Querying
- **Dynamic Q&A**: Allows users to input questions about the data and retrieve precise answers in real-time.
- **Chat History**: Maintains conversation context for enhanced user experience and coherent multi-turn dialogues.

### Streamlit Interface
The application uses **Streamlit** to provide a simple and interactive interface for uploading files, displaying results, and querying the processed data. Its ease of use makes the system accessible for both developers and non-technical users.

## Requirements
To run the application, ensure the following dependencies are installed:

```
streamlit
pandas
langchain
langchain-community
sentence-transformers
faiss-cpu
ctransformers
```

Install the dependencies using:

```bash
pip install -r requirements.txt
```

## Download the Llama 2 Model
To use the system, you need to download the **Llama 2 Model** in GGML format. Follow these steps:

1. Download the model file `llama-2-7b-chat.ggmlv3.q4_0.bin` from the following link:
   [Llama 2 Model on HuggingFace](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)

2. Save the model file in the `models` directory of this repository.

3. Detailed instructions are also provided in the `instructions.md` file located in the `models` directory.

## Installation and Usage
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

4. **Access the App**:
   Open your browser and navigate to the Local URL provided in the terminal, usually `http://localhost:8501`, to interact with the Q&A Agent.

## Technical Details
- **Preprocessing**:
  - Bar-separated files are normalized to CSV format with consistent column lengths.
  - Errors are managed gracefully, and temporary files are used to avoid memory overload.

- **Knowledge Base**:
  - Text chunks are generated for efficient token usage.
  - FAISS is utilized for vector storage and fast semantic querying.

- **LLM Integration**:
  - Llama 2 is used in GGML format for its efficiency in resource-constrained environments.
  - Conversational chains ensure context-aware responses by maintaining chat history.

- **Performance Optimization**:
  - Recursive text splitting and token limits optimize performance for local hardware.
  - Temporary files prevent memory overload in high-volume operations.

## Future Work
1. **Full-Scale LLM Integration**:
   - Transition to the original Llama 2 model with full token limits, eliminating the need for data chunking.
   - Enable GPU integration to enhance processing power and leverage larger LLMs effectively.

2. **Cloud Migration**:
   - Move the system to a cloud environment, allowing the vector data to be stored persistently. Once vectors are generated, they can be reused for queries without regeneration, significantly improving efficiency.

3. **Enhanced Interface**:
   - Develop a polished, branded interface to improve usability and user experience.

4. **Metadata Indexing**:
   - Introduce metadata indexing in the data loading process. By associating data frames with structured metadata, the LLM can query the data more efficiently, leading to faster and more accurate responses.

5. **Fine-Tuning and Optimization**:
   - Fine-tune the LLM for domain-specific tasks and optimize metadata indexing to align with specific use cases.

6. **Scalability and Advanced Features**:
   - Experiment with larger vector stores and additional indexing techniques to handle larger datasets.
   - Explore advanced retrieval methods for integrating multiple data sources seamlessly.

## Limitations
- **Hardware Constraints**: The current system is designed for local hardware and may encounter limitations with large datasets or queries.
- **Token Limits**: The Llama 2 model's token constraints require careful preprocessing and chunking.
- **Accuracy Limitations**: The current setup produces low accuracy due to data chunking required for the reduced LLM version.

## Contributing
Contributions are welcome! If you have suggestions for improvements or additional features, please submit a pull request or open an issue.

## Acknowledgments
Special thanks to the tools and frameworks that made this project possible:
- **Streamlit**: For the interactive user interface.
- **Pandas**: For efficient data preprocessing.
- **FAISS**: For fast and scalable vector storage.
- **LangChain**: For conversational and retrieval-based AI workflows.
- **Meta Llama 2**: For powering the LLM-driven responses.
- **HuggingFace**: For embedding models enabling semantic similarity.


*Case developed by Raihan Karim for Passionfruit. © 2025 Raihan Karim. All rights reserved.*