# Testing Documentation

Ensuring the stability and correctness of the data pipeline is a core priority of the **Green Bharat** project.

## Test Suite Structure
The project uses the `unittest` framework (and is compatible with `pytest`) for automated verification.

```text
tests/
├── test_backend.py     # Verifies Pathway schema and pipeline initialization
└── test_config.py      # Validates centralized configuration and env loading
```

## Running Tests

### Using standard `unittest`
From the project root, run:
```bash
python -m unittest discover tests/
```

### Using `pytest` (Recommended)
`pytest` is included in the project requirements. Run:
```bash
pytest tests/
```

## Coverage
- **Backend**: Verifies that the `GreenAssetSchema` correctly handles data and that the `SustainabilityPipeline` initializes without errors.
- **Configuration**: Ensures that all critical application constants are present and that defaults are correctly applied when environment variables are missing.
