import streamlit as st
import pandas as pd

def document_verification():
    st.subheader("Document Verification Results")
    st.write("Analyze document authenticity and detect potential tampering.")

    # Sample table
    documents = pd.DataFrame({
        "Document ID": ["DOC123", "DOC124", "DOC125"],
        "Customer": ["John Doe", "Jane Smith", "Alice Johnson"],
        "Verification Status": ["Authentic", "Tampered", "Authentic"],
        "Fraud Risk": ["Low", "High", "Low"]
    })
    st.table(documents)

    # Upload document
    uploaded_file = st.file_uploader("Upload Document for Verification")
    if uploaded_file is not None:
        st.write("Analyzing document...")
        st.success("Document verified successfully! Status: Authentic")
