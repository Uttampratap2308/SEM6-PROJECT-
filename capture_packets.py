# capture_packets.py
from scapy.all import sniff

# Function to process each packet
def monitor_packet(packet):
    packet.show()  # Display packet details

# Capture live packets
sniff(prn=monitor_packet, count=10)



#how to run : sudo python3 capture_packets.py
