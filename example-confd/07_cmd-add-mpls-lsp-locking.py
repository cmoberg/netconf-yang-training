#!/usr/bin/env python3

import sys, os, warnings, time
from ncclient import manager, operations, xml_
from ncenviron import *

def default_unknown_host_cb(foo, bar):
    return True

CONFIG = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <routing xmlns="urn:ietf:params:xml:ns:yang:ietf-routing">
    <mpls xmlns="urn:ietf:params:xml:ns:yang:ietf-mpls">
      <static-lsps xmlns="urn:ietf:params:xml:ns:yang:ietf-mpls-static">
        <static-lsp>
          <name>lsp0</name>
          <in-segment>
            <fec>
              <incoming-label>100</incoming-label>
            </fec>
          </in-segment>
          <out-segment>
            <nhlfe-single>
              <outgoing-interface>eth0</outgoing-interface>
            </nhlfe-single>
          </out-segment>
        </static-lsp>
      </static-lsps>
    </mpls>
  </routing>
</config>
"""

def demo(host=nc_host, port=nc_port, user=nc_user, password=nc_password):
    with manager.connect(host=host, port=port, username=user, password=password,
                         hostkey_verify=False, look_for_keys=False, allow_agent=False) as mgr:
        assert ':candidate' in mgr.server_capabilities
        with mgr.locked(target='candidate'):
            mgr.discard_changes()
            mgr.edit_config(config=CONFIG, target="candidate")
            res = mgr.commit()
            print(res)

if __name__ == '__main__':
    demo()
