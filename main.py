# main.py
from scapy.all import sniff
from extract_features import extract_features
from predict_intrusion import predict_attack
from send_alert import send_alert

# Integrate all steps for real-time detection and alerting
def monitor_packet(packet):
    features_df = extract_features(packet)
    if not features_df.empty:
        prediction = predict_attack(features_df)
        if prediction[0] == 1:  # Attack Detected
            send_alert()

# Start live packet sniffing
sniff(prn=monitor_packet, count=0)



#how to run : sudo python3 main.py
