#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2016, Joseph Callen <jcpowermac () gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

try:
    import os
    import SimpleHTTPServer
    import SocketServer
    import signal
    HAS_PKGS = True
except:
    HAS_PKGS = False

#def signal_handler(signal, frame):


def main():

    argument_spec = dict(port=dict(required=False, default=8000, type='int'),
                         path=dict(required=True, type='str'))

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)
    os.chdir(module.params['path'])
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", module.params['port']), Handler)

    httpd.serve_forever()
    module.exit_json(changed=False)   



from ansible.module_utils.basic import *


if __name__ == '__main__':
    main()
