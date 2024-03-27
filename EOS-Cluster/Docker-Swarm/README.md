To fix "Unable to find an agent on any Manager Node" in Portainer

SSH into a manager node and run:
docker service update portainer_agent --force

That forces an update and restart of the portainer agents on every node.