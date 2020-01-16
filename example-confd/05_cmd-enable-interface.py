#!/usr/bin/env python3

from ncclient import manager
from ncenviron import *

def default_unknown_host_cb(foo, bar):
    return True

CONFIG = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>eth0</name>
      <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
      <enabled>true</enabled>
    </interface>
  </interfaces>
</config>
"""

def demo(host=nc_host, port=nc_port, user=nc_user, password=nc_password):
    with manager.connect(host=host, port=port, username=user, password=password,
                         hostkey_verify=False, look_for_keys=False, allow_agent=False) as mgr:
        res = mgr.edit_config(config=CONFIG, target="running")
        print(res)

if __name__ == '__main__':
    demo()

