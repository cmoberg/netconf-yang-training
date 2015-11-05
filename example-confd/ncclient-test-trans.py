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

def prepare(m):
	m.lock(target="running")
	m.lock(target="candidate")
	m.discard_changes()
	m.edit_config(target="candidate", config = cfg)
	m.validate(source="candidate")

def commit(m):
	res = m.commit(confirmed = True, timeout = "30")

def persist(m):
	res = m.commit()

def demo(devices):
	username = password = "admin"
	for device in devices
	with manager.connect(host=host, port=port, username=user, password=password, unknown_host_cb=_unknown_host_cb) as m1, manager.connect(host=host, port=port + 1, username=user, password=password, unknown_host_cb=_unknown_host_cb) as m2:
		assert(":candidate" in m1.server_capabilities)
		assert(":confirmed-commit" in m1.server_capabilities)
		assert(":candidate" in m2.server_capabilities)
		assert(":confirmed-commit" in m2.server_capabilities)

		try:
			print "Prepare"
			prepare(m1)
			prepare(m2)
		except operations.RPCError, e:
			print "RPC Error", e
		except:
			print "Unexpected error", sys.exc_info()[0]
		else:
			print "Commit"
			commit(m1)
			commit(m2)
		finally:
			print "Persist"
			persist(m1)
			persist(m2)

if __name__ == '__main__':
	devices = {"127.0.0.1": 12022, "127.0.0.1": 12023}
	demo(devices)