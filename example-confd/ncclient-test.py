#!/bin/env python

import sys, os, warnings, time
from ncclient import manager, operations

cfg = """
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

def _unknown_host_cb(frib, frob):
	return True

def demo(host="127.0.0.1", port = 2022, user="admin", password = "admin"):
	with manager.connect(host=host, port=port, username=user, password=password, unknown_host_cb=_unknown_host_cb) as m1, manager.connect(host=host, port=port + 1, username=user, password=password, unknown_host_cb=_unknown_host_cb) as m2:
		assert(":candidate" in m.server_capabilities)
		assert(":confirmed-commit" in m.server_capabilities)

		with m.locked(target="candidate") and m.locked(target="running"):
			try:
				res = m.discard_changes()
				res = m.edit_config(target="candidate", config = cfg)
				res = m.validate(source="candidate")
				res = m.commit(confirmed = True, timeout = "30")
				res = m.commit()
			except operations.RPCError, e:
				print "RPC Error", e
			except:
				print "Unexpected error", sys.exc_info()[0]
			else:
				print "Success"				

if __name__ == '__main__':
	demo()