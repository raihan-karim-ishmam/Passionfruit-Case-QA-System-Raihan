# Instructions for Setting Up the Llama 2 model for LLM-Based CSV Q&A System

## Overview
This file provides step-by-step instructions for setting up the Llama2 GGML version to run the LLM-Based CSV Q&A System. Follow these steps:

---

## Requirements
Before you begin, ensure you have the following installed on your system:

- **Python** (Version 3.8 or above)


## Downloading the Llama 2 Model
To use the system, you need to download the **Llama 2 Model** in GGML format. Follow these steps:

1. Navigate to the following link:
   [Llama 2 Model on HuggingFace](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)

2. Download the model file:
   ```
   llama-2-7b-chat.ggmlv3.q4_0.bin
   ```

3. Save the downloaded file to the `models` directory in the repository.

4. Ensure the model file is located at:
   ```
   <repository-root>/models/llama-2-7b-chat.ggmlv3.q4_0.bin
   ```

---

## Notes
- **Model Setup**: Ensure that the Llama 2 model is downloaded and placed correctly; otherwise, the application will not function.
- **System Requirements**: Running the GGML format of the model requires a minimum of 16GB RAM for smooth operation.

---

## Future Improvements
- Full Llama 2 model integration with GPU support.
- Transition to a cloud-based environment for enhanced scalability.

---

For further details, consult the project README file.