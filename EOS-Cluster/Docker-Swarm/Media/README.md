If not using the Ansible way....

Install Samba:
sudo apt install cifs-utils

Make the needed directories:
sudo mkdir /mnt/samba
sudo mkdir /mnt/samba/media
sudo mkdir /mnt/samba/media/media
sudo mkdir /mnt/samba/media/downloads
sudo mkdir /mnt/samba/media/disk-imports
sudo mkdir /mnt/samba/cloud-storage
sudo mkdir /mnt/samba/cloud-storage/dropbox
sudo mkdir /mnt/samba/cloud-storage/onedrive

Make the needed credentials file directory:
mkdir /root/smbcredentials && chmod -R 550 /root/smbcredentials

Add the needed credentials:
vi /root/smbcredentials/eos

And then paste in the below with the needed credentials:
user=mysambauser
password=mysambapassword

To add these to fstab
sudo su -c "echo '//192.168.100.192/Media /mnt/samba/media/media cifs credentials=/root/smbcredentials/eos,uid=1000,gid=1000 0 0' >> /etc/fstab"
sudo su -c "echo '//192.168.100.42/Disk-Imports /mnt/samba/media/disk-imports cifs credentials=/root/smbcredentials/eos,uid=1000,gid=1000 0 0' >> /etc/fstab"
sudo su -c "echo '//192.168.100.42/Downloads /mnt/samba/media/downloads cifs credentials=/root/smbcredentials/eos,uid=1000,gid=1000 0 0' >> /etc/fstab"
sudo su -c "echo '//192.168.100.42/Dropbox /mnt/samba/cloud-storage/dropbox cifs credentials=/root/smbcredentials/eos,uid=1000,gid=1000 0 0' >> /etc/fstab"
sudo su -c "echo '//192.168.100.42/OneDrive /mnt/samba/cloud-storage/onedrive cifs credentials=/root/smbcredentials/eos,uid=1000,gid=1000 0 0' >> /etc/fstab"


And then run the below to mount all of them:
sudo mount -a