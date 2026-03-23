import unittest
from rag.rag_pipeline import query_rag

class TestIntegration(unittest.TestCase):

    def test_end_to_end_query(self):
        result = query_rag("What is RAG?")

        self.assertIsInstance(result, dict)
        self.assertIn("answer", result)
        self.assertIn("source", result)
        self.assertTrue(len(result["answer"]) > 0)

    def test_empty_query(self):
        result = query_rag("")
        self.assertEqual(result["answer"], "Please provide a valid query.")

    def test_unknown_query(self):
        result = query_rag("asdasdasd random nonsense")

        self.assertIsInstance(result["answer"], str)
        # Should not crash
        self.assertTrue(len(result["answer"]) > 0)


if __name__ == "__main__":
    unittest.main()