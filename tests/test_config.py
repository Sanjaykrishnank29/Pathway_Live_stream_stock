import unittest
from src.config import Config


class TestConfig(unittest.TestCase):
    def test_config_values(self):
        self.assertEqual(Config.PAGE_TITLE, "Green Bharat Live AI")
        self.assertEqual(Config.PAGE_ICON, "🌱")
        self.assertTrue(Config.OUTPUT_PATH.endswith(".csv"))


if __name__ == "__main__":
    unittest.main()
