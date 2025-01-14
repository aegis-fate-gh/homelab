Post deploy of the container, there are a few things that need to be done.

Note that this assumes the existence of an account on https://app.crowdsec.net/

1. Use the ptero-wings-setup ansible playbook. As it install all of the pre-requisites including the remediation portion of Crowdsec
2. Get a new key by creating a new security engine on the Crowdsec site
3. Add in the acquis.yaml to the config directory
4. To add a bouncer, run the following from within the container itself: cscli bouncers add host-firewall-bouncer-INSERT_NAME_HERE
5. Using the key that you'll get from the above command, add it to the bouncers config in the api_key field, in this case it's located at: /etc/crowdsec/bouncers/crowdsec-firewall-bouncer.yaml
6. After that, you'll need to ensure that the containers logs are showing 200's related to both the connection to crowdsec, and the bouncer.
7. Additionally, within that config disable ipv6, and uncomment the "- DOCKER-USER" line
8. Once complete, restart the bouncer with systemctl restart crowdsec-firewall-bouncer