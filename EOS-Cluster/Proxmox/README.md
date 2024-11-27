Initial Proxmox Setup
1. Install PVE, naming each server as desired. Ensure Raid 1 is set for the boot drives to ensure redundancy
2. Change the networking config as required. In my case, the bridges needed to be manually created and assigned to their corresponding vlan before the webui was accessible
3. Once installed and the bridges configured, update the node and reboot as needed
4. Once all nodes are up and updated, create a cluster on the first node
5. Join the other nodes to the cluster once they are ready

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

As a reminder, Eos is backed by 6 Micron 7450 NVMe Drives. The hdd-pool is backed by 5 20TB, and 5 24TB Seagate Exos SATA Hdd's. Also note that Eos is the storage for the majority of the VM in the cluster, and they were not stopped during these tests. Connecting all 5 nodes is a dedicated 10Gb network connection.

Dropping the caches:
sudo echo 3 | sudo tee /proc/sys/vm/drop_caches && sudo sync

10 Second sequential write tests to the respective pools
rados bench -p eos 10 write --no-cleanup
rados bench -p hdd-pool 10 write --no-cleanup

Results:
Eos
Bandwidth MB/s (Max, Min, Avg.): 780, 396, 649.957
IOPS (Max, Min, Avg.): 195, 99, 162
Latency S's (Max, Min, Avg.): 0.359, 0.016, 0.098

hdd-pool
Bandwidth MB/s (Max, Min, Avg.): 228, 148, 198.999
IOPS (Max, Min, Avg.): 57, 37, 49
Latency S's (Max, Min, Avg.): 1.311, 0.058, 0.317

10 Second sequential read tests from the respective pools
rados bench -p eos 10 seq
rados bench -p hdd-pool 10 seq

Results:
eos
Bandwidth MB/s (Avg.): 1810.41
IOPS (Max, Min, Avg.): 477, 446, 452
Latency S's (Max, Min, Avg.): 0.168, 0.003, 0.034

hdd-pool
Bandwidth MB/s (Avg.): 657.513
IOPS (Max, Min, Avg.): 176, 164, 164
Latency S's (Max, Min, Avg.): 0.688, 0.010, 0.090

10 Second random read tests from the respective pools
rados bench -p eos 10 rand
rados bench -p hdd-pool 10 rand

Results:
eos
Bandwidth MB/s (Avg.): 1792.93
IOPS (Max, Min, Avg.): 471, 432, 445
Latency S's (Max, Min, Avg.): 0.277, 0.001, 0.035

hdd-pool
Bandwidth MB/s (Avg.): 1267.87
IOPS (Max, Min, Avg.): 337, 298, 316
Latency S's (Max, Min, Avg.): 0.403, 0.001, 0.049

When done, this cleans up the respective pool
rados -p eos cleanup
rados -p hdd-pool cleanup

Maintenance Mode
Enable Maintenance mode on a node:
ha-manager crm-command node-maintenance enable <node>

Disable Maintenance mode on a node:
ha-manager crm-command node-maintenance disable <node>

Creating multiple Ceph and CephFS Pools
In order to do this, you'll need to ensure the device classes are set correctly, and then you'll need to create new crush rules that take that into account. Note that a given device class needs to exist before creating the crush rule for it.

https://pve.proxmox.com/pve-docs/chapter-pveceph.html#pve_ceph_device_classes

This will show the current rules and the OSD's assigned to them: ceph osd crush tree --show-shadow

Then you create a new crush rule with this: ceph osd crush rule create-replicated <rule-name> <root> <failure-domain> <class>
For example, this will create a rule to only use nvme class drives: ceph osd crush rule create-replicated eos-nvme default host nvme
And this will do the same for HDD class drives: ceph osd crush rule create-replicated eos-hdd default host hdd

Note that once the rule is created, you'll need to then set each pool to the new rule via the GUI. Then wait for it to finish the rebalancing process.

For CephFS pools, it's the same as before, except now you just select the new crush rule. One note though, is that a CephFS metadata server (MDS) is ONE per CephFS, and one per physical host. So with three hosts, you should only really have 2 MDS's for the sake of redundancy.

Ceph Warnings and crashes
https://forum.proxmox.com/threads/resetting-ceph-warnings.65778/

List all warnings and crashes: ceph crash ls

Display detailed info on a given id: ceph crash info <id>

Clear it: ceph crash archive <id>

Clear all of them: ceph crash archive-all