import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Central configuration for the Green Bharat AI application."""

    # API Keys
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

    # Pathway Options
    OUTPUT_PATH = "data/ui_output.csv"
    INPUT_RATE = 0.3

    # Streamlit Options
    REFRESH_RATE_SEC = 2
    HISTORY_ROWS = 8
    PAGE_TITLE = "Green Bharat Live AI"
    PAGE_ICON = "🌱"

    # LLM Options
    LLM_MODEL = "groq/llama-3.1-8b-instant"
