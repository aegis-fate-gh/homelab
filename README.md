# Homelab
This is centralized repo for most things related to my homelab

## Physical Infrastructure
### Eos 1-3
What I call "Eos" is composed of 3 identical servers. Using what I learned from testing on Andromeda (See below), they were built to allow for an easy highly available core group of servers. They do this without lots of noise, power consumption, or cost (Relatively speaking....). Each of the 3 is composed of:
- CPU: AMD Ryzen 5700X
- CPU Cooler: Noctua NH-D9L
- RAM: 128GB's DDR4 3200 with ECC
- Motherboard: AsRock Rack X570D4U-2L2T
- NIC: Intel X520-DA2 (Dual SFP+)
- GPU: GIGABYTE GeForce RTX 4060 OC Low Profile
- SATA SSD (Proxmox boot drives): 2x Samsung 500GB 870 EVO
- NVME SSD (Ceph NVMe storage): 2x Micron 7450 PRO 960GB
- PSU: Seasonic Focus SGX-650
- Case: Sliger CX3150x
- Case Fans: 2x Noctua NF-A12x25 PWM

Outside of those 3 main nodes are two others providing additional capabilities. Both participate in the Proxmox quorum voting process.

### Donnager
By far my oldest server, and formerly my only homelab and storage server. It was originally built for mass video transcoding, and was then setup for remote gaming using GPU passthrough. It was last used with UnRaid, housing 6 6TB SSD's for Plex media storage. Now it runs Proxmox and houses a VM for Dropbox / OneDrive synching, and Proxmox Backup Server.
- CPU: AMD Ryzen Threadripper 1950x
- CPU Cooler: NH-U12S TR4-SP3
- RAM: 64GB's DDR4 2133
- Motherboard: X399M Taichi
- NIC: Intel X520-DA2 (Dual SFP+)
- GPU: VisionTek AMD Radeon 5450
- NVME SSD (Boot and VM Storage): 3x 500GB WD Black
- NVME SSD (VM Storage): 4x 2TB Samsung 990 Evo Plus
- PSU: Corsair RM550x
- Case: Fractal Design Node 804
- Case Fans: 3x Noctua NF-A12x25 PWM

### Andromeda
With the CPU from my last gaming PC, this served as my main hardware testing server. It was essentially the testbed for what would become the Eos cluster. Allowing me to test out both the Intel Arc A380 and Nvidia GPU's for Plex transcoding.
- CPU: AMD Ryzen 3700X
- CPU Cooler: Noctua NH-D9L
- RAM: 128GB's DDR4 3200
- Motherboard: AsRock Rack X570D4U
- NIC: Intel X520-DA2 (Dual SFP+)
- GPU: None
- SATA SSD (Proxmox boot drives): 2x Samsung 500GB 870 EVO
- NVME SSD (VM Storage): 2x WD Black SN770's
- PSU: Corsair SF750
- Case: Sliger CX3170a XL
- Case Fans: 3x Noctua NF-A12x25 PWM

Non clustered storage is primarily provided by two Synology devices

### Syn-Sanctuary
- Synology RS1221+: Offsite backup located at my parents house. Also runs Uptime-Kuma for offsite monitoring. That secondary role resulted in removing a AWS lightsail instance (AWS-Skyeye) I was using for this purpose.
    - 5x Seagate Exos 20TB HDD's
    - 2x Intel 400GB 870 EVO SSD's
    - Synology E10G21-F2 dual SFP+
    - 32GB's OWC DDR4 2666 ECC RAM

### Syn-Coruscant
- Synology DS923+: Primarily used for syncing immich related data between my parents house and my homelab
    - 4x SAMSUNG 870 QVO 2TB SSD's
    - Synology E10G22-T1-Mini 10GBe

## Software Stack

### Hypervisor
All of my nodes run on Proxmox, which is configured into a cluster, with CEPH for the clustered storage.

### VM's
The VM's are a mix of Ubuntu server for everything related to Docker, and Windows 11 for when I need / want a UI. And as a place to remote into.

### Windows
Consists of a single VM for now, named Golden Gate.

### Ubuntu
Most of my homelab is running on an ubuntu server VM in some configuration. With the exception of the kubernetes nodes and Polaris, all other nodes are set up with High Availability to enable moving between hosts as needed.

Kubernetes Cluster - Runs on EOS-01-03:
The majority of the apps I run are now within my kubernetes cluster, named Jovian. It replaced the Eos Docker Swarm Cluster in 2025. This currently consists of 8 nodes.
3x Nodes for the control plane / etcd, named Jupiter 01-03
3x Worker nodes with GPU's passed through for the majority of applications, named Ganymede 01-03
2x Worker nodes with internet provided through a VPN, named Ganymede 01-02. These nodes are due for replacement due to increased knowledge with pods rendering them redundant

Polaris - Runs on Donnager:
Runs docker containers I don't want in the main kubernetes cluster.

Zion - Runs on EOS-01-03:
Prior to the switch to UNAS-Pro's, this enabled SMB access to the HDD based CEPH pool.

Wings-01-02 - Runs on EOS-01-03:
Host the Pterodactyl Wings docker containers for game server hosting.

LunaLand - Runs on EOS-01-03:
Used for testing and experiments by a friend. Is located in a separate VLAN from the rest of my homelab.
