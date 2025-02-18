# dashboard.py

# Importing required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scapy.all import sniff
from extract_features import extract_features  # Custom module to extract features
from predict_intrusion import predict_attack  # Custom module to make predictions

# ---------------------- Dashboard Layout ----------------------
# Setting the title and layout for the dashboard
st.title("Network Intrusion Detection System")
st.subheader("Real-Time Network Traffic Analysis")

# Placeholders for live packet monitor and alerts
packet_placeholder = st.empty()  # Placeholder for displaying live packets
alert_placeholder = st.empty()   # Placeholder for displaying alerts

# List to store historical logs
historical_log = []

# ---------------------- Real-Time Packet Monitoring ----------------------
# Function to capture and monitor live network packets
def monitor_packet(packet):
    # Extracting features from the captured packet
    features_df = extract_features(packet)
    if not features_df.empty:
        # Making predictions using the loaded model
        prediction = predict_attack(features_df)
        
        # Organizing packet details for display
        packet_details = {
            'Protocol': features_df['protocol_type'].values[0],
            'Service': features_df['service'].values[0],
            'Flag': features_df['flag'].values[0],
            'Prediction': 'Attack' if prediction[0] == 1 else 'Normal'
        }
        
        # Storing packet details in historical logs
        historical_log.append(packet_details)
        
        # Displaying live packet details
        packet_placeholder.write(pd.DataFrame([packet_details]))
        
        # Displaying real-time alerts
        if prediction[0] == 1:
            alert_placeholder.error("⚠️ Alert! Possible Attack Detected.")
        else:
            alert_placeholder.success("✅ Normal Activity")

# Start live packet sniffing
sniff(prn=monitor_packet, count=0)

# ---------------------- Historical Logs and Analysis ----------------------
# Displaying historical logs and traffic patterns
st.subheader("Historical Traffic Analysis")

if historical_log:
    # Creating a DataFrame from historical logs
    df = pd.DataFrame(historical_log)
    
    # Displaying the historical log data table
    st.dataframe(df)
    
    # ---------------------- Traffic Distribution Pie Chart ----------------------
    # Visualizing distribution of normal and attack packets
    st.subheader("Traffic Distribution")
    fig, ax = plt.subplots()
    df['Prediction'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_ylabel('')
    st.pyplot(fig)
    
    # ---------------------- Traffic Trends Over Time ----------------------
    # Displaying the trend of network activity over time
    st.subheader("Traffic Trends Over Time")
    st.line_chart(df['Prediction'].value_counts())
