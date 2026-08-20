#!/usr/bin/env python3
import os

count = int(input(" chand adad ip mikhay scan koni ???"))

for i in range(count):
    ip = input(f" ip {i+1} ra vared kon ")
    result = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
    if result == 0:
        print(f"{ip}!!! online ast")
    else:
        print(f":{ip}!!!offline ast")

print(" scan tamam shud!!!")
