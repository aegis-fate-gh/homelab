from diagrams import Diagram, Cluster, Edge
from diagrams.onprem import monitoring, logging, inmemory, database, network, container
from diagrams.custom import Custom

with Diagram("Current Homelab", show=False, direction="TB"):
    with Cluster("Cloud Services"):
        backblaze = Custom("Backblaze B2", "./local_icons/backblaze.png")
        dropbox = Custom("Dropbox", "./local_icons/dropbox.png")
        discord = Custom("Discord", "./local_icons/discord.png")
        proton_mail = Custom("Proton Mail", "./local_icons/proton-mail.png")
        proton_vpn = Custom("Proton VPN", "./local_icons/proton-vpn.png")

    with Cluster("Home - Chicago"):
        silo_01 = Custom("UNAS-Pro - Silo-01\n 5x 24TB Seagate Exos HDD's", "./local_icons/unifi.png")
        silo_02 = Custom("UNAS-Pro - Silo-02\n 5x 24TB Seagate Exos HDD's", "./local_icons/unifi.png")
        syn_coruscant = Custom("Synology DS923+\n4x 2TB Samsung 870 QVO", "./local_icons/synology.png")

        with Cluster("Arc Mac Server\nM2 Pro Mac Mini, 32GB's RAM, 512GB SSD, 10GBe"):
            lm_studio = Custom("LM Studio", "./local_icons/lmstudio.png")
            ams_handbrake = Custom("Handbrake", "./local_icons/handbrake.png")
            with Cluster("Docker"):
                ams_portainer = Custom("Portainer", "./local_icons/portainer.png")

        with Cluster("PVE-Donnager\nThreadripper 1950x, 64GB's RAM, 3x 500GB WD Black SSD's, 4x 2TB Samsung 990 EVO Plus SSD's, 1x Dual SFP+"):
            with Cluster("Polaris - Docker Host - VM"):
                polaris_monitoring = Custom("Telegraf", "./local_icons/telegraf_logo.png")
                polaris_portainer = Custom("Portainer", "./local_icons/portainer.png")
                loki = logging.Loki("Loki")
                polaris_watchtower = Custom("Watchtower", "./local_icons/watchtower.png")
                polaris_logging = Custom("Promtail", "./local_icons/promtail.png") >> Edge(color="darkorange", style="solid") >> loki
                polaris_handbrake = Custom("Handbrake", "./local_icons/handbrake.png")

        with Cluster("PVE-EOS-01 > 03\n3x Physical Hosts\nRyzen 7 5700x, 128GB's ECC, 2x 500GB Samsung 870 EVO (Boot), 2x 1TB Micron 7450 (CEPH), 1x Nvidia RTX 4060, 1x Dual SFP+"):
            with Cluster("Jovian Prod - K3s Cluster - 8x VMs"):
                traefik = network.Traefik("Traefik\nInternal Proxy")
                rancher = Custom("Rancher", "./local_icons/rancher.png")
                cftunnel = Custom("Cloudflare Tunnel", "./local_icons/cf-tunnel.png")
                qbittorrent = Custom("qBittorrent", "./local_icons/qBittorrent.png")
                prometheus = monitoring.Prometheus("Prometheus")
                metallb = Custom("Metallb", "./local_icons/metallb.png")
                grafana = monitoring.Grafana("Grafana")
                plex = Custom("Plex", "./local_icons/plex.jpg")
                tautulli = Custom("Tautulli", "./local_icons/tautulli.png")
                jellyfin = Custom("Jellyfin", "./local_icons/jellyfin.png")
                jdownloader = Custom("JDownloader 2", "./local_icons/jdownloader.png")
                mkvtoolnix = Custom("MKVToolNix", "./local_icons/mkvmerge.png")
                freshrss = Custom("FreshRSS", "./local_icons/freshrss.png")
                uptimekuma = Custom("Uptime Kuma", "./local_icons/uptime-kuma.png")
                seerr = Custom("Seerr", "./local_icons/overseerr.png")
                iperf3 = Custom("Iperf3", "./local_icons/iperf.gif")
                homarr = Custom("Homarr", "./local_icons/homarr.png")
                converternow = Custom("Converter Now", "./local_icons/converternow.jpg")
                it_tools = Custom("Homarr", "./local_icons/it-tools.png")
                littlelink = Custom("LittleLink", "./local_icons/littlelink.png")
                openspeedtest = Custom("Openspeedtest", "./local_icons/openspeedtest.png")
                vaultwarden = Custom("VaultWarden", "./local_icons/vaultwarden.png")
                restic = Custom("Restic Backups", "./local_icons/restic.png")

                with Cluster("ArrStack"):
                    sonarr = Custom("Sonarr", "./local_icons/sonarr.png")
                    radarr = Custom("Radarr", "./local_icons/radarr.png")
                    bazarr = Custom("Bazarr", "./local_icons/bazarr.png")
                    prowlarr = Custom("Prowlarr", "./local_icons/prowlarr.png")
                    cleanuparr = Custom("Cleanuparr", "./local_icons/cleanuperr.png")
                    flaresolverr = Custom("Flaresolverr", "./local_icons/flaresolverr.png")
                with Cluster("Paperless"):
                    paperless_ngx = Custom("Paperless-ngx", "./local_icons/paperless-ngx.png")
                    apache_tika = Custom("Apache Tika", "./local_icons/apache_tika.png") >> paperless_ngx
                    paperless_redis = inmemory.Redis("Redis") >> paperless_ngx
                    paperless_db = database.Postgresql("Postgres") >> paperless_ngx
                    gotenberg = Custom("Gotenberg", "./local_icons/gotenberg.png") >> paperless_ngx
                with Cluster("Ghost"):
                    ghost = Custom("Ghost CMS", "./local_icons/ghost-cms.png")
                    ghost_db = database.Mysql("Ghost DB") >> ghost
                with Cluster("Pterodactyl-Panel"):
                    pterodactyl_panel = Custom("Pterodactyl Panel", "./local_icons/pterodactyl.png")
                    ptero_redis = inmemory.Redis("Ptero-Redis") >> pterodactyl_panel
                    ptero_mariadb = database.Mariadb("Ptero-MariaDB") >> pterodactyl_panel
                with Cluster("Immich"):
                    immich = Custom("Immich Server", "./local_icons/immich.png")
                    immich_micro = Custom("Immich Microservices", "./local_icons/immich.png") >> immich
                    immich_ml = Custom("Immich Machine Learning", "./local_icons/immich.png") >> immich
                    immich_redis = inmemory.Redis("Immich Redis") >> immich
                    immich_db = database.Postgresql("Immich DB") >> immich

            with Cluster("Wings-01 - Docker Host - VM"):
                w01_portainer_agent = Custom("Portainer Agent", "./local_icons/portainer.png")
                new_arcadia = Custom("New Arcadia", "./local_icons/minecraft-monitor.png")
                w01_pterodactyl_wings = Custom("Pterodactyl Wings", "./local_icons/pterodactyl.png")
                w01_crowdsec = Custom("Crowdsec", "./local_icons/crowdsec.jpeg")
                w01_watchtower = Custom("Watchtower", "./local_icons/watchtower.png")

            with Cluster("Wings-02 - Docker Host - VM"):
                w02_portainer_agent = Custom("Portainer Agent", "./local_icons/portainer.png")
                test = Custom("Test", "./local_icons/minecraft-monitor.png")
                w02_pterodactyl_wings = Custom("Pterodactyl Wings", "./local_icons/pterodactyl.png")
                w02_crowdsec = Custom("Crowdsec", "./local_icons/crowdsec.jpeg")
                w02_watchtower = Custom("Watchtower", "./local_icons/watchtower.png")

    with Cluster("AWS Lightsail\nOhio Zone-A"):
        with Cluster("AWS-SkyEye - 2GB's RAM, 2cpu"):
            skyeye_portainer = Custom("Portainer", "./local_icons/portainer.png")
            skyeye_watchtower = Custom("Watchtower", "./local_icons/watchtower.png")
            skyeye_cftunnel = Custom("Cloudflare Tunnel", "./local_icons/cf-tunnel.png")
            skyeye_uptimekuma = Custom("Uptime Kuma", "./local_icons/uptime-kuma.png")
            gluetun = Custom("Gluetun", "./local_icons/gluetun.png")

    with Cluster("Parents House - MD"):
        syn_sanctuary = Custom("Synology RS1221+\n32GB's RAM, Dual SFP+\n2x Intel DC S3700 DC 400GB, 5x Seagate Exos 20TB", "./local_icons/synology.png")

    silo_01 >> Edge(color="royalblue", style="bold") >> silo_02
    silo_01 >> Edge(color="royalblue", style="bold") >> backblaze
    silo_01 >> Edge(color="royalblue", style="bold") >> syn_sanctuary

    dropbox >> syn_sanctuary
    dropbox >> syn_coruscant

    immich >> Edge(color="violet", style="bold") >> silo_01
    immich >> Edge(color="violet", style="bold") >> syn_coruscant

    plex >> silo_01

    jellyfin >> silo_01

    tautulli >> Edge(color="darkorange", style="bold") >> plex
    tautulli >> Edge(color="darkorange", style="bold") >> proton_mail

    traefik >> Edge(color="blue", style="dotted") >> jellyfin
    traefik >> Edge(color="blue", style="dotted") >> homarr
    traefik >> Edge(color="blue", style="dotted") >> sonarr
    traefik >> Edge(color="blue", style="dotted") >> radarr
    traefik >> Edge(color="blue", style="dotted") >> prowlarr
    traefik >> Edge(color="blue", style="dotted") >> bazarr
    traefik >> Edge(color="blue", style="dotted") >> cleanuparr
    traefik >> Edge(color="blue", style="dotted") >> converternow
    traefik >> Edge(color="blue", style="dotted") >> immich
    traefik >> Edge(color="blue", style="dotted") >> pterodactyl_panel
    traefik >> Edge(color="blue", style="dotted") >> paperless_ngx
    traefik >> Edge(color="blue", style="dotted") >> vaultwarden
    traefik >> Edge(color="blue", style="dotted") >> littlelink
    traefik >> Edge(color="blue", style="dotted") >> freshrss
    traefik >> Edge(color="blue", style="dotted") >> ghost
    traefik >> Edge(color="blue", style="dotted") >> it_tools
    traefik >> Edge(color="blue", style="dotted") >> jdownloader
    traefik >> Edge(color="blue", style="dotted") >> mkvtoolnix
    traefik >> Edge(color="blue", style="dotted") >> seerr
    traefik >> Edge(color="blue", style="dotted") >> qbittorrent
    traefik >> Edge(color="blue", style="dotted") >> tautulli
    traefik >> Edge(color="blue", style="dotted") >> uptimekuma
    traefik >> Edge(color="blue", style="dotted") >> prometheus
    traefik >> Edge(color="blue", style="dotted") >> grafana

    pterodactyl_panel >> Edge(color="sienna", style="solid") >> w01_pterodactyl_wings
    pterodactyl_panel >> Edge(color="sienna", style="solid") >> w02_pterodactyl_wings

    w01_pterodactyl_wings >> silo_01
    w01_pterodactyl_wings >> new_arcadia
    w02_pterodactyl_wings >> silo_01
    w02_pterodactyl_wings >> test

    qbittorrent >> Edge(color="deepskyblue", style="solid") >> silo_01
    qbittorrent >> Edge(color="deepskyblue", style="solid") >> proton_vpn

    mkvtoolnix >> silo_01
    jdownloader >> silo_01
    polaris_handbrake >> silo_01

    uptimekuma >> Edge(color="forestgreen", style="solid") >> discord
    skyeye_uptimekuma >> Edge(color="forestgreen", style="solid") >> discord

    grafana >> Edge(color="orange", style="bold")  >> loki
    grafana >> Edge(color="orange", style="bold") >> prometheus

    seerr >> Edge(color="magenta1", style="bold") >> sonarr >> Edge(color="turquoise1", style="bold") >> qbittorrent
    seerr >> Edge(color="magenta1", style="bold") >> radarr >> Edge(color="orange1", style="bold") >> qbittorrent
    seerr >> Edge(color="magenta1", style="bold") >> plex
    seerr >> Edge(color="magenta1", style="bold") >> discord

    sonarr >> Edge(color="turquoise1", style="bold") >> silo_01
    sonarr >> Edge(color="turquoise1", style="bold") >> plex
    sonarr >> Edge(color="turquoise1", style="bold") >> jellyfin
    sonarr >> Edge(color="turquoise1", style="bold") >> prowlarr

    radarr  >> Edge(color="orange1", style="bold") >> silo_01
    radarr  >> Edge(color="orange1", style="bold") >> plex
    radarr  >> Edge(color="orange1", style="bold") >> jellyfin
    radarr  >> Edge(color="orange1", style="bold") >> prowlarr

    bazarr >> silo_01

    prowlarr >> flaresolverr

    cleanuparr >> Edge(color="darkviolet", style="bold") >> sonarr
    cleanuparr >> Edge(color="darkviolet", style="bold") >> radarr
    cleanuparr >> Edge(color="darkviolet", style="bold") >> qbittorrent

    bazarr >> Edge(color="black", style="bold") >> sonarr
    bazarr >> Edge(color="black", style="bold") >> radarr

    polaris_portainer >> Edge(color="deeppink", style="solid") >> w01_portainer_agent
    polaris_portainer >> Edge(color="deeppink", style="solid") >> w02_portainer_agent

    metallb >> Edge(color="navyblue", style="dashed") >> plex
    metallb >> Edge(color="navyblue", style="dashed") >> jellyfin
    metallb >> Edge(color="navyblue", style="dashed") >> iperf3
    metallb >> Edge(color="navyblue", style="dashed") >> traefik
    metallb >> Edge(color="navyblue", style="dashed") >> rancher
    metallb >> Edge(color="navyblue", style="dashed") >> openspeedtest

    skyeye_uptimekuma >> gluetun

    skyeye_cftunnel >> Edge(color="#CEA400", style="solid") >> skyeye_uptimekuma
    cftunnel >> Edge(color="#CEA400", style="solid") >> freshrss
    cftunnel >> Edge(color="#CEA400", style="solid") >> seerr
    cftunnel >> Edge(color="#CEA400", style="solid") >> grafana
    cftunnel >> Edge(color="#CEA400", style="solid") >> immich
    cftunnel >> Edge(color="#CEA400", style="solid") >> jellyfin
    cftunnel >> Edge(color="#CEA400", style="solid") >> pterodactyl_panel
    cftunnel >> Edge(color="#CEA400", style="solid") >> littlelink
    cftunnel >> Edge(color="#CEA400", style="solid") >> tautulli

    restic >> Edge(color="yellowgreen", style="bold") >> backblaze
    freshrss >> Edge(color="yellowgreen", style="bold") >> restic
    ghost >> Edge(color="yellowgreen", style="bold") >> restic
    grafana >> Edge(color="yellowgreen", style="bold") >> restic
    immich >> Edge(color="yellowgreen", style="bold") >> restic
    jellyfin >> Edge(color="yellowgreen", style="bold") >> restic
    seerr >> Edge(color="yellowgreen", style="bold") >> restic
    paperless_ngx >> Edge(color="yellowgreen", style="bold") >> restic
    plex >> Edge(color="yellowgreen", style="bold") >> restic
    pterodactyl_panel >> Edge(color="yellowgreen", style="bold") >> restic
    tautulli >> Edge(color="yellowgreen", style="bold") >> restic
    uptimekuma >> Edge(color="yellowgreen", style="bold") >> restic
    vaultwarden >> Edge(color="yellowgreen", style="bold") >> restic

