# tests/test_agent.py
import unittest
from unittest.mock import patch

class TestTriageAgent(unittest.TestCase):
    @patch("agents.triage_agent.model")
    def test_classification(self, mock_model):
        mock_model.predict.return_value = ["Network Issue"]
        from agents.triage_agent import classify_ticket
        result = classify_ticket("User cannot access shared drive")
        self.assertEqual(result, "Network Issue")

if __name__ == "__main__":
    unittest.main()