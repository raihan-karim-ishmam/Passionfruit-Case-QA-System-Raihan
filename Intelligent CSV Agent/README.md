# CSV Agent

## Overview
The **CSV Agent** is a robust and user-friendly tool designed to simplify CSV file processing and facilitate seamless interaction with advanced language models (LLMs). It excels in scenarios where users need to clean, process, and normalize complex CSV datasets, enabling these datasets to be queried efficiently by cutting-edge LLMs. This tool is particularly valuable for projects requiring fast, accurate data retrieval and intelligent decision-making, such as data-driven research, automated reporting, and dynamic knowledge querying. This application allows users to process delimited CSV files and provides an embedded interface for querying a pipeline created with advanced AI tools. It is ideal for developers, data scientists, and AI enthusiasts looking to work with LLMs efficiently and effectively.

## Features
### CSV Processor
- **Delimiter Transformation**: Converts bar-delimited (`|`) CSV files into standard comma-separated format (`.csv`).
- **Error Handling**: Ensures robust file parsing, automatically normalizing rows and handling irregular column counts.
- **Interactive Processing**: Users can upload a raw CSV file, preview the processed data, and download the cleaned file.

#### Development and Testing Process
The pre-processing pipeline for CSV files was developed after multiple rounds of testing. Initially, raw CSV files were directly used, but this approach led to challenges such as:
1. **Inaccuracy in Model Responses**: Early tests showed an accuracy of approximately 60-70%, with models correctly answering only 6-7 out of 10 questions.
2. **Frequent Errors**: The raw CSV files often contained unusual delimiters and inconsistent structuring, which caused errors during processing and reduced model efficiency.

Each iteration of testing and troubleshooting informed improvements to the pre-processing logic, leading to:
- Enhanced **accuracy**, now achieving approximately 90-95% accuracy, with 9-10 correct answers out of 10 questions.
- Improved **efficiency**, with processing time reduced by an estimated 15-20%.

The current version of the CSV processing block is optimized for compatibility with LLMs, ensuring that the data is structured in a way that allows the models to perform at their best.

### Query LLM Pipeline
- **Pipeline Structure**: The pipeline is designed with two primary inputs: the CSV data and the user query. These are fed into a **retrieval agent** built using **VectorShift**. The agent retrieves an answer directly from the CSV data if possible. If it cannot retrieve a specific answer, it uses an LLM to generate a response based on general knowledge or its internal data, effectively avoiding the need for additional web search functionality. However, this limits the ability to provide web-sourced answers, which is planned as a future enhancement.
- **Chat History Integration**: The pipeline incorporates chat history, allowing a defined amount of previous context (adjustable by token limits) to be stored and referenced. This enables the agent to provide more coherent and contextually aware responses.
- **Final Answer Generation**: The query results, along with the chat history, are fed into another **OpenAI LLM** that makes the final decision and generates the answer provided to the user.

### Modular Design
The application is built using **Streamlit**, ensuring modularity, simplicity, and easy customization. Developers can extend the functionality as needed.

## Requirements
To run this application, ensure you have the following Python dependencies installed:

```
streamlit
pandas
```

You can install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

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
   Open your browser and navigate to the Local URL provided in the terminal, usually `http://localhost:8501`, to interact with the CSV Agent.

## Technical Details
- The **CSV Processor** uses a custom method to:
  - Parse bar-separated (`|`) CSV files.
  - Normalize rows with varying column counts.
  - Preserve headers and save the processed file in a standardized format.

- The **Query LLM Pipeline** leverages a preconfigured pipeline created using advanced tools for efficient interaction with top-tier LLMs.

### Note on SDK and Prompt Engineering
This implementation avoids detailed prompt engineering and SDK usage due to time constraints. For more extensive customization, the **VectorShift SDK** is available, offering:
- Fine-tuned control over AI workflows.
- Advanced prompt engineering for specific use cases.

## Future Work
As we move forward with a longer timeline, the following enhancements are planned:
1. **Pipeline Implementation via SDK**: Transitioning the pipeline to the **VectorShift SDK** will provide more control and features for prompt engineering and feature engineering within the flow. This will allow for finer customization and optimization of the knowledge querying process.
2. **Exploration of Diverse Knowledge Bases**: Installing and testing a wider range of knowledge bases to identify the most optimized querying configurations.
3. **Upgrade to Advanced Tiers**: Currently leveraging the free tier, we plan to upgrade to higher tiers of VectorShift for access to enhanced SDK functionalities and better model capabilities.
4. **Enhanced Interface Design**: Developing a more polished and user-centric interface aligned with Passion Fruit's branding guidelines to improve usability and visual appeal.
5. **Incorporation of Web-Sourced Answers**: Integrating the ability to provide web-sourced answers in addition to responses based on CSV data and internal knowledge.
6. **Proof of Concept Expansion**: While this is a basic proof of concept, further refinements will aim to make the tool more robust and production-ready.

## Limitations
- **File Size**: Processing very large CSV files may lead to performance degradation due to memory constraints.
- **Customizations**: Additional features like specific data validations or transformations need to be implemented as extensions.

## Acknowledgments
Special thanks to the tools and frameworks that made this project possible:
- **Streamlit**: For creating an intuitive interface.
- **Pandas**: For powerful data manipulation capabilities.
- **VectorShift**: For providing a reliable platform to design and host AI pipelines.

Case developed by Raihan Karim for Passionfruit. © 2025 Raihan Karim. All rights reserved.