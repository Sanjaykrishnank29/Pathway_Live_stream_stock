# Frontend Documentation - Streamlit Dashboard

The frontend is built using [Streamlit](https://streamlit.io/), providing a premium, interactive user interface for visualizing live sustainability insights.

## Configuration
The dashboard pulls settings from `src/config.py`, including page titles, icons, and refresh intervals.

## UI Components

### 1. `src/frontend/components.py`
A library of reusable Streamlit components:
- **`render_premium_styles()`**: Glassmorphism and dark mode injection.
- **`render_sidebar()`**: Reactive system monitoring.
- **`render_header()`**: High-contrast branding.
- **`render_metric_card()`**: Real-time asset performance visualization.

### 2. `src/frontend/dashboard.py`
The main application that orchestrates the UI components into a cohesive, sub-second reporting interface.

## Real-time Polling
The frontend implements a polling loop that reads from the intermediary `data/ui_output.csv` file. This decoupled architecture ensures the UI remains responsive even during high-throughput streaming events.

## Aesthetics
The dashboard uses custom CSS to provide a premium "Glassmorphism" look, featuring:
- Dark theme orientation.
- Rounded corners and subtle box shadows for cards.
- Custom typography and brand-consistent colors.
