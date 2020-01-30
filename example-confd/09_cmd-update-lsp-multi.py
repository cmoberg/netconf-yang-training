#!/usr/bin/env python3

import sys
import pprint
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
    devices = [
        {"name": "dev1", "ip": "127.0.0.1", "port": "2022"},
        {"name": "dev2", "ip": "127.0.0.1", "port": "2024"},
        {"name": "dev3", "ip": "127.0.0.1", "port": "2026"},
    ]

    mdev = {}

    for device in devices:
      name = device["name"]
      print("Connecting to:",  name)

      with manager.connect(host=host, port=port, username=user, password=password,
                        hostkey_verify=False, look_for_keys=False, allow_agent=False) as mdev[name]:
        print("Connected to:",  name)

    pprint.pprint(mdev)


    for dev in mdev:
        print("Asserting the :candidate and :validate capabilities for %s" % mdev[dev])
        # Switch to if-clauses
        assert ':candidate' in mdev[dev].server_capabilities
        assert ':validate'  in mdev[dev].server_capabilities

    for dev in mdev:
        print("Locking device %s" % mdev[dev])
        with mdev[dev].locked(target='candidate') as mdev[dev]["locked"]:
            pass
    sys.exit()

    with m1.locked(target='candidate') as foo, m2.locked(target='candidate') as bar, m3.locked(target='candidate') as frob:
        for m in m1, m2, m3:
            print("Edit, validate for %s" % m)
            m.discard_changes()
            m.edit_config(config=CONFIG, target="candidate")
            m.validate()

        for m in m1, m2, m3:
            print("Committing confirmed, testing for %s" % m)
            pid = str(m1)
            m.commit(confirmed=True, timeout="10", persist=pid)
            print("Running the tests")

        # Insert service testing here

        for m in m1, m2, m3:
            print("Committing confirmed, testing for %s" % m)
            res = m.commit(confirmed=True)
            print(res)

if __name__ == '__main__':
    demo()