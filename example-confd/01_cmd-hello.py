#!/bin/env python

import sys, os, warnings, time
from ncclient import manager, operations

def _unknown_host_cb(foo, bar):
	return True

def demo(host="127.0.0.1", port = 2022, user="admin", password = "admin"):
	with manager.connect(host=host, port=port, username=user, password=password, unknown_host_cb=_unknown_host_cb) as m:
		print m.__dict__
		for capa in m.server_capabilities:
			print capa

if __name__ == '__main__':
	demo()