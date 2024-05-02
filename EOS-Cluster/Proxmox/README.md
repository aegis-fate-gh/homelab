Initial Proxmox Setup
1. Install PVE, naming each server as desired. Ensure Raid 1 is set for the boot drives to ensure redundancy
2. Change the networking config as required. In my case, the bridges needed to be manually created and assigned to their corresponding vlan before the webui was accessible
3. Once installed and the bridges configured, update the node and reboot as needed
4. Once all 3 nodes are up and updated, create a cluster on the first node
5. Join the other two nodes to the cluster once they are ready

Nvidia GPU Setup
Note: This presumes that the goal is to attach the GPU to a VM. To use them with LXC containers, you do not want to do this.
See basic guide here: https://www.reddit.com/r/homelab/comments/b5xpua/the_ultimate_beginners_guide_to_gpu_passthrough/
1. Ensure IOMMU is enabled: dmesg | grep -e DMAR -e IOMMU
2. Ensure interrupt remapping is enabled: dmesg | grep 'remapping'
3. Blacklist the drivers: echo "blacklist nouveau" >> /etc/modprobe.d/blacklist.conf && echo "blacklist nvidia*" >> /etc/modprobe.d/blacklist.conf
4. echo "options vfio-pci ids=10de:2882,10de:22be disable_vga=1"> /etc/modprobe.d/vfio.conf
4. Reboot server

Ceph Configuration
1. Ensure all nodes are in Proxmox cluster
2. Ensure the network is setup as intended
3. Install Ceph on all nodes
4. Create the CEPH Monitors on all nodes
5. Create the OSD's on each node
6. Create the CEPH pool

Ceph FS Configuration
1. Ensure the CEPH Cluster is set up and functioning properly
2. Create one metadata server per node
3. Create the CEPHfs itself

CloudInit Prep
1. Do the following on each node: apt update -y && apt install libguestfs-tools -y

Testing Ceph Performance:
https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/1.3/html/administration_guide/benchmarking_performance

Enable Maintenance mode on a node:
ha-manager crm-command node-maintenance enable <node>

Disable Maintenance mode on a node:
ha-manager crm-command node-maintenance disable <node>