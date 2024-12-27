import streamlit as st
import pandas as pd

def real_time_alerts():
    st.subheader("Real-Time Alerts")
    st.write("""
    Stay informed with real-time alerts about high-risk claims, tampered documents, or suspicious activities.
    """)

    # Sample alerts
    alerts = pd.DataFrame({
        "Time": ["10:15 AM", "11:30 AM", "2:45 PM"],
        "Alert": ["High-risk claim detected", "Tampered document uploaded", "Suspicious customer-agent activity"]
    })
    st.table(alerts)

    # Actions
    if st.button("Acknowledge All Alerts"):
        st.success("All alerts acknowledged!")
import streamlit as st
import pandas as pd

def real_time_alerts():
    st.subheader("Real-Time Alerts")
    st.write("""
    Stay informed with real-time alerts about high-risk claims, tampered documents, or suspicious activities.
    """)

    # Sample alerts
    alerts = pd.DataFrame({
        "Time": ["10:15 AM", "11:30 AM", "2:45 PM"],
        "Alert": ["High-risk claim detected", "Tampered document uploaded", "Suspicious customer-agent activity"]
    })
    st.table(alerts)

    # Actions
    if st.button("Acknowledge All Alerts"):
        st.success("All alerts acknowledged!")
import streamlit as st
import pandas as pd

def real_time_alerts():
    st.subheader("Real-Time Alerts")
    st.write("""
    Stay informed with real-time alerts about high-risk claims, tampered documents, or suspicious activities.
    """)

    # Sample alerts
    alerts = pd.DataFrame({
        "Time": ["10:15 AM", "11:30 AM", "2:45 PM"],
        "Alert": ["High-risk claim detected", "Tampered document uploaded", "Suspicious customer-agent activity"]
    })
    st.table(alerts)

    # Actions
    if st.button("Acknowledge All Alerts"):
        st.success("All alerts acknowledged!")
