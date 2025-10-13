# tests/test_agent.py
import unittest
from unittest.mock import patch

class TestTriageAgent(unittest.TestCase):
    def test_classification(self):
        with patch("agents.triage_agent.get_model") as mock_get_model:
            mock_model = type("MockModel", (), {"predict": lambda self, x: ["Network Issue"]})()
            mock_get_model.return_value = mock_model

            from agents.triage_agent import classify_ticket
            result = classify_ticket("User cannot access shared drive")
            self.assertEqual(result, "Network Issue")

if __name__ == "__main__":
    unittest.main()