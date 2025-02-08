Setting up CephFS

1. Create the cepf config folder on each node (see ansible cephfs)

2. Create the directory you want on the Proxmox node under /mnt/pve/(insert cephfs name here)

2. Generate the minimal config
    ssh root@192.168.6.30 "sudo ceph config generate-minimal-conf" | sudo tee /etc/ceph/ceph.conf

3. Get the needed secret key to access the share, and add it to a keyring file:
    ssh root@192.168.6.30 "sudo ceph fs authorize eos-fs client.dockerswarm /swarm_prod rw" | sudo tee /etc/ceph/ceph.client.dockerswarm.keyring

4. Change the permissions on the keyring file: 
    chmod 600 /etc/ceph/ceph.client.jurassicpark.keyring
    
5. Add to cephfs to fstab
    # Important note, none of the secrets here are in use anymore, as they were either only used for testing or have since been replaced. They are only for illustrative purposes.
    nano /etc/fstab
        10.1.100.30,10.1.100.31,10.1.100.32:/swarm_prod     /mnt/ceph    ceph    name=dockerswarm,secret=AQDSvgBmT1iaFhAAMj76ud9oV1sw642LhoeZEg==,rw,noatime,_netdev    0       2

6. Mount cephfs
    mount -a

7. Mounting multiple cephfs pools
    https://docs.ceph.com/en/mimic/cephfs/kernel/
    If there's more than one Ceph pool and more than one cephfs namespace, extra configuration is required to both ensure you connect to the correct one, and to allow connecting to multiple pools simultaneously. Firstly, you'll need to use an admin account, or one with all of the needed permissions to every pool. The final key is an extra option when you add the fstab entry.

    For Ex:
    10.1.100.30,10.1.100.31,10.1.100.32:/     /mnt/ceph    ceph    name=zion,secret=AQB/jjln4zKJBhAAbBQcq/8Ie5WjvPtOXsLC/g==,mds_namespace=eos-fs,rw,noatime,_netdev    0       2
    10.1.100.30,10.1.100.31,10.1.100.32:/     /mnt/media    ceph    name=zion,secret=AQB/jjln4zKJBhAAbBQcq/8Ie5WjvPtOXsLC/g==,mds_namespace=hdd-cephfs,rw,noatime,_netdev    0       2

    Note the addition of the mds_namespace option. With that, you can select which pool a given mount point is using.

Setting up Docker Swarm
https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/

1. docker swarm init --advertise-addr <MANAGER-IP>

Installing Nvidia Drivers
https://ubuntu.com/server/docs/nvidia-drivers-installation

1. See available and compatible drivers
    sudo ubuntu-drivers list --gpgpu

2. Install a given version of the drivers
    sudo ubuntu-drivers install nvidia:535-server


3. Install the nvidia utilities
    sudo apt install nvidia-utils-535-server

Install the Nvidia Container Toolkit
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

Add Node labels as appropriate. For Ex:
docker node update --label-add nvidia=true sovereign-01
docker node update --label-add nvidia=false starbase-01
docker node update --label-add connection=standard voyager-01
docker node update --label-add connection=vpn defiant-03
docker node update --label-add connection=wan2 excelsior-01

docker node update --label-add host_type=proxmox sovereign-01
docker node update --label-add host_type=proxmox sovereign-02
docker node update --label-add host_type=proxmox sovereign-03
docker node update --label-add host_type=proxmox defiant-01
docker node update --label-add host_type=proxmox defiant-02
docker node update --label-add host_type=synology voyager-01
docker node update --label-add host_type=synology defiant-03

docker node update --label-add name=sovereign-01 sovereign-01
docker node update --label-add name=sovereign-02 sovereign-02
docker node update --label-add name=sovereign-03 sovereign-03