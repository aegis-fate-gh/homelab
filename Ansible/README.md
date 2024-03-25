If using manual VM Creation you'll need to manually set it up with the ssh key for ansible:
ssh-copy-id ansible@192.168.6.40


Verify the Inventory file:
ansible-inventory -i inventory.yaml --list

Run a Ping against everything in the EOS Cluster with the ansible user:
ansible EOS_Cluster -m ping -i inventory.yaml -u ansible