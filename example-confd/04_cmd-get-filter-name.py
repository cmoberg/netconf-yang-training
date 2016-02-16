#!/bin/env python

import sys, os, warnings, time
from ncclient import manager, operations, xml_

def default_unknown_host_cb(foo, bar):
	return True

filter_snippet = """
<nacm>
  <groups>
    <group>
      <name>admin</name>
    </group>
  </groups>
</nacm>
"""

def demo(host="127.0.0.1", port = 2022, user="admin", password = "admin"):
	with manager.connect(host=host, port=port, username=user, password=password, unknown_host_cb=default_unknown_host_cb) as m:
		res = m.get(("subtree", filter_snippet))
		print xml_.to_xml(res.data_ele, pretty_print=True)

if __name__ == '__main__':
	demo()