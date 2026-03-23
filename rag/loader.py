from llama_index.core import SimpleDirectoryReader

def load_documents(path="data"):
    documents = SimpleDirectoryReader(path).load_data()
    return documents
