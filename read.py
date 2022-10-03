import socket
import scapy.all as scapy
from scapy.all import IterSocket

s = IterSocket()
conn, addr = s.accept()
with conn:
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(999999999)
        if not data:
            break   

print(data)