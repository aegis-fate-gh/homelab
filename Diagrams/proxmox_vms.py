from diagrams import Diagram, Cluster, Edge
from diagrams.onprem import proxmox
from diagrams.generic import os, storage
from diagrams.custom import Custom

with Diagram("Homelab VMs", show=False, direction="TB"):
    with Cluster("Eos Proxmox HA Cluster"):
        cephfs = storage.Storage("CephFS")
        ceph = storage.Storage("Ceph")

        with Cluster("pve-eos-01"):
            with Cluster("Local ZFS Storage"):
                dsm1 = os.Ubuntu("Starbase-01")
                dsw_gpu1 = os.Ubuntu("Sovereign-01")
                dsw_vpn1 = os.Ubuntu("Defiant-01")

            with Cluster("Ceph Cluster Storage"):
                wing_commander = os.Ubuntu("Wing-Commander")

        with Cluster("pve-eos-02"):
            with Cluster("Local ZFS Storage"):
                dsm2 = os.Ubuntu("Starbase-02")
                dsw_gpu2 = os.Ubuntu("Sovereign-02")
                dsw_vpn2 = os.Ubuntu("Defiant-02")
            
            with Cluster("Ceph Cluster Storage"):
                w11_MB = os.Windows("Golden-Gate")

        with Cluster("pve-eos-03"):
            with Cluster("Local ZFS Storage"):
                dsm3 = os.Ubuntu("Starbase-03")
                dsw_gpu3 = os.Ubuntu("Sovereign-03")
            
            with Cluster("Ceph Cluster Storage"):
                docker1 = os.Ubuntu("Jurassic-Park-01")
            
    with Cluster("pve-andromeda"):
        with Cluster("Local ZFS Storage"):
            pihole_staging = os.Ubuntu("pihole-stage-01")
            
            with Cluster("Staging HA Cluster"):
                cephfs_stage = storage.Storage("CephFS")
                ceph_stage = storage.Storage("Ceph")

                with Cluster("pve-stage-01"):
                    dsms1 = os.Ubuntu("dss-man-01")
                    dsws1 = os.Ubuntu("dss-w-01")

                with Cluster("pve-stage-02"):
                    dsms2 = os.Ubuntu("dss-man-02")
                    dsws2 = os.Ubuntu("dss-w-02")

                with Cluster("pve-stage-03"):
                    dsms3 = os.Ubuntu("dss-man-03")
                    dsws3 = os.Ubuntu("dss-w-03")

    with Cluster("pve-aegis"):
        pbs = proxmox.Pve("Proxmox Backup Server")

    dsm1 << cephfs
    dsm2 << cephfs
    dsm3 << cephfs

    dsms1 << cephfs_stage
    dsms2 << cephfs_stage
    dsms3 << cephfs_stage

    dsws1 << cephfs_stage
    dsws2 << cephfs_stage
    dsws3 << cephfs_stage

    dsw_gpu1 << cephfs
    dsw_gpu2 << cephfs
    dsw_gpu3 << cephfs
    dsw_vpn1 << cephfs
    dsw_vpn2 << cephfs
    docker1 << cephfs

    w11_MB << ceph
    docker1 << ceph
    wing_commander << ceph

    ceph >> cephfs >> ceph
    ceph_stage >> cephfs_stage >> ceph_stage


