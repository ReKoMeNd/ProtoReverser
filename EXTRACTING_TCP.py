from scapy.all import *
import re

# Read the pcap file
packets = rdpcap("TCPProtocol.pcap")

#Every TcpPacketWithPayload is an object with Source/Dst IP, Source/Dst Port, Payload and variable to know whether this is a client-to-server packet or vice-versa
class TcpPacketWithPayload:
                def __init__(self, srcip, dstip, srcport, dstport, payload, clientToServer):
                    self.srcip = srcip #pkt[IP].src
                    self.dstip = dstip #pkt[IP].dst
                    self.srcport = srcport #tcp.sport
                    self.dstport = dstport #tcp.dport
                    self.payload = payload #tcp.payload.original.hex()
                    self.clientToServer = clientToServer #clientToServer

i = 0
packettt = []
# Extract TCP payload from each packet
for pkt in packets:
    if TCP in pkt:
        tcp = pkt[TCP]
        if tcp.payload:
            #Chech if this packet is sent from client to server

            packettt.append(TcpPacketWithPayload(pkt[IP].src, pkt[IP].dst, tcp.sport, tcp.dport, tcp.payload.original.hex(), 1))
            
            print(f"Source IP: {packettt[i].srcip}\tSource Port: {packettt[i].srcport}\tDestination IP: {packettt[i].dstip}\tDestination Port: {packettt[i].dstport}\nPayload: {packettt[i].payload}\nIsClient?: {packettt[i].clientToServer}")
            print("YES")

            i = i + 1
            
            # Extract source and destination IP addresses and port numbers
            #src_ip = pkt[IP].src
            #dst_ip = pkt[IP].dst
            #src_port = tcp.sport
            #dst_port = tcp.dport

            # Extract TCP payload as a raw hexadecimal string
            #payload_hex = tcp.payload.original.hex()

print("-------------------------------End------------------------------------")
for ppp in packettt:
      print(ppp.payload)
            