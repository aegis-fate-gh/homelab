#Until a better backup solution is in place, this is the script to backup the New Arcadia minecraft files offsite

# Find and copy the latest backup file to OneDrive
cp "$(find /mnt/ceph/ -maxdepth 1 -type f -exec ls -t {} + | head -1)" /mnt/samba/cloud-storage/onedrive/Pterodactyl_Backups/NewArcadia/

# Delete anything older than 7 days
find /mnt/samba/cloud-storage/onedrive/Pterodactyl_Backups/NewArcadia/ -type f -mtime +7 -exec rm -f {} +