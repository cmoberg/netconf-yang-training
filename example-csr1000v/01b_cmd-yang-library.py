#!/bin/env python

from ncclient import manager, operations, xml_
from ncenviron import *

def default_unknown_host_cb(foo, bar):
    return True

filter_snippet = """
<modules-state/>
"""

def demo(host=nc_host, port=nc_port, user=nc_user, password=nc_password):
    with manager.connect(host=host, port=port, username=user, password=password, hostkey_verify=False, look_for_keys=False, allow_agent=False) as m:
        res = m.get(("subtree", filter_snippet))
        print xml_.to_xml(res.data_ele, pretty_print=True)

if __name__ == '__main__':
    demo()

