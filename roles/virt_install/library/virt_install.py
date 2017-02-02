#!/usr/bin/env python

import sys
sys.path.append('/usr/share/virt-manager/')
sys.path.append('/usr/share/virt-manager/virtinst/')

import time
import atexit
import imp
import libvirt
import virtinst
from virtinst import cli
from virtinst.cli import fail, print_stdout, print_stderr
import argparse

EXAMPLES = '''
    - name: virt-install CentOS
      virt_install:
        name: om1
        vcpus: 2
        memory: 4096
        disks:
          - 'path=/instances/om1.qcow2,size=64'
        networks:
          - 'network=ovsbr0,portgroup=vlan-252'
        extra_args:
          - 'ks=http://10.53.252.110:8000/ks.cfg ip=dhcp console=ttyS0,115200n8 serial'
        location: 'http://centos.mbni.med.umich.edu/mirror/7.2.1511/os/x86_64/'
'''

# This module is exiting somewhere without module.exit_json
def onexit(module):
    time.sleep(5)
    module.exit_json(changed=True, msg="This is the wrong way to exit" )


def createoptions():

    argument_spec = dict(name=dict(required=True, type='str'),
                         vcpus=dict(required=True, type='str'),
                         memory=dict(required=True, type='int'),
                         disks=dict(required=True, type='list'),
                         networks=dict(required=True, type='list'),
                         extra_args=dict(required=False, default=None, type='list'),
                         location=dict(required=False, default=None, type='str'),
                         os_variant=dict(required=False, default=None, type='str'),
                         wait=dict(required=False, default=None, type='int'),
                         import_install=dict(required=False, default=False, type='bool'))


    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)
#wait=module.params['wait'], 
#graphics=['none'], 

    if not (module.params['extra_args'] is None):
        if len(module.params['extra_args']) == 0:
            module.params['extra_args'] = None



    options = argparse.Namespace(accelerate=False, arch=None, autoconsole=False, autostart=False, blkiotune=None, boot=None,
                       bridge=None,
                       cdrom=None, cdrom_short=None, channel=None, check=None, check_cpu=False, clock=None,
                       connect=None,
                       console=['pty,target_type=serial'], container=False, controller=None, cpu=None, cpuset=None,
                       debug=False,
                       description=None, disk=module.params['disks'], disksize=None, distro_type=None,
                       distro_variant=None, dry=False, events=None,
                       extra_args=module.params['extra_args'],
                       features=None,
                       file_paths=None, filesystem=None, force=False, fullvirt=False, graphics=['none'], hostdev=None,
                       hv_type='', idmap=None, import_install=module.params['import_install'], init=None, initrd_inject=None, input=None,
                       keymap=None,
                       livecd=False, location=module.params['location'], mac=None,
                       machine=None, memballoon=None, memory=None, memorybacking=None, memtune=None, metadata=None,
                       name=module.params['name'],
                       network=module.params['networks'], noacpi=False, noapic=False, nodisks=False,
                       nographics=False, nonetworks=False, noreboot=True, numatune=None, oldmemory=module.params['memory'], panic=None,
                       parallel=None, paravirt=False, pm=None, prompt=False, pxe=False, quiet=True, redirdev=None,
                       resource=None,
                       rng=None, sdl=False, security=None, serial=None, smartcard=None, sound=None, sparse=True,
                       test_media_detection=None, tpm=None, transient=False, uuid=None, vcpus=module.params['vcpus'], video=None,
                       vnc=False,
                       vnclisten=None, vncport=None, wait=None, watchdog=None, xmlonly=False, xmlstep=None)

#    options = argparse.Namespace(accelerate=False, arch=None, 
#            autoconsole=False, autostart=False, blkiotune=None, boot=None,
#            bridge=None, cdrom=None, cdrom_short=None, channel=None, 
#            check=None, check_cpu=False, clock=None,
#            connect=None,
#            console=['pty,target_type=serial'], 
#            container=False, controller=None, cpu=None, cpuset=None, debug=False,
#            description=None, 
#            disk=module.params['disks'], 
#            disksize=None, 
#            distro_type=None,
#            distro_variant=None, 
#            #distro_variant=module.params['os_variant'], 
#            dry=False, events=None,
#            extra_args=module.params['extra_args'],
#            features=None, file_paths=None, filesystem=None, force=False, 
#            fullvirt=False, 
#            graphics=None,  <-----*****
#            hostdev=None, hv_type='', idmap=None, 
#            import_install=module.params['import_install'], 
#            init=None, initrd_inject=None, input=None, keymap=None, livecd=False, 
#            location=module.params['location'], 
#            mac=None, machine=None, memballoon=None, memory=None, 
#            memorybacking=None, memtune=None, metadata=None,
#            name=module.params['name'],
#            network=module.params['networks'], 
#            noacpi=False, noapic=False, nodisks=False, nographics=False, 
#            nonetworks=False, noreboot=True, numatune=None, 
#            oldmemory=module.params['memory'],
#            panic=None, parallel=None, paravirt=False, pm=None, prompt=False, 
#            pxe=False, quiet=True, redirdev=None, resource=None, rng=None, 
#            sdl=False, security=None, serial=None, smartcard=None, sound=None, 
#            sparse=True, test_media_detection=None, tpm=None, transient=False, 
#            uuid=None, 
#            vcpus=module.params['vcpus'], 
#            video=None, vnc=False, vnclisten=None, vncport=None, 
#            wait=None, 
#            watchdog=None, xmlonly=False, xmlstep=None)

    atexit.register(onexit, module)
    return options, module

# Using all the code from main() 
# https://github.com/virt-manager/virt-manager/blob/master/virt-install
# Added function to support ansible

def main(conn=None):
    try:
        sys.path.append('/usr/share/virt-manager/')
        vi = imp.load_source('virt-install', '/usr/share/virt-manager/virt-install')
    
        cli.earlyLogging()
        options, module = createoptions()
    
        vi.convert_old_printxml(options)
    
        # Default setup options
        options.quiet = (options.xmlonly or
                         options.test_media_detection or options.quiet)
    
        cli.setupLogging("virt-install", options.debug, options.quiet)
    
        vi.check_cdrom_option_error(options)
    
        cli.convert_old_force(options)
        cli.parse_check(options.check)
        cli.set_prompt(options.prompt)
    
        if cli.check_option_introspection(options):
            module.exit_json(changed=True)
    
        if conn is None:
            conn = cli.getConnection(options.connect)
    
        if options.test_media_detection:
            vi.do_test_media_detection(conn, options.test_media_detection)
            module.exit_json(changed=True)

        guest = vi.build_guest_instance(conn, options)
        time.sleep(5)
        if options.xmlonly or options.dry:
            xml = vi.xml_to_print(guest, options.xmlonly, options.dry)
            if xml:
                print_stdout(xml, do_force=True)
        else:
            vi.start_install(guest, options)
        
        module.exit_json(changed=True)
    except Exception:
        module.fail_json(msg='Exception')
        #module.fail_json(msg='Exception', value=str(value), traceback=str(traceback))


from ansible.module_utils.basic import *


if __name__ == '__main__':
    main()
