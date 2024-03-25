Traefik handles all internal > internal network proxying to the rest of the swarm.

Basically, PiHole sends requests to Traefik for external requests, and then traefik directs it where it needs to go.