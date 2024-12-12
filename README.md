# Homelab
This is centralized repo for everything related to my homelab

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
- SATA HDD (Ceph HDD Storage): 2x Seagate Exos - 1x 24TB, 1x 20TB
- SATA SSD (Ceph DB/WAL): 1x Intel SSDSC2BA400G3 400GB
- PSU: Seasonic Focus SGX-650
- Case: Sliger CX3150x
- Case Fans: 2x Noctua NF-A12x25 PWM

Outside of those 3 main nodes are two others providing additional capabilities. Both participate in the Proxmox quorum voting process and contain OSD's and Monitors for Ceph. But do not run the Manager service or Metadata 

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
- SATA HDD (Ceph HDD Storage): 2x Seagate Exos - 1x 24TB, 1x 20TB
- SATA SSD (Ceph DB/WAL): 1x Intel SSDSC2BA400G3 400GB
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
- SATA HDD (Ceph HDD Storage): 2x Seagate Exos - 1x 24TB, 1x 20TB
- SATA SSD (Ceph DB/WAL): 1x Intel SSDSC2BA400G3 400GB
- PSU: Corsair SF750
- Case: Sliger CX3170a XL
- Case Fans: 3x Noctua NF-A12x25 PWM

Non clustered storage is primarily provided by two Synology devices

### Syn-Vault
- Synology RS1221+: Currently my main media storage server, but will soon become the backup for my media storage. Was upgraded to 32GB's of ram to enable VM testing.
    - 5x Seagate Exos 18TB HDD's
    - 2x Samsung 500GB 870 EVO SSD's (VM Storage)
    - Synology E10G21-F2 dual SFP+
    - 32GB's OWC DDR4 2666 ECC RAM

### Syn-Coruscant
- Synology DS923+: Primarily used for when Blu-Ray / DVD's are being imported.
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
Within the Eos Proxmox cluster there is the Eos Docker swarm cluster. Any VM's in the swarm cluster are not set up for HA, as that is handled by the swarm and swarm managers. All also run on Ubuntu Server. They consist of:
- 3x Manager VM's (1 per proxmox host) which provide 2 floating VIPS for cluster access. These are the "Starbase" nodes
- 3x Worker VM's (1 per Proxmox host, with 1 GPU attached) for general purpose containers. These are the "Sovereign" nodes
- 2x Worker VM's hat have VPN connections for anything I need secured. These are the "Defiant" nodes

Yes, those are all Star Trek references.

Additionally, there are 2 standalone VM's for Docker, each set up in HA mode on Proxmox
- 1 For any containers I didn't want in the Swarm, also hosts the Pterodactyl Panel and associated services, known as Wing Commander
- 1 For hosting Pterodactyl Wings, known as Jurassic Park 01

Finally, there is the Voyager type of node, which has / will run on the Synology NAS's (Or whatever replaces them...), and act as the lower powered version of the Sovereign nodes. The basic premise is that anything not requiring a GPU or VPN connection would run on the Voyager nodes.