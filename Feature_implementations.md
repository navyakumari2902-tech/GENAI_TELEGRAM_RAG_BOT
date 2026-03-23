## 🛠️ Implementation Details

This project includes several custom-built components beyond basic RAG implementation.

---

### 📂 1. Document Loading & Processing

- Implemented custom document loader (`loader.py`)
- Reads `.txt` files from `Data/` directory
- Converts them into LlamaIndex-compatible documents

---

### 🔍 2. Vector Index Creation

- Built vector index using `SimpleVectorStore`
- Used HuggingFace embeddings (`all-MiniLM-L6-v2`)
- Stored locally in `storage/` directory

---

### 🔄 3. Automatic Index Management

- Implemented `should_rebuild()` logic
- Detects changes in document files
- Rebuilds index only when required

---

### ⚡ 4. Query Pipeline (`query_rag`)

Core logic includes:

- Input validation (empty query handling)
- Greeting handling (`hi`, `hello`, etc.)
- Retrieval using similarity search (`top_k=5`)
- Custom re-ranking using keyword overlap
- Sentence-level answer extraction
- Source snippet generation

---

### 🧠 5. Custom Re-Ranking Algorithm

- Scores retrieved chunks using word overlap with query
- Selects the most relevant chunk instead of relying only on vector similarity

---

### ✂️ 6. Sentence-Level Answer Extraction

- Splits selected chunk into sentences
- Chooses most relevant sentence as final answer

---

### ⚡ 7. Caching System

- Implemented in-memory cache using dictionary
- Stores query results with timestamp
- TTL (Time-To-Live): 5 minutes

---

### 🔁 8. Fallback & Error Handling

- Returns `"I don't know"` when:
  - No relevant context found
  - Low-quality retrieval
- Graceful error handling for runtime failures

---

### 🤖 9. Telegram Bot Integration

Implemented in `main.py`:

- `/start` command → welcome message
- `/help` command → usage guide
- `/ask` command → structured query input
- Direct message handling (no command required)
- Clean formatted response (Answer + Source)

---

### 🎯 10. Response Formatting

- Structured output:
  - 📌 Answer
  - 📄 Source snippet
- Improves readability in chat interface

---

## 🏆 Summary of Implementation

This project goes beyond a basic RAG setup by adding:

- Custom retrieval optimization
- Answer extraction logic
- Caching layer
- Smart index management
- Real-world bot interface

These enhancements make the system **more reliable, efficient, and production-aware**.