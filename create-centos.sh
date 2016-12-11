#!/bin/bash
NAME="om1"
DOMAIN="virtomation.com"


python -m SimpleHTTPServer 8000 &




virt-install --name ${NAME} --ram 4096 --disk path=/instances/${NAME}.qcow2,size=64 --vcpus 2 --network network=ovsbr0,portgroup=vlan-252 --graphics none --console pty,target_type=serial --location 'http://centos.mbni.med.umich.edu/mirror/7.2.1511/os/x86_64/' --extra-args 'ks=http://10.53.252.110:8000/ks.cfg ip=dhcp console=ttyS0,115200n8 serial'
