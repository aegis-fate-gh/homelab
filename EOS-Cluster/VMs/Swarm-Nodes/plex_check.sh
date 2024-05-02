#Put the below in: /usr/libexec/keepalived/

#!/bin/bash

docker ps -q -f name=plex_plex | grep -q . && exit 0 || exit 1

# And then:
# chmod u=rwx,g=rx,o=rx /usr/libexec/keepalived/plex_check.sh