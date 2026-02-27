@echo off
REM Windows runner script for Green Bharat Live AI

echo Creating data directory if it doesn't exist...
if not exist "data" mkdir data
if not exist "data\ui_output.csv" type nul > data\ui_output.csv

set PYTHONPATH=%CD%

echo Starting Backend Pipeline...
start "Pathway Backend" cmd /c "python src/backend/pipeline.py"

echo Starting Frontend Dashboard...
start "Streamlit Frontend" cmd /c "streamlit run src/frontend/dashboard.py"

echo Both services have been started in separate windows!
