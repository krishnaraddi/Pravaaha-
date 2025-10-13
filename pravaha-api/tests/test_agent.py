# tests/test_agent.py
import unittest
from agents.triage_agent import classify_ticket

class TestTriageAgent(unittest.TestCase):
    def test_classification(self):
        result = classify_ticket("User cannot access shared drive")
        self.assertIn("Network Issue", result)

if __name__ == "__main__":
    unittest.main()