import streamlit as st
from components.sidebar import sidebar
from components.overview import overview
from components.fraud_trends import fraud_trends
from components.document_verification import document_verification
from components.network_analysis import network_analysis
from components.real_time_alerts import real_time_alerts

def main():
    # Set page config
    st.set_page_config(page_title="Fraud Prevention Dashboard", layout="wide")

    # Render sidebar and get the selected module
    selected_module = sidebar()

    # Application header
    st.title("Adaptive AI Fraud Prevention Dashboard")
    st.header("Monitor, Detect, and Prevent Insurance Fraud in Real-Time")

    # Render the selected module
    if selected_module == "Overview":
        overview()
    elif selected_module == "Fraud Trends":
        fraud_trends()
    elif selected_module == "Document Verification":
        document_verification()
    elif selected_module == "Network Analysis":
        network_analysis()
    elif selected_module == "Real-Time Alerts":
        real_time_alerts()

if __name__ == "__main__":
    main()
