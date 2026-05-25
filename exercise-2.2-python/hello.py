#!/usr/bin/env python3
"""
First Python script — system info reporter.
"""

import os
import socket
from datetime import datetime

# Sakupi info
hostname = socket.gethostname()
username = os.getlogin()
now = datetime.now()

# Lista servera koje monitoriramo
servers = [
    {"name": "web01", "ip": "10.0.1.5", "role": "frontend"},
    {"name": "db01", "ip": "10.0.2.10", "role": "database"},
    {"name": "cache01", "ip": "10.0.2.20", "role": "redis"},
]

# Output
print("=" * 50)
print(f"  System Info Report")
print(f"  Generated: {now:%Y-%m-%d %H:%M:%S}")
print("=" * 50)
print(f"User:     {username}")
print(f"Hostname: {hostname}")
print()
print("Monitored servers:")

for i, server in enumerate(servers, 1):
    print(f"  {i}. {server['name']:<10} {server['ip']:<15} ({server['role']})")

print("=" * 50)
