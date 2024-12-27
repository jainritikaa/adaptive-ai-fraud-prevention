import streamlit as st
import pandas as pd
import plotly.express as px

def fraud_trends():
    st.subheader("Fraud Trends Visualization")
    st.write("""
    This section highlights trends in fraudulent and normal claims over time, helping to identify spikes or patterns in fraud attempts.
    """)

    # Sample data
    data = {
        "Date": pd.date_range(start="2024-01-01", periods=30, freq="D"),
        "Fraudulent Claims": [10, 15, 12, 8, 20, 25, 18, 15, 17, 22, 30, 28, 24, 19, 21, 23, 26, 29, 35, 33, 25, 20, 18, 17, 16, 22, 24, 28, 30, 35],
        "Normal Claims": [90, 85, 88, 92, 80, 75, 82, 85, 83, 78, 70, 72, 76, 81, 79, 77, 74, 71, 65, 67, 75, 80, 82, 83, 84, 78, 76, 72, 70, 65]
    }
    df = pd.DataFrame(data)
    fig = px.line(
        df, 
        x="Date", 
        y=["Fraudulent Claims", "Normal Claims"], 
        title="Daily Claims Trends", 
        labels={"value": "Number of Claims", "variable": "Type of Claims"}
    )
    st.plotly_chart(fig, use_container_width=True)
