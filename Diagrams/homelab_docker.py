from diagrams import Diagram, Cluster, Edge
from diagrams.onprem import monitoring, logging, inmemory, database, network, container
from diagrams.custom import Custom

with Diagram("Homelab docker", show=False, direction="TB"):

  with Cluster("AWS-SkyEye - 2GB's RAM, 2cpu"):
    skyeye_portainer = Custom("Portainer", "./local_icons/portainer.png")
    aws_logging = Custom("Promtail", "./local_icons/promtail.png")
    aws_monitoring = Custom("Telegraf", "./local_icons/telegraf_logo.png")
    skyeye_watchtower = Custom("Watchtower", "./local_icons/watchtower.png")
    skyeye_cftunnel = Custom("Cloudflare Tunnel", "./local_icons/cf-tunnel.png")
    skyeye_uptimekuma = Custom("Uptime Kuma", "./local_icons/uptime-kuma.png")
    gluetun = Custom("Gluetun", "./local_icons/gluetun.svg")

  with Cluster("Eos Proxmox Cluster - 5x Physical Hosts"):

    with Cluster("Docker Swarm Cluster - 10x VMs"):

      with Cluster("GPU Worker Nodes - x3 - 16GB's RAM, 12cpu, 1x RTX 4060"):
        influxdb = Custom("InfluxDB", "./local_icons/influx.png")
        standard_monitoring = Custom("GPU Telegraf", "./local_icons/telegraf_logo.png")
        standard_logging = Custom("Promtail", "./local_icons/promtail.png")
        promtail = Custom("Promtail Syslog", "./local_icons/promtail.png")
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
        kometa = Custom("Kometa", "./local_icons/kometa.png")
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
        overseerr = Custom("Overseerr", "./local_icons/overseerr.png")
        rclone_immich = Custom("Rclone - Immich", "./local_icons/rclone.png")
        rclone_pterodactyl = Custom("Rclone - Pterodactyl", "./local_icons/rclone.png")
        rclone_media = Custom("Rclone - Media", "./local_icons/rclone.png")
        rclone_cloud_vault = Custom("Rclone - Cloud", "./local_icons/rclone.png")

      with Cluster("VPN Worker Nodes - x2 - 8GB's RAM, 4cpu"):
        vpn_monitoring = Custom("Telegraf", "./local_icons/telegraf_logo.png")
        vpn_logging = Custom("Promtail", "./local_icons/promtail.png")
        vpn_portainer_agent = Custom("Portainer Agent", "./local_icons/portainer.png")
        vpn_prune_nodes = container.Docker("Prune Nodes")
        sonarr = Custom("Sonarr", "./local_icons/sonarr.png")
        radarr = Custom("Radarr", "./local_icons/radarr.png")
        bazarr = Custom("Bazarr", "./local_icons/bazarr.png")
        prowlarr = Custom("Prowlarr", "./local_icons/prowlarr.png")
        qbittorrent = Custom("qBittorrent", "./local_icons/qBittorrent.png")

      with Cluster("Draper internet Worker Nodes - x2 - 8GB's RAM, 4cpu"):
        draper_monitoring = Custom("Telegraf", "./local_icons/telegraf_logo.png")
        draper_logging = Custom("Promtail", "./local_icons/promtail.png")
        draper_portainer_agent = Custom("Portainer Agent", "./local_icons/portainer.png")
        draper_prune_nodes = container.Docker("Prune Nodes")
        rclone_b2 = Custom("Rclone B2 Uploader", "./local_icons/rclone.png")

      with Cluster("Manager Nodes - x3 - 12GB's RAM, 4cpu"):
        manager_monitoring = Custom("Telegraf", "./local_icons/telegraf_logo.png")
        manager_logging = Custom("Promtail", "./local_icons/promtail.png")
        manager_portainer_agent = Custom("Portainer Agent", "./local_icons/portainer.png")
        manager_prune_nodes = container.Docker("Prune Nodes")
        portainer = Custom("Portainer", "./local_icons/portainer.png")
        shepherd = Custom("Shepherd", "./local_icons/shepherd.png")
        swarm_cronjob = Custom("Swarm Cronjob", "./local_icons/swarm-cronjob.png")
        traefik = network.Traefik("Traefik\nInternal Proxy")
        cftunnel = Custom("Cloudflare Tunnel", "./local_icons/cf-tunnel.png")

    with Cluster("Jurassic-Park-01 - 24GB's RAM, 8cpu"):
      jp1_monitoring = Custom("Telegraf", "./local_icons/telegraf_logo.png")
      jp1_logging = Custom("Promtail", "./local_icons/promtail.png")
      jp1_portainer_agent = Custom("Portainer Agent", "./local_icons/portainer.png")
      new_arcadia = Custom("Minecraft - New Arcadia", "./local_icons/minecraft-monitor.png")
      jp1_pterodactyl_wings = Custom("Pterodactyl Wings", "./local_icons/pterodactyl.png")    
      jp1_watchtower = Custom("Watchtower", "./local_icons/watchtower.png")
      jp1_crowdsec = Custom("Crowdsec", "./local_icons/crowdsec.jpeg") 

    with Cluster("Jurassic-Park-02 - 24GB's RAM, 8cpu"):
      jp2_monitoring = Custom("Telegraf", "./local_icons/telegraf_logo.png")
      jp2_logging = Custom("Promtail", "./local_icons/promtail.png")
      jp2_portainer_agent = Custom("Portainer Agent", "./local_icons/portainer.png")
      jp2_pterodactyl_wings = Custom("Pterodactyl Wings", "./local_icons/pterodactyl.png")
      jp2_watchtower = Custom("Watchtower", "./local_icons/watchtower.png")
      jp2_crowdsec = Custom("Crowdsec", "./local_icons/crowdsec.jpeg") 

    with Cluster("Polaris - 8GB's RAM, 4cpu"):
      polaris_monitoring = Custom("Telegraf", "./local_icons/telegraf_logo.png")
      polaris_logging = Custom("Promtail", "./local_icons/promtail.png")
      polaris_portainer_agent = Custom("Portainer Agent", "./local_icons/portainer.png")
      loki = logging.Loki("Loki")
      polaris_watchtower = Custom("Watchtower", "./local_icons/watchtower.png") 

    with Cluster("Wing-Commander - x1 VM - 8GB's RAM, 4cpu"):
      wc_portainer_agent = Custom("Portainer Agent", "./local_icons/portainer.png")
      iperf3 = Custom("Iperf3", "./local_icons/iperf.gif")
      wc_logging = Custom("Promtail", "./local_icons/promtail.png")
      wc_monitoring = Custom("Telegraf", "./local_icons/telegraf_logo.png")

    kometa >> plex >> tautulli
    jellyfin >> jellystat >> jellystat_db

    unpoller >> Edge(color="blue", style="dashed") >> influxdb

    mc_monitor >> Edge(color="blue", style="solid") >> mc_telegraf
    mc_telegraf >> Edge(color="blue", style="solid") >> influxdb

    influxdb >> grafana
    prometheus >> grafana
    loki >> grafana