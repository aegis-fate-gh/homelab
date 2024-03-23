First Node
vrrp_instance VRRP1 {
    state MASTER
#   Specify the network interface to which the virtual address is assigned
    interface ens18
#   The virtual router ID must be unique to each VRRP instance that you define
    virtual_router_id 40
#   Set the value of priority higher on the master server than on a backup server
    priority 200
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass Insert password here
    }
    virtual_ipaddress {
        192.168.6.3/24
    }
}

vrrp_instance VRRP2 {
    state BACKUP
#   Specify the network interface to which the virtual address is assigned
    interface ens18
#   The virtual router ID must be unique to each VRRP instance that you define
    virtual_router_id 41
#   Set the value of priority higher on the master server than on a backup server
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass Insert password here
    }
    virtual_ipaddress {
        192.168.6.4/24
    }
}

vrrp_instance VRRP3 {
    state BACKUP
#   Specify the network interface to which the virtual address is assigned
    interface ens18
#   The virtual router ID must be unique to each VRRP instance that you define
    virtual_router_id 42
#   Set the value of priority higher on the master server than on a backup server
    priority 50
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass Insert password here
    }
    virtual_ipaddress {
        192.168.6.5/24
    }
}



Second Node:
vrrp_instance VRRP1 {
    state BACKUP
#   Specify the network interface to which the virtual address is assigned
    interface ens18
#   The virtual router ID must be unique to each VRRP instance that you define
    virtual_router_id 40
#   Set the value of priority higher on the master server than on a backup server
    priority 50
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass Insert password here
    }
    virtual_ipaddress {
        192.168.6.3/24
    }
}

vrrp_instance VRRP2 {
    state MASTER
#   Specify the network interface to which the virtual address is assigned
    interface ens18
#   The virtual router ID must be unique to each VRRP instance that you define
    virtual_router_id 41
#   Set the value of priority higher on the master server than on a backup server
    priority 200
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass Insert password here
    }
    virtual_ipaddress {
        192.168.6.4/24
    }
}

vrrp_instance VRRP3 {
    state BACKUP
#   Specify the network interface to which the virtual address is assigned
    interface ens18
#   The virtual router ID must be unique to each VRRP instance that you define
    virtual_router_id 42
#   Set the value of priority higher on the master server than on a backup server
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass Insert password here
    }
    virtual_ipaddress {
        192.168.6.5/24
    }
}



Third Node:
vrrp_instance VRRP1 {
    state BACKUP
#   Specify the network interface to which the virtual address is assigned
    interface ens18
#   The virtual router ID must be unique to each VRRP instance that you define
    virtual_router_id 40
#   Set the value of priority higher on the master server than on a backup server
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass Insert password here
    }
    virtual_ipaddress {
        192.168.6.3/24
    }
}

vrrp_instance VRRP2 {
    state BACKUP
#   Specify the network interface to which the virtual address is assigned
    interface ens18
#   The virtual router ID must be unique to each VRRP instance that you define
    virtual_router_id 41
#   Set the value of priority higher on the master server than on a backup server
    priority 50
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass Insert password here
    }
    virtual_ipaddress {
        192.168.6.4/24
    }
}

vrrp_instance VRRP3 {
    state MASTER
#   Specify the network interface to which the virtual address is assigned
    interface ens18
#   The virtual router ID must be unique to each VRRP instance that you define
    virtual_router_id 42
#   Set the value of priority higher on the master server than on a backup server
    priority 200
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass Insert password here
    }
    virtual_ipaddress {
        192.168.6.5/24
    }
}