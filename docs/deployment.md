# Deployment Documentation

**Green Bharat** is designed with a "Single Source of Truth" configuration, making it highly portable and easy to deploy across various environments.

## Local Deployment

### Using `run.bat` (Windows)
Designed for quick local execution. It automatically prepares the `data/` directory and launches both services in separate windows.
```cmd
run.bat
```

### Using `Makefile` (Linux/macOS)
The Makefile orchestrates the setup and execution workflow:
- `make setup`: Prepares the virtual environment and installs dependencies.
- `make run-all`: Launches both the backend and frontend services.
- `make test`: Executes the verification suite.

## Docker Deployment
The project is fully containerized for cloud or server-based deployments.

### 1. Build the Image
```bash
docker build -t green-bharat-ai .
```

### 2. Run the Container
Ensure your `.env` file contains the required `GROQ_API_KEY`.
```bash
docker run -p 8501:8501 --env-file .env green-bharat-ai
```

The application will be accessible at `http://localhost:8501`.
