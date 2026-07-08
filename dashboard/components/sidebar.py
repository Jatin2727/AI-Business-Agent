import streamlit as st

def sidebar():

    st.sidebar.title("Navigation")

    menu = st.sidebar.radio(
        "Choose a Page",
        [
            "🏠 Home",
            "📁 Upload Data",
            "📊 Dashboard",
            "🤖 AI Chat",
            "📈 Machine Learning",
            "📄 Reports",
            "⚙ Settings"
        ]
    )

    return menu