#Put the below in: /usr/libexec/keepalived/

#!/bin/bash

docker ps -q -f name=jellyfin_jellyfin | grep -q . && exit 0 || exit 1

# And then:
# chmod u=rwx,g=rx,o=rx /usr/libexec/keepalived/jellyfin_check.sh