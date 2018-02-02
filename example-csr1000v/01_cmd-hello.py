#!/bin/env python

from ncclient import manager, operations
from ncenviron import *

def default_unknown_host_cb(foo, bar):
    return True

def demo(host=nc_host, port=nc_port, user=nc_user, password=nc_password):
    with manager.connect(host=host, port=port, username=user, password=password,
                         hostkey_verify=False, look_for_keys=False, allow_agent=False) as mgr:
        for capa in mgr.server_capabilities:
            print capa

if __name__ == '__main__':
    demo()
