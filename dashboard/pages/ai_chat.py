import streamlit as st

def show():

    st.title("🤖 AI Chat")

    question = st.text_input("Ask a business question")

    if st.button("Submit"):

        st.success("AI response will appear here.")
    