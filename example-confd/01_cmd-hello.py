#!/bin/env python

import sys, os, warnings, time
from ncclient import manager, operations

def default_unknown_host_cb(foo, bar):
	return True

def demo(host="127.0.0.1", port=2022, user='admin', password='admin'):
	with manager.connect(host=host, port=port, username=user, password=password, hostkey_verify=False) as m:
		for capa in m.server_capabilities:
			print capa

if __name__ == '__main__':
	demo()