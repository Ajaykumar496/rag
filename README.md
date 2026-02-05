# Agentic RAG with Agno & GPT-4o

Built by **Ajaykumar**

An intelligent Retrieval-Augmented Generation (RAG) system I built that combines OpenAI's GPT-4o with advanced knowledge retrieval. Load multiple web URLs into a knowledge base and ask questions — the system retrieves relevant context and generates accurate answers using both the indexed content and the language model.

## Features

- **Dynamic Knowledge Base** — Load multiple URLs into a persistent vector database
- **Semantic Search** — Intelligent retrieval using OpenAI embeddings
- **Chat Interface** — Streamlit-based conversational UI
- **Observability** — Integrated with Arize Phoenix for monitoring and tracing
- **Real-time Streaming** — Responses streamed as they're generated
- **Knowledge Management** — Load, view, and reset the knowledge base easily
- **Vector Search** — Fast similarity search powered by LanceDB

## Architecture

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

## Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key
- Arize Phoenix API key (optional, for observability)

### Installation

1. **Clone the repo**:

   ```bash
   git clone https://github.com/Ajaykumar496/rag.git
   cd rag/agentic_rag
   ```

2. **Install dependencies**:

   ```bash
   uv sync
   ```

3. **Set up environment variables** — create a `.env` file:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ARIZE_PHOENIX_API_KEY=your_phoenix_api_key_here  # Optional
   ```

4. **Run the app**:
   ```bash
   uv run streamlit run main.py
   ```

## How to Use

### 1. Add URLs

- In the sidebar, enter one or more URLs you want to query
- Click **+** to add more URL fields
- Any web content works — docs, articles, blogs, etc.

### 2. Load Knowledge Base

- Click **"Load Knowledge Base"** to process and index the URLs
- Wait for loading to finish — you'll see a success message with the loaded URLs

### 3. Ask Questions

- Type your question in the chat input
- The system searches the knowledge base and streams a contextual answer

### 4. Manage Knowledge Base

- **View Loaded URLs** in the sidebar
- **Reset** with the **"Reset KB"** button to clear and start fresh
- **Add More URLs** anytime and reload

## Configuration

### Vector Database

```python
vector_db=LanceDb(
    table_name="mcp-docs-knowledge-base",
    uri="tmp/lancedb",
    search_type=SearchType.vector,
    embedder=OpenAIEmbedder(id="text-embedding-3-small")
)
```

### Model

```python
model=OpenAIChat(id="gpt-4o")  # Can swap for other OpenAI models
```

## Observability

Integrated with Arize Phoenix for monitoring:

- **Request Tracing** — Track all API calls and responses
- **Performance Monitoring** — Latency and token usage
- **Error Tracking** — Capture and analyze failures
- **Usage Analytics** — Query patterns and knowledge base effectiveness

Visit [Arize Phoenix](https://app.phoenix.arize.com) to view traces and analytics.

## Tech Stack

| Technology | Purpose |
|---|---|
| [Agno](https://github.com/agno-ai/agno) | AI agent framework |
| [Streamlit](https://streamlit.io/) | Web interface |
| [LanceDB](https://lancedb.com/) | Vector database |
| [OpenAI](https://openai.com/) | LLM and embeddings |
| [Arize Phoenix](https://phoenix.arize.com/) | AI observability |

## Core Functions

- **`load_knowledge_base(urls)`** — Processes URLs and creates vector embeddings
- **`agentic_rag_response(urls, query)`** — Generates responses using RAG

## Use Cases

- **Documentation Q&A** — Load API docs and ask implementation questions
- **Research Assistant** — Index papers and query specific topics
- **Company Knowledge Base** — Internal documents and policies
- **Educational Content** — Course materials and study questions
- **News Analysis** — Load articles and ask analytical questions

## Troubleshooting

**"Knowledge base not loaded" error:**
- Make sure you clicked "Load Knowledge Base" after adding URLs
- Check that URLs are accessible and contain readable content

**OpenAI API errors:**
- Verify your API key and credits
- Check internet connectivity

**Vector database issues:**
- Clear the `tmp/lancedb` directory if corruption occurs
- Restart the application

## Contributing

Contributions are welcome! Feel free to open issues, feature requests, or pull requests.

## License

MIT License — see the LICENSE file for details.
