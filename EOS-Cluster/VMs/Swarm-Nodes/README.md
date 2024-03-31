Setting up CephFS

1. Create the cepf config folder on each node (see ansible cephfs)
2. Create the directory you want on the Proxmox node under /mnt/pve/(insert cephfs name here)
2. Generate the minimal config
    ssh root@192.168.6.30 "sudo ceph config generate-minimal-conf" | sudo tee /etc/ceph/ceph.conf
3. Get the needed secret key to access the share, and add it to a keyring file:
    ssh root@192.168.6.30 "sudo ceph fs authorize eos-fs client.dockerswarm /swarm_prod rw" | sudo tee /etc/ceph/ceph.client.dockerswarm.keyring
    ssh root@192.168.6.30 "sudo ceph fs authorize eos-fs client.jurassicpark /ptero_backups rw" | sudo tee /etc/ceph/ceph.client.jurassicpark.keyring
4. Change the permissions on the keyring file: 
    chmod 600 /etc/ceph/ceph.client.dockerswarm.keyring
    chmod 600 /etc/ceph/ceph.client.jurassicpark.keyring
5. Add to cephfs to fstab
    nano /etc/fstab
        10.1.100.30,10.1.100.31,10.1.100.32:/swarm_prod     /mnt/ceph    ceph    name=dockerswarm,secret=AQDSvgBmT1iaFhAAMj76ud9oV1sw642LhoeZEg==,rw,noatime,_netdev    0       2
        10.1.100.30,10.1.100.31,10.1.100.32:/ptero_backups     /mnt/ceph    ceph    name=jurassicpark,secret=AQBklwhmLmEwKBAAMvx6888taWuq0amtsJE9Hw==,rw,noatime,_netdev    0       2
6. Mount cephfs
    mount -a

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
docker node update --label-add connection=standard sovereign-01
docker node update --label-add connection=vpn defiant-01