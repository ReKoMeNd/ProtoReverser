from scapy.all import *
import re

# Read the pcap file
packets = rdpcap("UDPProtocol.pcap")

#Every UdpPacketWithPayload is an object with Source/Dst IP, Source/Dst Port, Payload and variable to know whether this is a client-to-server packet or vice-versa
class UdpPacketWithPayload:
                def __init__(self, srcip, dstip, srcport, dstport, payload, clientToServer):
                    self.srcip = srcip 
                    self.dstip = dstip 
                    self.srcport = srcport 
                    self.dstport = dstport 
                    self.payload = payload 
                    self.clientToServer = clientToServer 

i = 0
packettt = []

# Extract UDP payload from each packet
for pkt in packets:
    if UDP in pkt:
        udp = pkt[UDP]
        if udp.payload:

            
            packettt.append(UdpPacketWithPayload(pkt[IP].src, pkt[IP].dst, udp.sport, udp.dport, udp.payload.original.hex(), 1))
            print(f"Source IP: {packettt[i].srcip}\tSource Port: {packettt[i].srcport}\tDestination IP: {packettt[i].dstip}\tDestination Port: {packettt[i].dstport}\nPayload: {packettt[i].payload}\nIsClient?: {packettt[i].clientToServer}")
            i = i + 1
            print("YES")

            
            # Extract source and destination IP addresses and port numbers
            #src_ip = pkt[IP].src
            #dst_ip = pkt[IP].dst
            #src_port = udp.sport
            #dst_port = udp.dport

            # Extract UDP payload as a raw hexadecimal string
            #payload_hex = udp.payload.original.hex()

print("-------------------------------End------------------------------------")
for ppp in packettt:
      print(ppp.payload)
