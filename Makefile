.PHONY: setup run-backend run-frontend run-all clean docker-build docker-run

# Variables
PYTHON = python3
STREAMLIT = streamlit
APP_NAME = green-bharat-ai

setup:
	$(PYTHON) -m venv venv
	./venv/bin/pip install -r requirements.txt

run-backend:
	$(PYTHON) src/backend/pipeline.py

run-frontend:
	$(STREAMLIT) run src/frontend/dashboard.py

run-all:
	@echo "Starting backend and frontend..."
	mkdir -p data
	touch data/ui_output.csv
	$(PYTHON) src/backend/pipeline.py & $(STREAMLIT) run src/frontend/dashboard.py

clean:
	rm -rf data/*.csv
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
	
docker-build:
	docker build -t $(APP_NAME) .

docker-run:
	docker run -p 8501:8501 --env-file .env $(APP_NAME)
