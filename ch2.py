from scapy.all import *


pkts = sniff(iface="eno1",prn=lambda x: x.summary(), count=74, filter="tcp and ( port 443 or port 110 )")

