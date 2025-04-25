# README - Ansible Automated Infrastructure Deployment

## Project Overview
This project provides an automated way to deploy and configure a small-scale cybersecurity lab using Ansible. It includes VyOS router configuration, OPNsense firewall rules, and proxy server setup. The infrastructure aims to simulate a real-world enterprise network with DMZ, LAN, and administrative zones.

Structure:
```
project-ansible/
├── inventory/
│   └── hosts
├── roles/
│   ├── ip/
│   │   └── tasks/main.yml
│   ├── static/
│   │   └── tasks/main.yml
│   ├── vlan_dhcp/
│   │   └── tasks/main.yml
│   ├── opnsense/
│   │   └── tasks/main.yml
│   ├── ids/
│   │   └── tasks/main.yml
│   └── proxy/
│       └── tasks/main.yml
├── playbooks.yml
└── ansible.cfg
.secret/opn.key
```

### Technologies Used
- Ansible
- VyOS
- OPNsense
- Debian
- Squid (Web proxy)

### Roles Included
- `ip`: Interface IP address configuration (static and DHCP)
- `static`: Default route and NAT setup
- `vlan_dhcp`: VLAN interface creation with DHCP settings
- `opnsense`: Firewall rules via API
- `ids`: Enable IDS on OPNsense
- `proxy`: Installation and startup of Squid proxy

### Inventory
Defined in `inventory/hosts`, it includes:
- Proxy server
- VyOS router
- Localhost (used to configure OPNsense via API)

As well as the variables for the different groups

### Requirements
- Python 3.x
	```bash
	dnf install -y python3-paramiko
	sudo pip install httpx
	```
- Required Ansible collections:
  ```bash
  ansible-galaxy collection install ansibleguy.opnsense
  ansible-galaxy collection install vyos.vyos
  ```
- API key and secret for OPNsense with appropriate permissions

### Usage
To apply the entire configuration:
```bash
ansible-playbook playbooks.yml
```

To apply only specific roles:
```bash
ansible-playbook playbooks.yml --tags opnsense
ansible-playbook playbooks.yml --tags ids
```