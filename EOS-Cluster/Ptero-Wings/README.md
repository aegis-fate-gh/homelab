Within this folder are the configs for the newer Pterodactyl Wings servers set up with Ansible. Using ptero-wings-setup.yml essentially handles every part of the setup. Having said there, there are some extra things to do.

For Wings within Docker to work...

1. Disable the UFW firewall: systemctl disable ufw.service
2. Get the ssl certs:

    acme.sh --issue --dns dns_cf -d "FQDN_HERE" --server letsencrypt \
    --key-file /etc/letsencrypt/live/FQDN_HERE/privkey.pem \
    --fullchain-file /etc/letsencrypt/live/FQDN_HERE/fullchain.pem

And that's it! Ansible really is quite helpful.
