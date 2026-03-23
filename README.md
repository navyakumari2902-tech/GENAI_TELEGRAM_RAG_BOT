# 🤖 GenAI Telegram RAG Bot

A Retrieval-Augmented Generation (RAG) based Telegram bot that answers questions strictly from uploaded documents.

---

## 🚀 Features

- 📂 Document-based Q&A (RAG)
- 🔍 Semantic search using embeddings
- 🧠 Retrieval + Re-ranking logic
- ❌ No hallucination (answers only from documents)
- ⚡ In-memory caching (faster repeated queries)
- 🤖 Telegram bot interface
- 🔄 Auto index rebuild when documents change

---

## 🏗️ Tech Stack

- Python
- LlamaIndex
- HuggingFace Embeddings (`all-MiniLM-L6-v2`)
- Ollama (optional)
- Telegram Bot API

---

## 📁 Project Structure
  genai-telegram-rag-bot/
├── Data/                   # Knowledge Base: Input documents (txt/md)
│   ├── doc1.txt            # e.g., Company Policies
│   ├── doc2.txt            # e.g., Technical FAQs
│   └── ...                 
├── rag/                    # Core AI Logic
│   ├── __init__.py
│   ├── loader.py           # Document ingestion & semantic chunking
│   └── rag_pipeline.py     # Embedding logic & LLM orchestration
├── storage/                # Persistent Vector Database (SQLite-vec)
├── tests/                  # Automated Test Suite (Pytest)
│   ├── test_rag.py         # Retrieval accuracy tests
│   ├── test_integration.py # End-to-end pipeline checks
│   ├── test_cache.py       # Performance & Caching verification
│   └── test_bot.py         # Telegram handler mocks
├── main.py                 # Application Entry Point & Bot Interface
├── requirements.txt        # Project dependencies
└── README.md               # Documentation & Design Decisions
└── Feature_implementations.md #Features implemented list 
└── key_decisions.md        # Key decisions taken 

---

## ⚙️ Setup Instructions

### Clone the repository
'''bash
git clone https://github.com/navyakumari2902-tech/GENAI_TELEGRAM_RAG_BOT.git
cd genai-telegram-rag-bot
'''

### Create and activate virtual environment
'''bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows (PowerShell)
'''
###  3️. Install Dependencies
'''bash
pip install -r requirements.txt
'''

### 4. Documents 
'''bash
Place your .txt files inside:
- Data/
'''

### 5. Set Telegram Bot Token

In main.py:

BOT_TOKEN = "8646544195:AAFVKiGW9yalZ7QzT4kUdEMN1nV9shzealQ"
BOT_Username = @navya2904_bot

### 6. Build RAG Index (IMPORTANT)
'''bash
python -m rag.rag_pipeline
'''

This step will:
           - Load documents
           - Generate embeddings
           - Store vector index in storage/

### 7. Run Telegram Bot
'''bash
python main.py
'''

Example Usage
Start the bot:/start

Ask questions:What is RAG?
or:
/ask What is machine learning?

Get help:/help
🧪 Example Queries
- What is RAG?
- What is machine learning?
- What is a vector database?
- Who is Vara?

---
## Testing 
- python -m tests.test_rag
- python -m tests.test_integration
- python -m tests.test_cache
- python -m tests.test_bot


