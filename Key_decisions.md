## 🧠 Key Engineering Decisions

This project is designed not just as a working RAG system, but as a **thoughtful engineering solution** with clear trade-offs and priorities.

---

### ⚡ 1. Local Embeddings for Zero Cost

- Used `sentence-transformers/all-MiniLM-L6-v2`
- Runs completely locally (no API calls)

**Why:**
- Eliminates API costs → scalable for production
- Faster inference (no network latency)
- Works offline

---

### 🚀 2. Extractive Answering (No Hallucination)

- Avoided full LLM generation for answers
- Answers are extracted directly from retrieved context

**Why:**
- Ensures 100% grounded responses
- Eliminates hallucination risk
- Improves reliability for factual Q&A systems

---

### 🔍 3. Custom Re-Ranking Logic

- Implemented keyword-overlap based scoring
- Selects the most relevant chunk from retrieved results

**Why:**
- Improves precision beyond default vector similarity
- Handles noisy or overlapping document chunks
- Lightweight alternative to expensive rerankers

---

### 🧾 4. Sentence-Level Answer Extraction

- Instead of returning full chunks, selects the most relevant sentence

**Why:**
- Improves answer clarity and conciseness
- Reduces irrelevant information
- Enhances user experience in chat interface

---

### ⚡ 5. In-Memory Caching (TTL-Based)

- Stores recent query responses with a 5-minute TTL

**Why:**
- Reduces repeated computation
- Improves response latency
- Useful for frequently asked questions

---

### 🔄 6. Automatic Index Rebuild

- Detects changes in document files
- Rebuilds vector index when needed

**Why:**
- Keeps system always in sync with data
- Eliminates manual re-indexing errors
- Improves maintainability

---

### 🤖 7. Telegram Bot Interface

- Integrated RAG system with Telegram

**Why:**
- Real-world usability (not just a script)
- Demonstrates end-to-end system design
- Makes the project interactive and demo-friendly

---

### ⚙️ 8. Lightweight & Resource-Efficient Design

- Avoided heavy LLM dependency for core functionality

**Why:**
- Works on low-memory systems
- Avoids GPU dependency
- Ensures broader accessibility

---

### 🧠 9. Strong Focus on Reliability Over Complexity

- Prioritized correctness over fancy generation

**Why:**
- In production systems, **wrong answers are worse than no answers**
- Designed to return `"I don't know"` instead of guessing
- Aligns with real-world AI system expectations

---

## 🏆 Summary

This system is designed with:

- 💸 **Zero API cost**
- ⚡ **Low latency (fast local execution)**
- 🎯 **High accuracy (grounded answers)**
- 🔒 **No hallucination risk**

