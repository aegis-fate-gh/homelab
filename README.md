# Homelab
This is centralized repo for everything related to my homelab

## Physical Infrastructure
What I call "Eos" is composed of 3 identical servers each containing:
- CPU: AMD Ryzen 5700X 8c 16t
- CPU Cooler: Noctua NH-D9L
- RAM: 64GB's Kingston DDR4 3200 with ECC
- Motherboard: AsRock Rack X570D4U-2L2T
- NIC: Intel X520-DA2 (Dual SFP+)
- GPU: GIGABYTE GeForce RTX 4060 OC Low Profile
- SATA SSD (Boot and Swarm VM's): 2x Samsung 500GB 870 EVO
- NVME SSD (Ceph): 2x Micron 7450 PRO 960GB
- PSU: Seasonic Focus SGX-650
- Case: Sliger CX3150x
- Case Fans: 2x Noctua NF-A12x25 PWM

Non clustered storage is currently provided by two NAS devices
- Synology RS1221+: Primary content / media storage, also runs Proxmox Backup server for testing, and occasionally 2 VM's for Swarm related testing
    - 4x Seagate Exos X18 18TB HDD's
    - 2x Samsung 500GB 870 EVO SSD's (VM Storage)
- Synology DS: Primarily used for when Blu-Ray / DVD's are being imported, where downloaded content is temporarily stored, and for local copies of Dropbox and OneDrive files.
    - 4x SAMSUNG 870 QVO 2TB SSD's

An additional RS1221+ may be part of future expansions and be used for backups. But idea might get may be replaced by something custom built running Proxmox with a TruNAS Scale VM or the like.

## Software Stack

### Hypervisor
All of my nodes run on Proxmox, which is configured into a cluster, with CEPH for the clustered storage.

### VM's
The VM's are a mix of Ubuntu server for everything related to Docker, and Windows 11 for when I need / want a UI. And as a place to remote into.

### Windows
Consists of a single VM for now, named Golden Gate. Which has network connections to every VLAN.

### Ubuntu
Within the Eos Proxmox cluster there is the Eos Docker swarm cluster. Any VM's in the swarm cluster are not set up for HA, as that is handled by the swarm and swarm managers. All also run on Ubuntu Server. They consist of:
- 3x Manager VM's (1 per proxmox host) which provide 2 floating VIPS for cluster access. These are the "Starbase" nodes
- 3x Worker VM's (1 per Proxmox host, with 1 GPU attached) for general purpose containers. These are the "Sovereign" nodes
- 2x Worker VM's hat have VPN connections for anything I need secured. These are the "Defiant" nodes

Yes, those are all Star Trek references.

Additionally, there are 2 standalone VM's for Docker, each set up in HA mode on Proxmox
- 1 For any containers I didn't want in the Swarm, also hosts the Pterodactyl Panel and associated services, known as Wing Commander
- 1 For hosting Pterodactyl Wings, known as Jurassic Park 01

Finally, there is the Voyager type of node, which has / will run on the Synology NAS's (Or whatever replaces them...), and act as the lower powered version of the Sovereign nodes. The basic premise is that anything not requiring a GPU or VPN connection would run on the Voyager nodes.




