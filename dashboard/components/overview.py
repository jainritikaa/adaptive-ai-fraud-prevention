import streamlit as st
from PIL import Image

def overview():
    st.subheader("System Overview")
    st.write("""
    Welcome to the Adaptive AI Fraud Prevention Dashboard. This system provides modules to monitor and detect insurance fraud effectively:
    - **Fraud Trends Visualization**: Identify patterns in fraudulent claims over time.
    - **Document Verification Insights**: Analyze document authenticity with tamper detection.
    - **Network Analysis**: Explore fraud rings and collusion between entities.
    - **Real-Time Alerts**: Stay updated on potential fraudulent activities instantly.
    """)

    # Ensure the image file exists
    try:
        overview_image = Image.open("static/images/overview.jpg")
        st.image(overview_image, caption="Fraud Prevention System Overview", use_container_width=True)
    except FileNotFoundError:
        st.error("Overview image not found. Please ensure 'overview.jpg' is in the 'static/images/' directory.")
