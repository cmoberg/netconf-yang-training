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
    with manager.connect(host=host, port=port, username=user, password=password, unknown_host_cb=default_unknown_host_cb) as m1, manager.connect(host=host, port=port+1, username=user, password=password, unknown_host_cb=default_unknown_host_cb) as m2, manager.connect(host=host, port=port+2, username=user, password=password, unknown_host_cb=default_unknown_host_cb) as m3:

        for m in m1, m2, m3:
            print("Asserting the capabilities for %s" % m)
            assert(":candidate" in m.server_capabilities)
            assert(":validate"  in m.server_capabilities)

        with m1.locked(target='candidate') as foo, m2.locked(target='candidate') as bar, m3.locked(target='candidate') as frob:
            for m in m1, m2, m3:
                print("Edit, validate for %s" % m)
                m.discard_changes()
                m.edit_config(config=config_snippet, target="candidate")
                m.validate()

            for m in m1, m2, m3:
                print("Committing confirmed, testing for %s" % m)
                pid = str(m1)
                m.commit(confirmed=True, timeout="10", persist=pid)
                print "Running the tests"

            # Insert service testing here

            for m in m1, m2, m3:
                print("Committing confirmed, testing for %s" % m)
                res = m.commit(confirmed=True)
                print res

if __name__ == '__main__':
    print('The candidate capability is not support on IOS-XE yet!')
    sys.exit()
    demo()