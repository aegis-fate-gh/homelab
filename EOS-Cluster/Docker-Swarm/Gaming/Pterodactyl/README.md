Installing on Docker Swarm
1. After deployment, go to the exec command page in Portainer
2. Select /bin/sh
3. Run php artisan p:user:make and follow the prompts

Updating Minecraft with Manual server.jar file when there's a Java change.

1. Check the needed version of Java: https://github.com/pterodactyl/yolks/tree/master/java
2. Update under Nests > Minecraft > Vanilla Minecraft
3. Add a new line under Docker images, like this one: Java 21|ghcr.io/pterodactyl/yolks:java_21

Another option is reinstalling the server after adding the new docker image, also via the UI. But that may overwrite files and hasn't been tested yet.
