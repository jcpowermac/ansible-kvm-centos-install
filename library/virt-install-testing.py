#!/usr/bin/env python

import argparse
import logging
import os
import re
import sys
import time

import libvirt

import virtinst
from virtinst import cli
from virtinst.cli import fail, print_stdout, print_stderr

'''
- name: virt-install
  virtinstall:
    name: foo
    ram: 4096
    vcpus: 2
    disk:  # dictionary?
      path: /instances/foo.qcow2
      size: 64
    network: #dictionary?
      network: ovsbr0
      portgroup: vlan252
    graphics: none
    console: pty
      target: serial
    extra-args: # string?
'''



#virt-install --name ${NAME} --ram 4096 
#--disk path=/instances/${NAME}.qcow2,size=64 --vcpus 2 
#--network network=ovsbr0,portgroup=vlan-252 --graphics none 
--console pty,target_type=serial 
#--location 'http://centos.mbni.med.umich.edu/mirror/7.2.1511/os/x86_64/' 
#--extra-args 'ks=http://10.53.252.110:8000/ks.cfg ip=dhcp console=ttyS0,115200n8 serial'





