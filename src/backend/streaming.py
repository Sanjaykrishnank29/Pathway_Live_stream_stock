import random
import pathway as pw
from src.backend.models import GreenAssetSchema
from src.config import Config


def get_market_data_stream() -> pw.Table:
    """
    Generates a simulated live market data stream for sustainability assets.
    """
    return pw.demo.generate_custom_stream(
        {
            "company": lambda _: random.choice(
                [
                    "Adani Green",
                    "Tata Power",
                    "Suzlon",
                    "Reliance New Energy",
                    "Jindal Renewables",
                    "Azure Power",
                    "Inox Wind",
                    "Hero Future Energies",
                ]
            ),
            "esg_score": lambda _: random.randint(55, 99),
        },
        schema=GreenAssetSchema,
        input_rate=Config.INPUT_RATE,
    )
