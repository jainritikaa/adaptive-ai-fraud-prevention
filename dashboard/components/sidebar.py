import streamlit as st
from PIL import Image

def sidebar():

    # Use the updated parameter
    logo_path = "dashboard/static/images/logo.png"
    logo = Image.open(logo_path)
    st.sidebar.image(logo, use_container_width=True)

    app_mode = st.sidebar.radio(
        "Navigation",
        ["Overview", "Fraud Trends", "Document Verification", "Network Analysis", "Real-Time Alerts"]
    )

    st.sidebar.markdown(
        """
        ### Fraud Prevention Dashboard
        This dashboard enables fraud analysts to monitor and detect insurance fraud using advanced AI techniques. Navigate through the modules to explore its features.
        """
    )
    return app_mode
