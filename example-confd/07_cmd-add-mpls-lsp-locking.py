#!/bin/env python

import sys, os, warnings, time
from ncclient import manager, operations, xml_

import logging

log = logging.getLogger(__name__)

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

def demo(host="127.0.0.1", port = 2022, user="admin", password = "admin"):
	# logging.basicConfig(level=logging.DEBUG)

	with manager.connect(host=host, port=port, username=user, password=password, unknown_host_cb=default_unknown_host_cb) as m:
		assert(":candidate" in m.server_capabilities)
		with m.locked(target='candidate'):
			m.discard_changes()
			m.edit_config(config=config_snippet, target="candidate")
			res = m.commit()

if __name__ == '__main__':
	demo()