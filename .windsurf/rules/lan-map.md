---
trigger: always_on
---

# Local Area Network / LAN

This describes the 

## Network Context
- **LAN Network**: 10.0.0.0/24
- **SSH**: Key-based access to LAN devices is preconfigured
- **Development Location**: Home (on the LAN)
- **External Networks**: Will inform when using Cloudflare IPs and Tailscale endpoints

## LAN IP Map

Use the following IP references unless Daniel indicates he is off the home LAN, in which case assume these are unavailable or use Tailnet alternatives.

| IP Address | Hostname         | Description                         |
| ---------- | ---------------- | ----------------------------------- |
| 10.0.0.1   | `opnsense`       | Gateway / Router                    |
| 10.0.0.2   | `proxmox-host`   | Proxmox (Ubuntu VM & HA containers) |
| 10.0.0.3   | `home-assistant` | Home Assistant OS                   |
| 10.0.0.4   | `home-server`    | Ubuntu VM (core services host)      |
| 10.0.0.50  | `synology`       | Synology NAS (DS920+)               |

## Network Context
- **Primary Development**: Home LAN (10.0.0.0/24)
- **External Access**: Cloudflare IPs and Tailscale endpoints when off-site
- **Local IP**: 10.0.0.6 (`enp6s0` interface)