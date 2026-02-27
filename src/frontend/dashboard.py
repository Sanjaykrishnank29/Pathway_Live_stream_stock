import os
import time
import pandas as pd
import streamlit as st

from src.config import Config
from src.frontend.components import (
    render_premium_styles,
    render_sidebar,
    render_header,
    render_metric_card,
)


class SustainabilityDashboard:
    """
    Modular Streamlit application for real-time ESG intelligence.
    """

    def __init__(self):
        self._setup_layout()

    def _setup_layout(self) -> None:
        """Initialize page layout and architectural styles."""
        st.set_page_config(
            page_title=Config.PAGE_TITLE,
            layout="wide",
            page_icon=Config.PAGE_ICON,
        )
        render_premium_styles()

    def render(self) -> None:
        """Main rendering orchestration for the dashboard."""
        status_placeholder = render_sidebar()
        render_header()

        # Layout allocation
        col_metrics, col_table = st.columns([1, 2])

        with col_metrics:
            metric_container = st.empty()

        with col_table:
            st.subheader("📡 Live Analytics Stream")
            table_placeholder = st.empty()

        st.write("---")
        insight_container = st.container()

        # Operational polling loop
        while True:
            self._fetch_and_update(
                status_placeholder,
                metric_container,
                table_placeholder,
                insight_container,
            )
            time.sleep(Config.REFRESH_RATE_SEC)

    def _fetch_and_update(
        self,
        status_placeholder,
        metric_container,
        table_placeholder,
        insight_container,
    ) -> None:
        """Fetch latest stream state and update the reactive UI."""
        if not os.path.exists(Config.OUTPUT_PATH):
            status_placeholder.error("Pathway Engine: OFFLINE 🔴")
            st.warning(f"Waiting for synchronization with '{Config.OUTPUT_PATH}'...")
            return

        try:
            # Load streaming intermediary state
            df = pd.read_csv(Config.OUTPUT_PATH)

            if not df.empty:
                latest = df.iloc[-1]
                status_placeholder.success("Pathway Engine: ACTIVE 🟢")

                # Update primary intelligence card
                with metric_container.container():
                    render_metric_card(
                        latest["company"],
                        latest["esg_score"],
                        latest.get("risk_level", "Analyzing..."),
                    )

                # Update historical analytics stream
                table_placeholder.dataframe(
                    df.tail(Config.HISTORY_ROWS),
                    use_container_width=True,
                    hide_index=True,
                )

                # Update advanced AI insights
                with insight_container:
                    st.subheader(f"🤖 AI Reasoning: {latest['company']}")
                    st.info(latest["ai_analysis"])

        except Exception:
            status_placeholder.warning("Pathway Engine: SYNCING... 🟡")


if __name__ == "__main__":
    app = SustainabilityDashboard()
    app.render()
