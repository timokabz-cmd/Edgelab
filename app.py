import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Edge Lab Analytics Limited",
    page_icon="⌁",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own chrome so the HTML site is the whole page
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        header[data-testid="stHeader"] {visibility: hidden; height: 0;}
        footer {visibility: hidden;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
        iframe {display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "index.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=3200, scrolling=True)
