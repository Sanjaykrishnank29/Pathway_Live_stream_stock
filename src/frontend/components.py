import streamlit as st
from src.config import Config


def render_premium_styles():
    """Injects custom CSS for a high-end, modern look."""
    st.markdown(
        """
        <style>
        .main { 
            background-color: #0d1117; 
            color: #c9d1d9; 
            font-family: 'Inter', sans-serif;
        }
        .stMetric { 
            background: rgba(22, 27, 34, 0.7);
            border: 1px solid rgba(48, 54, 61, 0.5); 
            padding: 25px; 
            border-radius: 16px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            backdrop-filter: blur(4px);
            -webkit-backdrop-filter: blur(4px);
        }
        .stDataFrame { 
            border: 1px solid #30363d; 
            border-radius: 12px; 
        }
        h1, h2, h3 { 
            color: #58a6ff !important; 
            font-weight: 700;
        }
        .sidebar .sidebar-content { 
            background-image: linear-gradient(#161b22, #0d1117); 
        }
        .stAlert {
            border-radius: 12px;
            border: 1px solid rgba(88, 166, 255, 0.2);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar():
    """Renders the dashboard sidebar with system metrics."""
    st.sidebar.title("📡 System Intelligence")
    status_placeholder = st.sidebar.empty()
    st.sidebar.markdown("---")

    with st.sidebar.expander("🛠️ Pipeline Details", expanded=True):
        st.info(
            "Powered by **Pathway Engine**\n\n"
            "Real-time streaming ingestion & AI reasoning active."
        )
        st.write(f"**Refresh Interval:** {Config.REFRESH_RATE_SEC}s")
        st.write(f"**Ingestion Rate:** {Config.INPUT_RATE} ops/s")

    st.sidebar.markdown("---")
    st.sidebar.caption("v1.2.0 | Green Bharat AI")

    return status_placeholder


def render_header():
    """Renders the dashboard main heading."""
    st.title(f"{Config.PAGE_ICON} Green Bharat: Live AI Market Intelligence")
    st.markdown(
        "### Reactive Sustainability & ESG Reasoning Engine\n"
        "Leveraging **Pathway** for real-time data orchestration and **Groq Llama 3** for architectural reasoning."
    )
    st.write("---")


def render_metric_card(company, score, risk_level):
    """Renders the main asset metric card."""
    with st.container():
        st.subheader("🎯 Primary Asset Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Focus Account", company)
        with col2:
            st.metric("Sustainability Score", f"{score}/100", delta=risk_level)
