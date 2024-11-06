# LLam2_on_cpu


Here's a refined and more engaging README, with emojis for added style!

---

# 📚 Local PDF-based QA with Quantized Llama Model 🚀

Welcome to this project, where we bring the power of AI to your local environment for document-based question-answering! Using a quantized version of the **Llama model** with **LangChain**, this setup is designed for efficient and offline-friendly performance.

### 🌟 Key Features
- **🖥️ Run Locally**: This project uses a quantized Llama model, optimized to work locally without the need for heavy GPU resources.
- **📄 PDF Document Retrieval**: Load and process PDF documents with ease from a designated directory.
- **🔍 Smart Text Splitting**: Documents are chunked into manageable parts to make embeddings and retrieval more effective.
- **⚡ FAISS Vector Store**: Stores embeddings for super-fast, semantic similarity searches.

### ⚙️ Requirements & Setup
To get started, install the required packages:
```bash
pip install langchain huggingface-transformers faiss-cpu ctransformers
```

### 📝 Code Workflow
1. **📂 Load PDF Files**: Automatically loads all PDF files in the `data/` directory.
2. **📏 Text Chunking**: `RecursiveCharacterTextSplitter` splits documents into smaller chunks, optimizing them for embedding and retrieval.
3. **🧠 Generate Embeddings**: Uses `HuggingFaceEmbeddings` with the `all-MiniLM-L6-v2` model. The `device` is set to 'cpu' for local, resource-friendly processing.
4. **🗃️ Vector Storage**: Embeddings are stored in a FAISS vector store, enabling high-speed and accurate retrieval.
5. **🤖 Initialize Llama Model**: A quantized Llama model (`llama-2-7b-chat.ggmlv3.q2_K.bin`) is loaded via `CTransformers` for effective local inference.
6. **💬 Prompt & Chain Setup**: A custom prompt template directs the Llama model to answer queries based on retrieved document content.

### 🛠️ Example Usage
Here’s how to ask questions based on your PDF content:
```python
user_input = "Tell me about Rainfall Measurement of the paper"
result = chain({'query': user_input})
print(f"Answer: {result['result']}")
```

### 📌 Project Highlights
This solution allows you to efficiently search and get insights from document-based data—all from your local machine! With the quantized Llama model, this project is optimized for offline usage and is ideal for those in resource-limited environments or without access to cloud services.

🌟 **Enjoy exploring and making the most of your document data with this local Llama-powered solution!**
