import streamlit as st

def show():

    st.title("📁 Upload Data")

    uploaded_file = st.file_uploader(
        "Upload CSV, Excel or PDF",
        type=["csv", "xlsx", "pdf"]
    )

    if uploaded_file:

        st.success("File Uploaded Successfully")

        st.write("Filename:", uploaded_file.name)

        st.write("Size:", uploaded_file.size, "bytes")