#!/bin/env python

import sys, os, warnings, time
from ncclient import manager, operations, xml_
from ncenviron import *

def default_unknown_host_cb(foo, bar):
	return True

config_snippet = """
<config>
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
    with manager.connect(host=host, port=port, username=user, password=password, hostkey_verify=False, look_for_keys=False, allow_agent=False) as m:
		assert(":candidate" in m.server_capabilities)
		m.discard_changes()
		m.edit_config(config=config_snippet, target="candidate")
		res = m.commit()
		print res

if __name__ == '__main__':
	demo()