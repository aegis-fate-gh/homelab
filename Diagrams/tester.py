from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom

with Diagram("Cloudflare Tunnel", show=False, direction="TB"):
    with Cluster("Cloudflare"):
        cloudflare = Custom("Converter Now", "/app/icons/cloudflare.png")
    with Cluster("k3s"):
        with Cluster("Namespace: jovian-prod"):
            cloudflare_tunnel = Custom("Converter Now", "/app/icons/cf-tunnel.png")
            freshrss = Custom("Converter Now", "/app/icons/freshrss.png")
            gaming = Custom("Converter Now", "/app/icons/pterodactyl.png")
            grafana = Custom("Converter Now", "/app/icons/grafana.png")
            home = Custom("Converter Now", "/app/icons/littlelink.png")
            immich = Custom("Converter Now", "/app/icons/immich.png")
            jellyfin = Custom("Converter Now", "/app/icons/jellyfin.png")
            requests = Custom("Converter Now", "/app/icons/overseerr.png")
            tautulli = Custom("Converter Now", "/app/icons/tautulli.png")

    cloudflare_tunnel >> Edge(color="#CEA400", style="solid") >> freshrss
    cloudflare_tunnel >> Edge(color="#CEA400", style="solid") >> gaming
    cloudflare_tunnel >> Edge(color="#CEA400", style="solid") >> grafana
    cloudflare_tunnel >> Edge(color="#CEA400", style="solid") >> home
    cloudflare_tunnel >> Edge(color="#CEA400", style="solid") >> immich
    cloudflare_tunnel >> Edge(color="#CEA400", style="solid") >> jellyfin
    cloudflare_tunnel >> Edge(color="#CEA400", style="solid") >> requests
    cloudflare_tunnel >> Edge(color="#CEA400", style="solid") >> tautulli
    cloudflare >> Edge(color="#CEA400", style="solid") >> cloudflare_tunnel
