import unittest
from src.backend.analytics import classify_esg_risk, get_trend_indicator


class TestAnalytics(unittest.TestCase):
    def test_classify_esg_risk(self):
        self.assertEqual(classify_esg_risk(95), "Leader (AAA)")
        self.assertEqual(classify_esg_risk(80), "Strong (AA)")
        self.assertEqual(classify_esg_risk(65), "Average (A)")
        self.assertEqual(classify_esg_risk(40), "Under Watch (B)")

    def test_get_trend_indicator(self):
        self.assertEqual(get_trend_indicator(80, 75), "Improving 📈")
        self.assertEqual(get_trend_indicator(75, 80), "Declining 📉")
        self.assertEqual(get_trend_indicator(75, 75), "Stable ➡️")
        self.assertEqual(get_trend_indicator(80, None), "Stable")


if __name__ == "__main__":
    unittest.main()
