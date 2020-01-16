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
      <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
          <ip>2001:db8:c18:1::3</ip>
          <prefix-length>128</prefix-length>
        </address>
      </ipv6>
    </interface>
  </interfaces>
</config>
"""

def demo(host=nc_host, port=nc_port, user=nc_user, password=nc_password):
    with manager.connect(host=host, port=port, username=user, password=password,
                         hostkey_verify=False, look_for_keys=False, allow_agent=False) as mgr:
        assert ':candidate' in mgr.server_capabilities
        mgr.discard_changes()
        mgr.edit_config(config=CONFIG, target="candidate")
        res = mgr.commit()
        print(res)

if __name__ == '__main__':
    demo()
