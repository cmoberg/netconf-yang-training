#!/bin/env python

import sys, os, warnings, time
from ncclient import manager, operations, xml_

def default_unknown_host_cb(foo, bar):
	return True

config_snippet = """
<config>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>eth0</name>
      <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
      <enabled>true</enabled>
    </interface>
  </interfaces>
</config>
"""

def demo(host="127.0.0.1", port = 2022, user="admin", password = "admin"):
	with manager.connect(host=host, port=port, username=user, password=password, unknown_host_cb=default_unknown_host_cb) as m:
		res = m.edit_config(config=config_snippet, target="running")
		print res.xml

if __name__ == '__main__':
	demo()