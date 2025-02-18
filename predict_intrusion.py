# predict_intrusion.py
import joblib
import pandas as pd
from extract_features import extract_features
from scapy.all import sniff

# Load the saved model
model = joblib.load('intrusion_detection_model.pkl')
print("Model loaded successfully.")

# Make predictions on extracted features
def predict_attack(features_df):
    prediction = model.predict(features_df)
    if prediction[0] == 1:
        print("Alert! Possible Attack Detected.")
    else:
        print("Normal Activity.")

# Capture live packets and make predictions
def monitor_packet(packet):
    features_df = extract_features(packet)
    predict_attack(features_df)

sniff(prn=monitor_packet, count=10)
