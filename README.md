# LLam2_on_cpu

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

Here’s an extended section that describes the Llama model, highlighting its quantized setup and its relevance for local, resource-efficient usage:

---

### 🦙 About the Llama Model

The **Llama model** (Large Language Model Meta AI) is a powerful language model developed by Meta, known for its efficiency and ability to perform well across various natural language processing tasks. In this project, we’re using a **quantized version of Llama-2 (7B)**, specifically the **llama-2-7b-chat.ggmlv3.q2_K.bin** model file, which brings several unique benefits:

- **🚀 Lightweight & Efficient**: The quantized version reduces model size without a significant loss in performance. Quantization is a technique that optimizes the model by reducing the precision of its weights, making it lightweight and faster for inference.
- **🧩 Memory-Friendly**: Thanks to quantization, this model runs smoothly on CPUs, allowing you to execute advanced language tasks locally even if you lack GPU resources.
- **⚡ Quick Response Times**: With a 7-billion parameter setup, this model strikes a balance between performance and efficiency, providing quick and contextually relevant answers in a small memory footprint.
- **🤖 Optimized for QA Tasks**: This version of Llama-2 has been adapted for conversational tasks, making it ideal for answering questions based on specific context—perfect for our retrieval-based QA setup!

### Why Use a Quantized Model?
Quantized models like this version of Llama-2 are highly beneficial for those needing **high-performance NLP capabilities** in a **resource-limited environment**. Since the model size is significantly reduced, you can achieve nearly the same level of performance as the full model, but with a fraction of the compute requirements.

