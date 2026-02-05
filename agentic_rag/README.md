![demo](./assets/demo.gif)

# 🤖 Agentic RAG with Agno & GPT-5

An intelligent Retrieval-Augmented Generation (RAG) system that combines the power of OpenAI's GPT-4o with advanced knowledge retrieval capabilities. This application allows you to load multiple web URLs into a knowledge base and ask questions that are answered using both the retrieved context and the language model's capabilities.

## ✨ Features

- **🧠 Dynamic Knowledge Base**: Load multiple URLs into a persistent vector database
- **🔍 Intelligent Retrieval**: Advanced semantic search using OpenAI embeddings
- **💬 Conversational Interface**: Streamlit-based chat interface for natural interactions
- **📊 Observable AI**: Integrated with Arize Phoenix for monitoring and tracing
- **🚀 Real-time Streaming**: Get responses as they're generated
- **🔄 Knowledge Management**: Easy loading, viewing, and resetting of knowledge base
- **⚡ Vector Search**: Lightning-fast similarity search using LanceDB

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Web URLs      │───▶│  Knowledge Base  │───▶│   Vector DB     │
│   (Sources)     │    │   (URL Content)  │    │   (LanceDB)     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Query    │───▶│   Agno Agent     │◀───│   Embeddings    │
└─────────────────┘    │   (GPT-4o)       │    │   (OpenAI)      │
                       └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │   RAG Response   │
                       │   (Generated)    │
                       └──────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API key
- Arize Phoenix API key (optional, for observability)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Ajaykumar496/rag.git
   cd rag/agentic_rag
   ```

2. **Install dependencies**:

   ```bash
   uv sync
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project directory:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ARIZE_PHOENIX_API_KEY=your_phoenix_api_key_here  # Optional
   ```

4. **Run the application**:
   ```bash
   uv run streamlit run main.py
   ```

## 📚 Usage Guide

### Step 1: Add URLs to Knowledge Base

1. In the sidebar, add one or more URLs containing the information you want to query
2. Click the **➕** button to add more URL fields
3. URLs can be documentation sites, articles, blogs, or any web content

### Step 2: Load Knowledge Base

1. Click **"Load Knowledge Base"** to process and index the URLs
2. Wait for the loading spinner to complete
3. You'll see a success message and the loaded URLs listed

### Step 3: Ask Questions

1. Use the chat input at the bottom to ask questions
2. The system will search the knowledge base and generate contextual answers
3. Responses are streamed in real-time

### Step 4: Manage Knowledge Base

- **View Loaded URLs**: See currently loaded URLs in the sidebar
- **Reset Knowledge Base**: Click **"🔄 Reset KB"** to clear and start over
- **Add More URLs**: Add new URLs and reload the knowledge base

## 🔧 Configuration

### Vector Database Settings

```python
vector_db=LanceDb(
    table_name="mcp-docs-knowledge-base",  # Table name for storing vectors
    uri="tmp/lancedb",                     # Local storage path
    search_type=SearchType.vector,         # Search algorithm
    embedder=OpenAIEmbedder(id="text-embedding-3-small")  # Embedding model
)
```

### Model Configuration

```python
model=OpenAIChat(id="gpt-4o")  # Can be changed to other OpenAI models
```

## 📊 Observability with Arize Phoenix

This application integrates with Arize Phoenix for comprehensive monitoring:

- **Request Tracing**: Track all API calls and responses
- **Performance Monitoring**: Monitor latency and token usage
- **Error Tracking**: Capture and analyze failures
- **Usage Analytics**: Understand query patterns and knowledge base effectiveness

Visit [Arize Phoenix](https://app.phoenix.arize.com) to view your traces and analytics.

## 🛠️ Key Components

### Core Functions

- **`load_knowledge_base(urls)`**: Processes URLs and creates vector embeddings
- **`agentic_rag_response(urls, query)`**: Generates responses using RAG methodology

### Technologies Used

- **[Agno](https://github.com/agno-ai/agno)**: AI agent framework
- **[Streamlit](https://streamlit.io/)**: Web interface
- **[LanceDB](https://lancedb.com/)**: Vector database
- **[OpenAI](https://openai.com/)**: Language model and embeddings
- **[Arize Phoenix](https://phoenix.arize.com/)**: AI observability

## 📝 Example Use Cases

1. **Documentation Q&A**: Load API documentation and ask implementation questions
2. **Research Assistant**: Index research papers and query specific topics
3. **Company Knowledge Base**: Load internal documents and policies for employee queries
4. **Educational Content**: Index course materials and ask study questions
5. **News Analysis**: Load news articles and ask analytical questions

## 🔒 Security & Privacy

- **Local Processing**: Vector database is stored locally in `tmp/lancedb`
- **API Security**: OpenAI API keys are securely handled through environment variables
- **Data Control**: You control what URLs are indexed and can reset the knowledge base anytime

## 🐛 Troubleshooting

### Common Issues

1. **"Knowledge base not loaded" error**:

   - Ensure you've clicked "Load Knowledge Base" after adding URLs
   - Check that URLs are accessible and contain readable content

2. **OpenAI API errors**:

   - Verify your API key is correct and has sufficient credits
   - Check internet connectivity

3. **Vector database issues**:
   - Clear the `tmp/lancedb` directory if you encounter database corruption
   - Restart the application

### Performance Tips

- **URL Selection**: Choose URLs with high-quality, relevant content
- **Knowledge Base Size**: Larger knowledge bases may take longer to load but provide more comprehensive answers
- **Query Specificity**: More specific questions generally yield better results

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
