# ProtoReverser
A new attempt of automatic reverse engineering unknown protocols (sort of).

# What is this ?
Another attempt to make Python solution for Automatic Protocol Reverse Engineering of Network Protocols (APRE).

# Core idea
Core idea is to make PRE process as easy as possible.
Proposed way:
1. Making a .pcap capture of TCP or UDP session (follow TCP or UDP flow of packet capture).
2. Parsing .pcap file and making a list of objects, where every object is an simplified model of every packet in file. Every object have: Payload, DST/SRC ip, DST/SRC port, isClient Flag (used for further inference).
3. Using various proposed ways of byte alignment for inference of unknown protocol and (in theory) making state machine model.

# What's the point ?
Other attempts are outdated, have "dependency hell" issues or other issues making them useless now.
