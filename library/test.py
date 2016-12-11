#!/usr/bin/env python

import sys
sys.path.append('/usr/share/virt-manager/')
sys.path.append('/usr/share/virt-manager/virtinst/')
#import virt-install

import imp
import argparse
#import sys

def main():
    #sys.path.append('/usr/share/virt-manager/')
    vi = imp.load_source('virt-install', '/usr/share/virt-manager/virt-install')
    #execfile('/usr/share/virt-manager/virt-install')
    options = argparse.Namespace()
#    print vi
#    print sys.modules.keys()


if __name__ == '__main__':
    main()
