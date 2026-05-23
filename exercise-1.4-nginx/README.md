# Exercise 1.4 — Nginx Web Server Setup

> **Phase 1 / Mini-project** — first real web server deployed on Ubuntu, documented
> end-to-end. Part of my [AWS Cloud Engineer learning roadmap](../).

## What was built

A custom HTML landing page served via **nginx** on Ubuntu Server 22.04, running in a
VirtualBox VM with a static IP on the local network, accessible from the host machine
via HTTP.

## Architecture
[ Windows host ] ----HTTP/80----> [ Ubuntu VM 192.168.1.46 ] ----> [ nginx ]
|
serves index.html

## Stack

| Layer | Tool |
|-------|------|
| Hypervisor | VirtualBox 7 |
| OS | Ubuntu Server 22.04 LTS |
| Networking | Bridged adapter, static IP via netplan |
| Web server | nginx 1.18 |
| Firewall | UFW (`Nginx HTTP` profile) |

## Setup steps

### 1. Install nginx

```bash
sudo apt update
sudo apt install nginx -y
sudo systemctl enable --now nginx
```

### 2. Configure firewall

```bash
sudo ufw allow 'Nginx HTTP'
sudo ufw status
```

### 3. Replace default page

```bash
sudo nano /var/www/html/index.html
# paste custom HTML, save
```

### 4. Verify

From Windows browser: `http://192.168.1.46`

## Lessons learned

- **Bridged vs NAT adapter** — bridged adapter gives the VM a real IP on the LAN, allowing direct access from the host without port forwarding
- **netplan YAML is whitespace-strict** — always use spaces (not tabs) and validate with `netplan try` before committing
- **nginx doesn't need a restart** when only HTML changes — it serves files straight from disk
- **`sudo` is required for `/var/www/html/`** — owned by root, not by the regular user

## Next steps

- Add HTTPS via Let's Encrypt (after getting a public domain)
- Replace static HTML with a small Python Flask app behind nginx (reverse proxy)
- Containerize with Docker (Phase 6)

---

*Built as part of my AWS Cloud Engineer learning roadmap, May 2026.*
