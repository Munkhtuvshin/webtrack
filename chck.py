from scapy.all import *

# packets = sniff(iface="lo", monitor=True, prn=lambda x:print(x))
# sniff(iface="lo", prn=lambda x: x.show() )

# sniff(session=TCPSession, prn=lambda x: x.summary(), store=False)

# pkts = sniff(iface="lo",prn=lambda x: x.summary(), count=74, filter="tcp and ( port 8020 or port 110 )")

# wrpcap("ss.pcap",pkts)

pkts = rdpcap("hell.pcap")

