## Automated CentOS libvirt-based install using Ansible

### Process
#### SimpleHTTPServer

1. Starts a python SimpleHTTPServer on the KVM node.  This is to serve kickstart files.

#### virt_install role

1. Finds a CentOS mirror
2. Create kickstart
3. Uses virt_install module to create and start an instance
4. Wait until the instance is in `shutdown` state (the kickstart template is configured to poweroff after installation is complete).

#### virt_ipaddress role
1. Using the qemu guest api determine the DHCP address of the instance
2. Set the `ansible_ssh_host` fact

#### configure_static_ip role
1. Install NetworkManager libraries
2. Add authorized key
3. Retrieve the general connection name from the default interface
4. Use `nmcli` to configure the static ip.
5. If `nmcli` fails:
- Use ifcfg template
- Reload the configuration and restart the device
6. Wait for address change
7. Set the `ansible_ssh_host` fact





Eventually will create ansible module and playbook to do this.
