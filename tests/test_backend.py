import unittest
from unittest.mock import patch
from src.backend.pipeline import SustainabilityPipeline, GreenAssetSchema


class TestBackend(unittest.TestCase):
    def test_pipeline_init(self):
        pipeline = SustainabilityPipeline(output_path="test_output.csv")
        self.assertEqual(pipeline.output_path, "test_output.csv")
        self.assertIsNotNone(pipeline.model)

    def test_schema_fields(self):
        schema = GreenAssetSchema(company="Test Corp", esg_score=85)
        self.assertEqual(schema.company, "Test Corp")
        self.assertEqual(schema.esg_score, 85)

    @patch("pathway.demo.generate_custom_stream")
    def test_get_data_stream(self, mock_stream):
        pipeline = SustainabilityPipeline()
        pipeline._get_data_stream()
        mock_stream.assert_called_once()


if __name__ == "__main__":
    unittest.main()
