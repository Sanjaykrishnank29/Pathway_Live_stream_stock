# Backend Documentation - Pathway Data Pipeline

The backend of **Green Bharat: Live AI Market Intelligence** is powered by the [Pathway](https://pathway.com/) framework, which provides a high-performance, reactive engine for streaming data processing.

## Components

### 1. `src/backend/pipeline.py`
This is the heart of the streaming engine. It manages data ingestion, schema validation, and integration with the Groq LLM.

- **`GreenAssetSchema`**: Defines the structure of the incoming data (company name and ESG score).
- **`SustainabilityPipeline`**: The main class orchestrating the flow.
    - `_get_data_stream()`: Generates a simulated real-time stream of market data.
    - `_build_pipeline()`: Defines the logic for selecting data and applying the LLM reasoning layer using `pw.apply`.
    - `run()`: Executes the pipeline and writes the output to a persistent CSV for the frontend.

## AI Reasoning Layer
The pipeline uses `LiteLLMChat` from Pathway's LLM pack to interface with **Groq's Llama 3.1** models. The reasoning is performed asynchronously on the streaming data, providing real-time insights based on the ESG scores.

## Data Sink
Processed insights are written to `data/ui_output.csv`. This file acts as a low-latency intermediary between the backend streaming engine and the frontend dashboard.
