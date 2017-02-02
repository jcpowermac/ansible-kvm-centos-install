#!/usr/bin/python

try:
    import libvirt
    LIBVIRT = True
except:
    LIBVIRT = False
    pass


def main():
    
    argument_spec = dict(src=dict(required=True, type='str'),
            dest=dict(required=True, type='str'),
            disks=dict(required=True, type='list'),
            networks=dict(required=False, default=None, type='list'))

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)




from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
