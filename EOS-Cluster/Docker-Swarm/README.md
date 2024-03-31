To fix "Unable to find an agent on any Manager Node" in Portainer

SSH into a manager node and run:
docker service update portainer_agent --force

That forces an update and restart of the portainer agents on every node.

Adding labels to nodes:
docker node update --label-add vpn=true defiant-01

Removing labels from a node:
docker node update --label-rm vpn defiant-01