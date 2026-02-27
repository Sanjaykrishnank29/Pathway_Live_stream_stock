import os
import random
import logging
from typing import Any, Dict

import pathway as pw
from pathway.xpacks.llm.llms import LiteLLMChat

from src.config import Config

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


class GreenAssetSchema(pw.Schema):
    """Schema for incoming green asset data stream."""

    company: str
    esg_score: int


class SustainabilityPipeline:
    """Pathway pipeline for computing ESG reasoning."""

    def __init__(self, output_path: str = Config.OUTPUT_PATH):
        self.output_path = output_path
        self._setup_model()

    def _setup_model(self) -> None:
        """Initialize the LLM reasoning model."""
        if not Config.GROQ_API_KEY:
            logger.warning("GROQ_API_KEY not found in environment. LLM calls may fail.")

        self.model = LiteLLMChat(
            model=Config.LLM_MODEL,
            api_key=Config.GROQ_API_KEY,
        )

    def _get_data_stream(self) -> Any:
        """Create a simulated live data stream."""
        return pw.demo.generate_custom_stream(
            {
                "company": lambda _: random.choice(
                    [
                        "Adani Green",
                        "Tata Power",
                        "Suzlon",
                        "Reliance New Energy",
                        "Jindal Renewables",
                    ]
                ),
                "esg_score": lambda _: random.randint(60, 98),
            },
            schema=GreenAssetSchema,
            input_rate=Config.INPUT_RATE,
        )

    def _build_pipeline(self) -> Any:
        """Build the Pathway reasoning pipeline."""
        streaming_data = self._get_data_stream()

        # Reasoning layer setup
        def create_prompt(company: str, esg_score: int) -> list[Dict[str, str]]:
            return [
                {
                    "role": "user",
                    "content": (
                        f"As an ESG expert, analyze the sustainability efforts of {company} "
                        f"which has an ESG score of {esg_score}. Provide a concise 2-sentence insight."
                    ),
                }
            ]

        responses = streaming_data.select(
            pw.this.company,
            pw.this.esg_score,
            ai_analysis=self.model(
                pw.apply(create_prompt, pw.this.company, pw.this.esg_score)
            ),
        )
        return responses

    def run(self) -> None:
        """Execute the Pathway pipeline."""
        logger.info(f"Starting Pathway pipeline. Writing output to {self.output_path}")

        # Ensure directory exists
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)

        responses = self._build_pipeline()

        # Write to CSV for UI consumption
        pw.io.csv.write(responses, self.output_path)
        pw.run()


if __name__ == "__main__":
    pipeline = SustainabilityPipeline()
    pipeline.run()
