from diagrams import Diagram, Cluster, Edge
from diagrams.onprem import monitoring, logging, inmemory, database, network, container
from diagrams.custom import Custom

with Diagram("Docker Prod", show=False, direction="TB"):
  xfinity = Custom("xfinity", "./local_icons/xfinity.png")
  unifi = Custom("UDM-Pro SE", "./local_icons/unifi.png")
  internet = Custom("Internet", "./local_icons/internet.png")

  with Cluster("Eos Proxmox Cluster - 3x Physical Hosts - Ryzen 7 5700x, 64GB's ram, 2x Samsung 870 EVO (Boot), 2x Micron 7450 (CEPH), 1x Nvidia RTX 4060, 1x Dual SFP+"):

    with Cluster("Docker Swarm Cluster - 8x VMs"):

      with Cluster("GPU Worker Nodes - x3 - 16GB's RAM, 12cpu, 1x RTX 4060"):
        influxdb = Custom("InfluxDB", "./local_icons/influx.png")
        loki = logging.Loki("Loki")
        standard_monitoring = Custom("GPU Telegraf", "./local_icons/telegraf_logo.png") >> Edge(color="blue", style="solid") >> influxdb
        standard_logging = Custom("Promtail", "./local_icons/promtail.png") >> Edge(color="darkorange", style="solid") >> loki
        standard_portainer_agent = Custom("Portainer Agent", "./local_icons/portainer.png")
        standard_prune_nodes = container.Docker("Prune Nodes")
        grafana = monitoring.Grafana("Grafana")
        unpoller = Custom("Unpoller", "./local_icons/unpoller.png")
        plex = Custom("Plex", "./local_icons/plex.jpg")
        tautulli = Custom("Tautulli", "./local_icons/tautulli.png")
        jellystat = Custom("Jellystat", "./local_icons/jellystat.png")
        jellystat_db = database.Postgresql("Jellystat DB")
        jellyfin = Custom("Jellyfin", "./local_icons/jellyfin.png")
        cloudflare_ddns = Custom("Cloudflare DDNS", "./local_icons/cloudflare.png")
        jdownloader = Custom("JDownloader 2", "./local_icons/jdownloader.png")
        pmm = Custom("Plex Meta Manager", "./local_icons/pmm.png")
        mkvtoolnix = Custom("MKVToolNix", "./local_icons/mkvmerge.png")
        youtubedlmaterial = Custom("Youtube DL Material", "./local_icons/youtube.png")
        youtube_dl_mongodb = database.Mongodb("Youtube DL Mongo DB") >> youtubedlmaterial
        freshrss = Custom("FreshRSS", "./local_icons/freshrss.png")
        krusader = Custom("Krusader", "./local_icons/krusader.png")
        chronograf = Custom("Chronograf", "./local_icons/chronograf.png") >> influxdb
        fah = Custom("Folding@Home", "./local_icons/foldingathome.jpeg")
        dockervolumebackup = Custom("Docker-Volume-Backup", "./local_icons/docker-volume-backup.png")
        filebrowser = Custom("File Browser", "./local_icons/filebrowser.png")
        immich = Custom("Immich Server", "./local_icons/immich.png")
        immich_micro = Custom("Immich Microservices", "./local_icons/immich.png") >> immich
        immich_ml = Custom("Immich Machine Learning", "./local_icons/immich.png") >> immich
        immich_redis = inmemory.Redis("Immich Redis") >> immich
        immich_db = database.Postgresql("Immich DB") >> immich
        ghost = Custom("Ghost CMS", "./local_icons/ghost-cms.png")
        ghost_db = database.Mysql("Ghost DB") >> ghost
        uptimekuma = Custom("Uptime Kuma", "./local_icons/uptime-kuma.png")
        prometheus = monitoring.Prometheus("Prometheus")
        mc_monitor = Custom("mc-monitor", "./local_icons/minecraft-monitor.png")
        mc_telegraf = Custom("MC Telegraf", "./local_icons/telegraf_logo.png")
        pterodactyl_eos = Custom("Pterodactyl Panel", "./local_icons/pterodactyl.png")
        ptero_redis_eos = inmemory.Redis("Ptero-Redis") >> pterodactyl_eos
        ptero_mariadb_eos = database.Mariadb("Ptero-MariaDB") >> pterodactyl_eos
        varken = Custom("Varken", "./local_icons/varken.png")

      with Cluster("VPN Worker Nodes - x2 - 8GB's RAM, 4cpu"):
        vpn_monitoring = Custom("Telegraf", "./local_icons/telegraf_logo.png") >> Edge(color="blue", style="solid") >> influxdb
        vpn_logging = Custom("Promtail", "./local_icons/promtail.png") >> Edge(color="darkorange", style="solid") >> loki
        vpn_portainer_agent = Custom("Portainer Agent", "./local_icons/portainer.png")
        vpn_prune_nodes = container.Docker("Prune Nodes")
        overseerr = Custom("Overseerr", "./local_icons/overseerr.png")
        sonarr = Custom("Sonarr", "./local_icons/sonarr.png")
        radarr = Custom("Radarr", "./local_icons/radarr.png")
        bazarr = Custom("Bazarr", "./local_icons/bazarr.png")
        prowlarr = Custom("Prowlarr", "./local_icons/prowlarr.png")
        qbittorrent = Custom("qBittorrent", "./local_icons/qBittorrent.png")

      with Cluster("Manager Nodes - x3 - 12GB's RAM, 4cpu"):
        manager_monitoring = Custom("Telegraf", "./local_icons/telegraf_logo.png") >> Edge(color="blue", style="solid") >> influxdb
        manager_logging = Custom("Promtail", "./local_icons/promtail.png") >> Edge(color="darkorange", style="solid") >> loki
        manager_portainer_agent = Custom("Portainer Agent", "./local_icons/portainer.png")
        manager_prune_nodes = container.Docker("Prune Nodes")
        portainer = Custom("Portainer", "./local_icons/portainer.png")
        shepherd = Custom("Shepherd", "./local_icons/shepherd.png")
        swarm_cronjob = Custom("Swarm Cronjob", "./local_icons/swarm-cronjob.png")
        traefik = network.Traefik("Traefik\nInternal Proxy")
        cftunnel = Custom("Cloudflare Tunnel", "./local_icons/cf-tunnel.png")

    with Cluster("Jurassic-Park-01 - x1 VM - 16GB's RAM, 8cpu"):
      with Cluster("Docker"):
        jp_monitoring = Custom("Telegraf", "./local_icons/telegraf_logo.png") >> Edge(color="blue", style="solid") >> influxdb
        jp_logging = Custom("Promtail", "./local_icons/promtail.png") >> Edge(color="darkorange", style="solid") >> loki
        jp_portainer_agent = Custom("Portainer Agent", "./local_icons/portainer.png")
        new_arcadia = Custom("New Arcadia", "./local_icons/minecraft-monitor.png") 

      with Cluster("Native"):
        pterodactyl_wings = Custom("Pterodactyl Wings", "./local_icons/pterodactyl.png")

    with Cluster("Wing-Commander - x1 VM - 8GB's RAM, 4cpu"):
      with Cluster("Docker"):
        wc_portainer_agent = Custom("Portainer Agent", "./local_icons/portainer.png")
        iperf3 = Custom("Iperf3", "./local_icons/iperf.gif")
        wc_logging = Custom("Promtail", "./local_icons/promtail.png") >> Edge(color="darkorange", style="solid") >> loki
        wc_monitoring = Custom("Telegraf", "./local_icons/telegraf_logo.png") >> Edge(color="blue", style="solid") >> influxdb
        npm = Custom("Nginx Proxy Manager\nExternal Proxy", "./local_icons/npm.png")
        authentik_server = Custom("Authentik Server", "./local_icons/authentik.png")
        authentik_worker = Custom("Authentik Worker", "./local_icons/authentik.png")
        authentik_redis = inmemory.Redis("Authentik Redis")
        authentik_db = database.Postgresql("Authentik DB")
      with Cluster("Native"):
        pterodactyl = Custom("Pterodactyl Panel", "./local_icons/pterodactyl.png")
        ptero_redis = inmemory.Redis("Ptero-Redis") >> pterodactyl
        ptero_mariadb = database.Mariadb("Ptero-MariaDB") >> pterodactyl

    internet >> xfinity >> unifi >> Edge(color="royalblue", style="bold") >> plex
    unifi >> Edge(color="royalblue", style="bold") >> npm
    unifi >> Edge(color="royalblue", style="solid") >> unpoller
    unifi << Edge(color="royalblue", style="bold")
    unifi >> Edge(color="royalblue", style="bold") >> pterodactyl_wings >> pterodactyl

    authentik_worker >> authentik_server
    authentik_db >> authentik_server
    authentik_db >> authentik_worker
    authentik_redis >> authentik_server
    authentik_redis >> authentik_worker

    npm >> Edge(color="darkred", style="bold") >> grafana
    npm >> Edge(color="darkred", style="bold") >> overseerr
    npm >> Edge(color="darkred", style="dashed") >> uptimekuma
    npm >> Edge(color="darkred", style="bold") >> pterodactyl
    npm >> Edge(color="darkred", style="bold") >> jellyfin
    npm >> Edge(color="darkred", style="dashed") >> influxdb
    npm >> Edge(color="darkred", style="dashed") >> loki

    cftunnel >> Edge(color="orange", style="bold") >> freshrss
    cftunnel >> Edge(color="orange", style="bold") >> ghost

    portainer >> Edge(color="deeppink", style="solid") >> standard_portainer_agent
    portainer >> Edge(color="deeppink", style="solid") >> manager_portainer_agent
    portainer >> Edge(color="deeppink", style="solid") >> jp_portainer_agent
    portainer >> Edge(color="deeppink", style="solid") >> wc_portainer_agent
    portainer >> Edge(color="deeppink", style="solid") >> vpn_portainer_agent

    swarm_cronjob >> Edge(color="navyblue", style="solid") >> shepherd
    swarm_cronjob >> Edge(color="navyblue", style="solid") >> vpn_prune_nodes
    swarm_cronjob >> Edge(color="navyblue", style="solid") >> manager_prune_nodes
    swarm_cronjob >> Edge(color="navyblue", style="solid") >> standard_prune_nodes

    pmm >> plex >> tautulli >> varken >> influxdb
    jellyfin >> jellystat >> jellystat_db

    overseerr >> Edge(color="magenta1", style="bold") >> sonarr >> Edge(color="turquoise1", style="bold") >> qbittorrent
    overseerr >> Edge(color="magenta1", style="bold") >> radarr >> Edge(color="orange1", style="bold") >> qbittorrent
    overseerr >> Edge(color="magenta1", style="bold") >> plex
    sonarr >> Edge(color="turquoise1", style="bold") >> bazarr
    radarr >> Edge(color="orange1", style="bold") >> bazarr
    sonarr >> Edge(color="turquoise1", style="bold") >> prowlarr
    radarr >> Edge(color="orange1", style="bold") >> prowlarr
    sonarr >> Edge(color="turquoise1", style="bold") >> plex
    radarr >> Edge(color="orange1", style="bold") >> plex
    sonarr >> Edge(color="turquoise1", style="bold") >> jellyfin
    radarr >> Edge(color="orange1", style="bold") >> jellyfin

    unpoller >> Edge(color="blue", style="dashed") >> influxdb

    new_arcadia >> Edge(color="blue", style="solid") >> mc_monitor
    mc_monitor >> Edge(color="blue", style="solid") >> mc_telegraf
    mc_telegraf >> Edge(color="blue", style="solid") >> influxdb

    influxdb >> grafana
    prometheus >> grafana
    loki >> grafana