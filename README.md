# Q&A Project Using LangChain

This project is a Question and Answer (Q&A) system built using LangChain, designed to extract information from various document formats, including PDFs, Word documents, and PowerPoint presentations. It leverages embeddings and retrieval techniques to generate precise answers based on document content and user queries.

To use this project, start by cloning the repository and installing the dependencies listed in `requirements.txt`. This project requires API keys from Hugging Face, Google, and Cohere to access essential embedding and language model services. Set these API keys as environment variables on your system:
```bash
export HuggingFaceHub_API_Token='your_huggingface_token'
export GOOGLE_API_KEY='your_google_api_key'
export cohere_api_key='your_cohere_api_key'

