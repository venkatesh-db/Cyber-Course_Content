import unittest
from soar_integration import execute_playbook

class TestSOARIntegration(unittest.TestCase):

    def test_block_ip(self):
        result = execute_playbook("block_ip", ip_address="192.168.1.1")
        self.assertEqual(result["status"], "success")
        self.assertIn("192.168.1.1", result["message"])

    def test_suspend_account(self):
        result = execute_playbook("suspend_account", account_id="user123")
        self.assertEqual(result["status"], "success")
        self.assertIn("user123", result["message"])

    def test_notify_fraud_team(self):
        result = execute_playbook("notify_fraud_team", incident_id="INC12345", details="Suspicious login attempts detected.")
        self.assertEqual(result["status"], "success")
        self.assertIn("INC12345", result["message"])
        self.assertIn("Suspicious login attempts detected.", result["message"])

if __name__ == "__main__":
    unittest.main()