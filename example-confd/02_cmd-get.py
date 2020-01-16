#!/usr/bin/env python3

from ncclient import manager, xml_
from ncenviron import *

def default_unknown_host_cb(foo, bar):
    return True

def demo(host=nc_host, port=nc_port, user=nc_user, password=nc_password):
    with manager.connect(host=host, port=port, username=user, password=password,
                         hostkey_verify=False, look_for_keys=False, allow_agent=False) as mgr:
        res = mgr.get()
        print(xml_.to_xml(res.data_ele, pretty_print=True))

if __name__ == '__main__':
    demo()
