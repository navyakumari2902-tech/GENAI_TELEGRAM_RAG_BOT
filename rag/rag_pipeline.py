import os
import time


from llama_index.core import (
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
    Settings
)
from llama_index.core.vector_stores import SimpleVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from .loader import load_documents

# -----------------------------
# 🔹 CONFIG
# -----------------------------
PERSIST_DIR = "storage"
DATA_DIR = "Data"
CACHE_TTL = 300  # 5 minutes

cache = {}

# -----------------------------
# 🔹 EMBEDDING MODEL
# -----------------------------
Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# 🔹 BUILD INDEX
# -----------------------------
def build_index():
    print("Building index...")

    documents = load_documents()

    vector_store = SimpleVectorStore()
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context
    )

    index.storage_context.persist(persist_dir=PERSIST_DIR)

    print("Index built and saved locally.")
    return index


# -----------------------------
# 🔹 LOAD INDEX
# -----------------------------
def load_index():
    print("Loading existing index...")

    storage_context = StorageContext.from_defaults(
        persist_dir=PERSIST_DIR
    )

    return load_index_from_storage(storage_context)


# -----------------------------
# 🔹 AUTO REBUILD CHECK
# -----------------------------
def should_rebuild():
    if not os.path.exists(PERSIST_DIR):
        return True

    data_files = [os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR)]
    storage_time = os.path.getmtime(PERSIST_DIR)

    return any(os.path.getmtime(f) > storage_time for f in data_files)


# -----------------------------
# 🔹 INIT INDEX
# -----------------------------
if should_rebuild():
    index = build_index()
else:
    index = load_index()

# Retrieval engine
query_engine = index.as_query_engine(similarity_top_k=5)

# -----------------------------
# 🔹 MAIN QUERY FUNCTION
# -----------------------------
def query_rag(query: str):

    query = query.strip()

    # 🔹 Greeting handling
    if query.lower() in ["hi", "hello", "hey"]:
        return {
            "answer": "Hi! Ask me anything from the documents 😊",
            "source": ""
        }

    # 🔹 Empty query
    if not query:
        return {
            "answer": "Please provide a valid query.",
            "source": ""
        }

    # 🔹 Cache check
    if query in cache:
        cached_result, timestamp = cache[query]
        if time.time() - timestamp < CACHE_TTL:
            print("Cache hit!")
            return cached_result

    try:
        # 🔹 Retrieve nodes
        retrieved_nodes = query_engine.retrieve(query)

        if not retrieved_nodes:
            return {
                "answer": "I don't know.",
                "source": ""
            }

        # 🔥 Extract texts
        texts = [node.node.text for node in retrieved_nodes]

        # 🔥 Re-ranking (keyword overlap)
        best_text = None
        best_score = 0

        query_words = set(query.lower().split())

        for text in texts:
            text_words = set(text.lower().split())
            score = len(query_words & text_words)

            if score > best_score:
                best_score = score
                best_text = text

        # 🔹 No good match
        if not best_text or best_score == 0:
            return {
                "answer": "I don't know.",
                "source": ""
            }

        context = best_text.strip()

# 🔥 Sentence-level answer extraction
        sentences = context.split("\n")

        best_sentence = None
        best_score = 0

        query_words = set(query.lower().split())

        for sentence in sentences:
                words = set(sentence.lower().split())
                score = len(query_words & words)

                if score > best_score:
                    best_score = score
                    best_sentence = sentence

         # fallback
        if not best_sentence:
            best_sentence = sentences[0]

        answer = best_sentence.strip()

        result = {
            "answer": answer,
            "source": context[:200]
        }

        # 🔹 Cache store
        cache[query] = (result, time.time())

        return result

    except Exception as e:
        print("Error:", str(e))
        return {
            "answer": "Something went wrong. Please try again.",
            "source": ""
        }