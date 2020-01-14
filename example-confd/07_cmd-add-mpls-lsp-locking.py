#!/bin/env python

import sys, os, warnings, time
from ncclient import manager, operations, xml_
from ncenviron import *

def default_unknown_host_cb(foo, bar):
    return True

FILTER = """
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
    with manager.connect(host=host, port=port, username=user, password=password,
                         hostkey_verify=False, look_for_keys=False, allow_agent=False) as mgr:
        assert ':candidate' in mgr.server_capabilities
        with mgr.locked(target='candidate'):
            mgr.discard_changes()
            mgr.edit_config(config=FILTER, target="candidate")
            res = mgr.commit()
            print res

if __name__ == '__main__':
    demo()
