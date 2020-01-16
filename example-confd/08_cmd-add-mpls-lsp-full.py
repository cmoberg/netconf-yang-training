#!/usr/bin/env python3

import time
from ncclient import manager, xml_
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
        # Persist-id for the confirmed commit
        pid = "IQ,d4668"
        assert ':candidate' in mgr.server_capabilities
        assert ':validate'  in mgr.server_capabilities
        with mgr.locked(target='candidate'):
            mgr.discard_changes()
            print("Editing config")
            mgr.edit_config(config=CONFIG, target="candidate")
            mgr.validate()
            mgr.commit(confirmed=True, timeout="10", persist=pid)
            print ("Running the tests (5s)")
            time.sleep(5)
            # Could cancel the commit during the timeout
            # res = mgr.cancel_commit(persist_id=pid)
            print("Committing")
            res = mgr.commit(confirmed=True)
            print(res)

if __name__ == '__main__':
    demo()
