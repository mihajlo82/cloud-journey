# Exercise 2.4 — System Monitor

A Python daemon that samples system metrics every 60 seconds and logs to CSV.
Inspired by AWS CloudWatch agent.

## Features

- CPU, memory, disk, and load monitoring
- Configurable sampling interval and alarm threshold
- CSV output (importable to Excel, Grafana, etc.)
- Graceful shutdown on Ctrl+C
- Robust error handling — keeps running through transient errors

## Stack

- Python 3.10
- `psutil` (system metrics)
- Standard library (`csv`, `signal`, `pathlib`)

## Run

```bash
python3 system-monitor.py
```

Output goes to `metrics.csv` in the same directory.

## Configuration

Edit constants at the top of the script:

| Constant | Default | Description |
|----------|---------|-------------|
| `INTERVAL` | 60 | Seconds between samples |
| `CPU_THRESHOLD` | 80 | % CPU above which alarm fires |

## Test the alarm

```bash
stress --cpu 2 --timeout 30
```

Watch the monitor print `*** ALARM ***` lines.

## Concepts learned

- `psutil` for cross-platform system metrics
- CSV writing with the `csv` module
- Signal handling (`signal.SIGINT`) for graceful shutdown
- `pathlib.Path` (modern path manipulation)
- Infinite loops with exception isolation

###################################################

# Cloud Journey

My path to becoming an AWS Cloud Engineer. Practical exercises, mini-projects, and notes.

## Phases

- **Phase 1:** Linux & Networking — *complete*
  - Exercise 1.4: [nginx web server setup](./exercise-1.4-nginx/)
- **Phase 2:** Bash, Python, Git — *complete*
  - Exercise 2.2: [Python API client](./exercise-2.2-python/)
  - Exercise 2.4: [System monitor (capstone)](./exercise-2.4-monitor/)
- **Phase 3:** AWS Cloud Practitioner — *next*

## About

Following a 9-month roadmap from beginner to junior cloud engineer.
