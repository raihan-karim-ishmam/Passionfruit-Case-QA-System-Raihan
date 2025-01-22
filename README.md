# Case Study: CSV-Based Q&A System

## Overview
This repository was developed as part of a case study assignment to create a **CSV-based Q&A system**. The system allows users to query a CSV file, retrieve answers, and handle errors effectively. The project expands upon the initial requirements by delivering **two distinct implementations**:

1. **Intelligent CSV Agent featuring VectorShift**: Focused on accuracy and efficiency.
2. **LLM-Based CSV Q&A System featuring Llama 2**: Built with open-source components for full customizability.

Both implementations demonstrate different approaches to solving the case, providing versatility and insight into advanced language model (LLM) workflows.

---

## Case Study Requirements
The project aimed to:
- Create a **Q&A system** capable of reading a CSV file and answering user questions.
- Optimize the CSV file for processing by normalizing columns and handling inconsistencies.
- Integrate an LLM for accurate question-answering, while managing token and memory limitations.

The original dataset was a **food database** containing:
- Food names (both in Dutch and English).
- Food types and categories.
- Energy content (in kcal) and other nutritional information.

---

## Two Implementations

### **1. Intelligent CSV Agent featuring VectorShift**
- **Goal**: Provide an efficient and modular CSV processing system integrated with advanced LLMs.
- **Key Features**:
  - Robust CSV normalization and error handling.
  - Query pipeline using **VectorShift**, ensuring accurate and contextual responses.
  - Modular design implemented using **Streamlit**.
- **Details**: Refer to the `Intelligent CSV Agent` directory for more information.

### **2. LLM-Based CSV Q&A System featuring Llama 2**
- **Goal**: Leverage open-source tools for a fully autonomous system without external dependencies.
- **Key Features**:
  - Local inference using **Llama 2** (in GGML format).
  - Vectorization with **HuggingFace Embeddings** and storage in a **FAISS vector store**.
  - Interactive querying via a **Conversational Retrieval Chain**.
- **Details**: Refer to the `LLM-Based CSV Q&A System` directory for more information.

---

## Installation and Setup

### Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### Install Dependencies
Ensure all required Python libraries are installed for each of the two directories:
```bash
pip install -r requirements.txt
```

### Explore Each Implementation
Navigate to the respective directories (`Intelligent CSV Agent V1.0` or `Llama Based Q&A System V2.0`) for detailed setup instructions and feature highlights.

---

## Key Highlights
1. **Two Distinct Approaches**:
   - The **VectorShift-based model** excels in accuracy and modularity.
   - The **Llama 2-based model** demonstrates the feasibility of a fully open-source solution.

2. **Scalable Design**:
   - Both systems are designed to handle CSV data efficiently and support future enhancements.

3. **Future Improvements**:
   - Integration of web-sourced answers for enhanced knowledge.
   - Migration to a cloud-based infrastructure for better scalability.

---

## Acknowledgments
This project is a demonstration of innovation in AI and showcases the use of tools like:
- **Streamlit**: For an intuitive user interface.
- **LangChain**: For conversational AI workflows.
- **FAISS**: For vector storage and retrieval.
- **Meta Llama 2**: For powering open-source LLM capabilities.



*Developed by Raihan Karim for Passionfruit. © 2025 Raihan Karim. All rights reserved.*