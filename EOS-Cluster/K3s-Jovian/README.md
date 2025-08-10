Netplan Example

network:
  version: 2
  ethernets:
    eth0:
      match:
        macaddress: "bc:24:11:7f:7e:a2"
      dhcp4: true
      set-name: "eth0"
    enp6s19:
      dhcp4: false
      addresses: [10.1.100.120/24]
      dhcp6: false
    enp6s20:
      dhcp4: false
      addresses: [10.1.90.120/24]
      dhcp6: false

Installing Nvidia Drivers:

Install Ubuntu drivers
https://documentation.ubuntu.com/server/how-to/graphics/install-nvidia-drivers/index.html

1. apt install -y ubuntu-drivers-common
2. ubuntu-drivers install --gpgpu nvidia:570-server

Install the nvidia container toolkit:
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#with-apt-ubuntu-debian

3. curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg   && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list |     sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' |     sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
4. apt-get update
5. apt-get install -y nvidia-container-toolkit

Install K3s if not already installed
6. nvidia-ctk runtime configure --runtime=containerd

Ensure that all of that worked...
7. grep nvidia /var/lib/rancher/k3s/agent/etc/containerd/config.toml

Install the encode and decode packages
8. apt install libnvidia-encode-570-server
9. apt install libnvidia-decode-570-server

Reboot the server
