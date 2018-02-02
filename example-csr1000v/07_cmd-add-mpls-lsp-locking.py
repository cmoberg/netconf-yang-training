#!/bin/env python

import sys
from ncclient import manager, operations, xml_
from ncenviron import *

def default_unknown_host_cb(foo, bar):
    return True

config_snippet = """
<config>
  <mpls xmlns="http://openconfig.net/yang/mpls">
    <lsps>
      <static-lsps>
        <label-switched-path>
          <name>lsp0</name>
          <ingress>
            <incoming-label>100</incoming-label>
          </ingress>
          <egress>
            <next-hop>2001:db8:c18:1::3</next-hop>
          </egress>
        </label-switched-path>
      </static-lsps>
    </lsps>
  </mpls>
</config>
"""

def demo(host=nc_host, port=nc_port, user=nc_user, password=nc_password):
    with manager.connect(host=host, port=port, username=user, password=password, hostkey_verify=False, look_for_keys=False, allow_agent=False) as m:
        assert(":candidate" in m.server_capabilities)
        with m.locked(target='candidate'):
            m.discard_changes()
            m.edit_config(config=config_snippet, target="candidate")
            res = m.commit()
            print res

if __name__ == '__main__':
    print('The candidate capability is not support on IOS-XE yet!')
    sys.exit()
    demo()