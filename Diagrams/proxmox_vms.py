from diagrams import Diagram, Cluster, Edge
from diagrams.onprem import proxmox
from diagrams.generic import os, storage
from diagrams.custom import Custom

with Diagram("Homelab VMs", show=False, direction="TB"):
    with Cluster("Proxmox HA Cluster"):
        cephfs = storage.Storage("CephFS")
        ceph = storage.Storage("Ceph")

        with Cluster("pve-selene-01"):
            with Cluster("Local ZFS Storage"):
                pihole1 = os.Ubuntu("pihole-01")
                dsm1 = os.Ubuntu("dsp-man-01")
                dsw_gpu1 = os.Ubuntu("dsp-w-gpu-01")
                dsw_vpn1 = os.Ubuntu("dsp-w-vpn-01")

            with Cluster("Ceph Cluster Storage"):
                w11_SB = os.Windows("Server Bridge")

        with Cluster("pve-selene-02"):
            with Cluster("Local ZFS Storage"):
                pihole2 = os.Ubuntu("pihole-02")
                dsm2 = os.Ubuntu("dsp-man-02")
                dsw_gpu2 = os.Ubuntu("dsp-w-gpu-02")
                dsw_vpn2 = os.Ubuntu("dsp-w-vpn-02")
            
            with Cluster("Ceph Cluster Storage"):
                w11_MB = os.Windows("Management Bridge")

        with Cluster("pve-selene-03"):
            with Cluster("Local ZFS Storage"):
                pihole3 = os.Ubuntu("pihole-03")
                dsm3 = os.Ubuntu("dsp-man-03")
                dsw_gpu3 = os.Ubuntu("dsp-w-gpu-03")
            
            with Cluster("Ceph Cluster Storage"):
                w11_GP = os.Windows("GP / Remote Access")
                docker1 = os.Ubuntu("ptero-wings-01")
            
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

    w11_GP << ceph
    w11_MB << ceph
    w11_SB << ceph
    docker1 << ceph

    ceph >> cephfs >> ceph
    ceph_stage >> cephfs_stage >> ceph_stage


