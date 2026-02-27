import logging
import os

import pathway as pw
from pathway.xpacks.llm.llms import LiteLLMChat

from src.config import Config
from src.backend.streaming import get_market_data_stream
from src.backend.utils import create_esg_prompt
from src.backend.analytics import classify_esg_risk

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


class SustainabilityPipeline:
    """
    Modular Pathway pipeline for computing ESG reasoning and analytics.
    """

    def __init__(self, output_path: str = Config.OUTPUT_PATH):
        self.output_path = output_path
        self._setup_model()

    def _setup_model(self) -> None:
        """Initialize the LLM reasoning model from LiteLLM."""
        if not Config.GROQ_API_KEY:
            logger.error(
                "GROQ_API_KEY missing. Pipeline will not be able to generate insights."
            )

        self.model = LiteLLMChat(
            model=Config.LLM_MODEL,
            api_key=Config.GROQ_API_KEY,
        )

    def _build_pipeline(self) -> pw.Table:
        """Construction of the reactive data processing pipeline."""
        streaming_data = get_market_data_stream()

        # Apply reasoning and analytics logic
        responses = streaming_data.select(
            pw.this.company,
            pw.this.esg_score,
            risk_level=pw.apply(classify_esg_risk, pw.this.esg_score),
            ai_analysis=self.model(
                pw.apply(create_esg_prompt, pw.this.company, pw.this.esg_score)
            ),
        )
        return responses

    def run(self) -> None:
        """Main execution loop for the Pathway streaming engine."""
        logger.info(f"🚀 Initializing Green Bharat Pipeline. Sink: {self.output_path}")

        # Ensure directory infrastructure exists
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)

        responses = self._build_pipeline()

        # Persist structured output for downstream consumption (Streamlit)
        pw.io.csv.write(responses, self.output_path)
        pw.run()


if __name__ == "__main__":
    pipeline = SustainabilityPipeline()
    pipeline.run()
