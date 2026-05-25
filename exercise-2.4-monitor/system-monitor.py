#!/usr/bin/env python3
"""
system-monitor.py
Logs CPU, RAM, disk usage to a CSV file every N seconds.
Alarms when CPU goes over threshold.
"""

import csv
import os
import sys
import time
import signal
import psutil
from datetime import datetime
from pathlib import Path

# === CONFIG ===
INTERVAL = 60                # sekundi između mjerenja
CPU_THRESHOLD = 80           # procenat — iznad ovog se alarmira
LOG_FILE = Path.home() / "cloud-journey" / "exercise-2.4-monitor" / "metrics.csv"
CSV_HEADERS = ["timestamp", "cpu_percent", "mem_percent", "disk_percent", "load_1min"]

# === SETUP ===
def init_csv():
    """Kreiraj CSV sa header-om ako ne postoji."""
    if not LOG_FILE.exists():
        with open(LOG_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)
        print(f"[{datetime.now():%H:%M:%S}] Created log file: {LOG_FILE}")


def collect_metrics():
    """Sakupi trenutne sistemske metrike."""
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    load = os.getloadavg()[0]
    return cpu, mem, disk, load


def log_metrics(cpu, mem, disk, load):
    """Upiši red u CSV."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, cpu, mem, disk, load])


def check_alarm(cpu):
    """Print upozorenje ako je CPU previsok."""
    if cpu > CPU_THRESHOLD:
        print(f"[{datetime.now():%H:%M:%S}] *** ALARM *** CPU = {cpu}% (>{CPU_THRESHOLD}%)")


def handle_sigint(signum, frame):
    """Graceful shutdown na Ctrl+C."""
    print(f"\n[{datetime.now():%H:%M:%S}] Stopping monitor. Log saved to {LOG_FILE}")
    sys.exit(0)


# === MAIN LOOP ===
def main():
    signal.signal(signal.SIGINT, handle_sigint)
    init_csv()
    print(f"[{datetime.now():%H:%M:%S}] Monitor started — sampling every {INTERVAL}s")
    print(f"[{datetime.now():%H:%M:%S}] Alarm threshold: CPU > {CPU_THRESHOLD}%")
    print(f"[{datetime.now():%H:%M:%S}] Logging to: {LOG_FILE}")
    print("Press Ctrl+C to stop.\n")

    while True:
        try:
            cpu, mem, disk, load = collect_metrics()
            log_metrics(cpu, mem, disk, load)
            check_alarm(cpu)
            print(f"[{datetime.now():%H:%M:%S}] CPU={cpu:>5.1f}%  MEM={mem:>5.1f}%  DISK={disk:>5.1f}%  LOAD={load:.2f}")
            time.sleep(INTERVAL)
        except Exception as e:
            print(f"[{datetime.now():%H:%M:%S}] ERROR: {e}", file=sys.stderr)
            time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
