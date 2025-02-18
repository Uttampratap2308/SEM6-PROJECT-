# extract_features.py
import pandas as pd
from scapy.all import IP, TCP, UDP

# Extract features from a packet
def extract_features(packet):
    features = {
        'protocol_type': packet.proto if IP in packet else 0,
        'service': packet.sport if TCP in packet or UDP in packet else 0,
        'flag': packet.flags if TCP in packet else 0
    }
    return pd.DataFrame([features])

# Test with a captured packet
from scapy.all import sniff

def monitor_packet(packet):
    features_df = extract_features(packet)
    print(features_df)

sniff(prn=monitor_packet, count=5)




#how to run :