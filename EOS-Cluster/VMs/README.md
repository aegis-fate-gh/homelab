In general, if there are two interfaces and you only one the internet to function from one of them, you'll need to delete any other default routes:
ip route del default via 10.1.100.1

If there isn't already a default to the correct gateway, you can add it this way:
ip route add default via 192.168.6.1