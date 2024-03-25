DNS is Hosted by PiHoles running Keepalived. As a result, there can be a separation between inside and outside remote proxies.

Internal reverse proxying is handled by traefik, with external Reverse proxying (And any SSL) handled by NPM.

The rationale is pretty simple. Anything external is rarely if ever changed. So to me, it can and probably should stay manual. But internally? That can constantly change...