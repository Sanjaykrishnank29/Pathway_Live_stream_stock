# Project Structure

This document provides a comprehensive overview of every file and directory in the **Green Bharat: Live AI Market Intelligence** repository.

## Root Directory

- **`README.md`**: Main entry point for documentation, features, architecture, and quick-start guides.
- **`LICENSE`**: MIT License covering the software.
- **`Makefile`**: Task orchestration for Linux and macOS environments.
- **`run.bat`**: Direct runner script for Windows environments.
- **`Dockerfile`**: Containerization instructions for the unified application.
- **`.gitignore`**: Specifies files and directories ignored by Git (e.g., `venv`, `data/*.csv`, `__pycache__`).
- **`.env.example`**: Template for environment variables required by the app.
- **`requirements.txt`**: List of Python dependencies (Pathway, Streamlit, LiteLLM, Pytest, etc.).

## `src/` (Source Code)

- **`src/__init__.py`**: Initializer for the source package.
- **`src/config.py`**: Centralized configuration and environment variable management.

### `src/backend/`
- **`src/backend/__init__.py`**: Initializer for the backend package.
- **`src/backend/pipeline.py`**: Pathway streaming pipeline and LLM reasoning logic.

### `src/frontend/`
- **`src/frontend/__init__.py`**: Initializer for the frontend package.
- **`src/frontend/dashboard.py`**: Streamlit-based real-time dashboard.

## `docs/` (Documentation)

- **`docs/backend.md`**: Deep dive into the streaming engine and LLM integration.
- **`docs/frontend.md`**: Detailed analysis of the UI components and polling logic.
- **`docs/config.md`**: Comprehensive guide to application settings.
- **`docs/testing.md`**: Overview of the testing suite and execution steps.
- **`docs/deployment.md`**: Guide for local and containerized deployments.
- **`docs/structure.md`**: This file; an index of all repository components.

## `tests/` (Verification)

- **`tests/test_backend.py`**: Unit tests for the Pathway pipeline and schema.
- **`tests/test_config.py`**: Unit tests for the configuration system.

## `data/` (Intermediary Storage)

- **`data/ui_output.csv`**: (Generated) Intermediary sink bridging the backend and frontend.
