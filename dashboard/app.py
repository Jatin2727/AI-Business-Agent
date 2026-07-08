import streamlit as st

from components.sidebar import sidebar

from pages.home import show as home_page
from pages.upload import show as upload_page
from pages.dashboard import show as dashboard_page
from pages.ai_chat import show as ai_chat_page
from pages.ml import show as ml_page
from pages.reports import show as reports_page
from pages.settings import show as settings_page

st.set_page_config(
    page_title="AI Business Intelligence Agent",
    page_icon="🤖",
    layout="wide"
)

menu = sidebar()

if menu == "🏠 Home":
    home_page()

elif menu == "📁 Upload Data":
    upload_page()

elif menu == "📊 Dashboard":
    dashboard_page()

elif menu == "🤖 AI Chat":
    ai_chat_page()

elif menu == "📈 Machine Learning":
    ml_page()

elif menu == "📄 Reports":
    reports_page()

elif menu == "⚙ Settings":
    settings_page()