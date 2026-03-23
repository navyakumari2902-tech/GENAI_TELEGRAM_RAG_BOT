import unittest
import time
from rag.rag_pipeline import query_rag, cache

class TestCache(unittest.TestCase):

    def test_cache_behavior(self):
        query = "What is RAG?"

        result1 = query_rag(query)
        result2 = query_rag(query)

        # Same result
        self.assertEqual(result1, result2)

        # Cache exists
        self.assertIn(query, cache)

    def test_cache_expiry(self):
        query = "What is machine learning?"

        result1 = query_rag(query)

        # simulate expiry
        cache[query] = (result1, time.time() - 400)

        result2 = query_rag(query)

        self.assertIsInstance(result2, dict)


if __name__ == "__main__":
    unittest.main()