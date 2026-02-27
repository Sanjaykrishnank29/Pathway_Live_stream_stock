import unittest
from src.backend.utils import create_esg_prompt


class TestUtils(unittest.TestCase):
    def test_create_esg_prompt(self):
        company = "Test Corp"
        score = 85
        prompt = create_esg_prompt(company, score)
        self.assertIsInstance(prompt, list)
        self.assertEqual(len(prompt), 1)
        self.assertIn(company, prompt[0]["content"])
        self.assertIn(str(score), prompt[0]["content"])


if __name__ == "__main__":
    unittest.main()
