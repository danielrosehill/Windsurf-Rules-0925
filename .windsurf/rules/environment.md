---
trigger: always_on
---

# Environment & System Configuration

## Basic Information
- **User**: Daniel Rosehill ([danielrosehill.com](https://danielrosehill.com))
- **Location**: Jerusalem, Israel
- **Environment**: Kubuntu 25.04 desktop
- **Privileges**: Full sudo access. Assume permission to invoke.

## System Specifications

### Core System
- **OS**: Kubuntu (Ubuntu + KDE Plasma), Latest release
- **Filesystem**: BTRFS + RAID5, 5 physical drives in array

### Hardware

#### CPU
- **Model**: Intel Core i7-12700F
- **Cores**: 12 cores / 20 threads

#### GPU
- **Model**: AMD Radeon RX 7700 XT (gfx1101 / Navi 32)
- **Driver**: `amdgpu`
- **ROCM**: Installed (important for LLM development and local AI tasks)

#### Memory
- **RAM**: 64 GB Installed

#### Network
- **Interface**: `enp6s0`
- **LAN IP**: 10.0.0.6

#### Motherboard
- **Model**: MSI PRO B760M-A WIFI (MS-7D99)

## Development Environment

### SDK Location
SDKs are available here: `/home/daniel/development/sdks`

### MCP Configuration
- **Configuration Location**: `/home/daniel/.codeium/windsurf/mcp_config.json`
- **Development Location**: Create MCP servers at `~/mcp`