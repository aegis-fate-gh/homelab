In general, if there are two interfaces and if you only want the internet to function from one of them, you'll need to delete any other default routes:
ip route del default via 10.1.100.1

If there isn't already a default to the correct gateway, you can add it this way:
ip route add default via 192.168.6.1



Installing Nvidia GPU Drivers

Go through the process, and follow the instructions
https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local



When this guide was written this was the process:

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.4.0/local_installers/cuda-repo-ubuntu2204-12-4-local_12.4.0-550.54.14-1_amd64.deb

sudo dpkg -i cuda-repo-ubuntu2204-12-4-local_12.4.0-550.54.14-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2204-12-4-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-4

sudo apt-get install -y cuda-drivers
Note: The above will prompt for a secure boot password if it's enabled.... You'll need to type it in on the next reboot for the drivers to actually... work....

Now reboot....

During the reboot, it'll prompt you for the MOK key portion. To enroll the key:
Enroll MOK > Continue > Yes > Type in the password you set above > Reboot

Then test for the gcc compiler:
gcc -v

Next, use the bottom portion of this guide:
https://www.cherryservers.com/blog/install-cuda-ubuntu

Specifically.....

export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-12.5/lib64\
                         ${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

Then reload the file
. ~/.bashrc

And test the Cuda toolkit:
nvcc -V

Next Navigate to the container runtime toml file:
nano /etc/nvidia-container-runtime/config.toml

And uncomment "swarm-resource = "DOCKER_RESOURCE_GPU" "

Via this: https://gist.github.com/coltonbh/374c415517dbeb4a6aa92f462b9eb287
Next run the below to get the GPU UUID:
nvidia-smi -a | grep UUID

For Ex:
GPU UUID                              : GPU-6f43d74b-c54c-ec7b-9104-4bcf68fa2a46

From that, take the first section (GPU-6f43d74b)

Next add that portion into the below code before putting it into the daemon.json (/etc/docker/daemon.json) file:

{
  "runtimes": {
    "nvidia": {
      "path": "/usr/bin/nvidia-container-runtime",
      "runtimeArgs": []
    }
  },
  "default-runtime": "nvidia",
  "node-generic-resources": [
    "NVIDIA-GPU=GPU-45cbf7b"
    ]
}

In this case, when added with the already existing log portion, it looks like this:
{
    "log-driver": "json-file",
    "log-opts": {
        "labels-regex": "^.+"
    },
    "runtimes": {
        "nvidia": {
            "path": "/usr/bin/nvidia-container-runtime",
            "runtimeArgs": []
        }
    },
    "default-runtime": "nvidia",
    "node-generic-resources": [
        "NVIDIA-GPU=GPU-45cbf7b"
    ]
}