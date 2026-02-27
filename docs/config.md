# Configuration Documentation

The project uses a centralized configuration system to maintain clean code and ensure consistency across the backend and frontend.

## `src/config.py`

All application constants are defined in the `Config` class:

| Variable | Description | Default / Source |
| :--- | :--- | :--- |
| `GROQ_API_KEY` | API Key for Llama 3 LLM access | Environment Variable |
| `OUTPUT_PATH` | Path to the intermediary CSV sink | `data/ui_output.csv` |
| `INPUT_RATE` | Rate of simulated data ingestion | `0.3` |
| `REFRESH_RATE_SEC`| UI polling interval in seconds | `2` |
| `HISTORY_ROWS` | Number of rows displayed in the UI table | `8` |
| `PAGE_TITLE` | Browser tab title for Streamlit | "Green Bharat Live AI" |
| `PAGE_ICON` | Favicon used in the dashboard | "🌱" |
| `LLM_MODEL` | The specific model identifier from Groq | `groq/llama-3.1-8b-instant` |

## Environment Setup
Environment-specific secrets (like API keys) should be stored in a `.env` file in the root directory. This file is automatically loaded by the `Config` class using `python-dotenv`.
