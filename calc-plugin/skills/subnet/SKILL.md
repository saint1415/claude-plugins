---
name: subnet
description: IP subnet calculator - CIDR notation, network/broadcast addresses, available hosts.
---

# Subnet Calculator Skill

Network address calculations.

## Steps

1. **Parse CIDR Input**: Extract network address and prefix length

2. **Calculate Network Details**:
   - Network Address: First address in range
   - Broadcast Address: Last address in range
   - Subnet Mask: Convert prefix to dotted decimal
   - Usable Hosts: 2^(32-prefix) - 2
   - First/Last Usable: Network+1 to Broadcast-1

3. **Output Format**:
   ```
   ## Subnet: 192.168.1.0/24

   | Property | Value |
   |----------|-------|
   | Network Address | 192.168.1.0 |
   | Broadcast Address | 192.168.1.255 |
   | Subnet Mask | 255.255.255.0 |
   | Wildcard Mask | 0.0.0.255 |
   | Total Addresses | 256 |
   | Usable Hosts | 254 |
   | First Usable | 192.168.1.1 |
   | Last Usable | 192.168.1.254 |
   | CIDR Notation | /24 |

   ### Binary Representation
   - Network: 11000000.10101000.00000001.00000000
   - Mask:    11111111.11111111.11111111.00000000
   ```

## Common CIDR Reference
| CIDR | Hosts | Subnet Mask |
|------|-------|-------------|
| /24 | 254 | 255.255.255.0 |
| /25 | 126 | 255.255.255.128 |
| /26 | 62 | 255.255.255.192 |
| /27 | 30 | 255.255.255.224 |
| /28 | 14 | 255.255.255.240 |

## Example Usage
- `/calc:subnet 192.168.1.0/24`
- `/calc:subnet 10.0.0.0/16 --split /24`
- `/calc:subnet --hosts 500`
