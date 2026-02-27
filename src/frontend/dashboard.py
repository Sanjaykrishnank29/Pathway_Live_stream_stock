import os
import time
import pandas as pd
import streamlit as st

from src.config import Config


class SustainabilityDashboard:
    """Main dashboard application class."""

    def __init__(self):
        self._configure_page()
        self._inject_styles()

    def _configure_page(self) -> None:
        """Configure page layout and metadata."""
        st.set_page_config(
            page_title=Config.PAGE_TITLE,
            layout="wide",
            page_icon=Config.PAGE_ICON,
        )

    def _inject_styles(self) -> None:
        """Inject custom CSS for a premium look."""
        st.markdown(
            """
            <style>
            .main { background-color: #0d1117; color: #c9d1d9; }
            .stMetric { 
                background-color: #161b22; 
                border: 1px solid #30363d; 
                padding: 20px; 
                border-radius: 12px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            .stDataFrame { 
                border: 1px solid #30363d; 
                border-radius: 12px; 
            }
            h1, h2, h3 { color: #58a6ff !format; }
            .sidebar .sidebar-content { background-image: linear-gradient(#161b22,#0d1117); }
            </style>
            """,
            unsafe_allow_html=True,
        )

    def _render_sidebar(self):
        """Render the sidebar components."""
        st.sidebar.title("📡 System Monitor")
        status_placeholder = st.sidebar.empty()
        st.sidebar.markdown("---")
        st.sidebar.info(
            "Pathway Framework is acting as the Unified Ingestion & Reasoning layer. "
            "Data is processed as a continuous stream from sustainability market feeds."
        )

        st.sidebar.subheader("Configuration")
        st.sidebar.text(f"Refresh Rate: {Config.REFRESH_RATE_SEC}s")
        st.sidebar.text(f"History Size: {Config.HISTORY_ROWS} rows")

        return status_placeholder

    def _render_header(self) -> None:
        """Render the main header components."""
        st.title(f"{Config.PAGE_ICON} Green Bharat: Live AI Market Intelligence")
        st.markdown(
            "**Real-time Sustainability & ESG Analysis** | Powered by **Pathway** & **Groq Llama 3**"
        )
        st.write("---")

    def render(self) -> None:
        """Render the full dashboard loop."""
        status_placeholder = self._render_sidebar()
        self._render_header()

        col_metrics, col_table = st.columns([1, 2])

        with col_metrics:
            st.subheader("Latest Asset Update")
            metric_container = st.empty()

        with col_table:
            st.subheader("Live Analysis Stream")
            table_placeholder = st.empty()

        st.write("---")
        latest_insight_placeholder = st.container()

        # Polling loop
        while True:
            self._update_data(
                status_placeholder,
                metric_container,
                table_placeholder,
                latest_insight_placeholder,
            )
            time.sleep(Config.REFRESH_RATE_SEC)

    def _update_data(
        self,
        status_placeholder,
        metric_container,
        table_placeholder,
        latest_insight_placeholder,
    ) -> None:
        """Update the dashboard with latest data from CSV."""
        if not os.path.exists(Config.OUTPUT_PATH):
            status_placeholder.error("Pathway Engine: OFFLINE 🔴")
            st.warning(
                f"Waiting for '{Config.OUTPUT_PATH}'... Ensure backend pipeline is running."
            )
            return

        try:
            df = pd.read_csv(Config.OUTPUT_PATH)

            if not df.empty:
                latest_data = df.iloc[-1]

                status_placeholder.success("Pathway Engine: ACTIVE 🟢")

                with metric_container.container():
                    st.metric("Company Name", latest_data["company"])
                    st.metric(
                        "ESG Sustainability Score", f"{latest_data['esg_score']}/100"
                    )

                # Show tail for history
                table_placeholder.dataframe(
                    df.tail(Config.HISTORY_ROWS),
                    use_container_width=True,
                    hide_index=True,
                )

                with latest_insight_placeholder:
                    st.subheader(f"🤖 AI Insight: {latest_data['company']}")
                    st.info(latest_data["ai_analysis"])

        except Exception:
            status_placeholder.warning("Pathway Engine: SYNCING... 🟡")


if __name__ == "__main__":
    app = SustainabilityDashboard()
    app.render()


if __name__ == "__main__":
    app = SustainabilityDashboard()
    app.render()
