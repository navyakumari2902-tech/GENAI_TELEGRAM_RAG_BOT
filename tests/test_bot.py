import unittest
from rag.rag_pipeline import query_rag

class TestBotLogic(unittest.TestCase):

    def test_response_format(self):
        result = query_rag("What is RAG?")

        answer = result.get("answer", "")
        source = result.get("source", "")

        reply = f"""
📌 Answer:
{answer}

📄 Source:
{source}
"""

        self.assertIn("Answer", reply)
        self.assertIn("Source", reply)

    def test_safe_response(self):
        result = query_rag("")

        self.assertEqual(result["answer"], "Please provide a valid query.")


if __name__ == "__main__":
    unittest.main()