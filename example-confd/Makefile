######################################################################
# Where is ConfD installed? Make sure CONFD_DIR points it out
CONFD_DIR ?= ../../..

# Include standard ConfD build definitions and rules
include $(CONFD_DIR)/src/confd/build/include.mk

# In case CONFD_DIR is not set (correctly), this rule will trigger
$(CONFD_DIR)/src/confd/build/include.mk:
	@echo 'Where is ConfD installed? Set $$CONFD_DIR to point it out!'
	@echo ''

######################################################################
# Example specific definitions and rules

CONFD_FLAGS = --addloadpath $(CONFD_DIR)/etc/confd 
START_FLAGS ?=

all: ietf-interfaces@2018-02-20.fxs ietf-ip@2018-02-22.fxs \
	ietf-yang-types@2013-07-15.fxs ietf-inet-types@2013-07-15.fxs \
	ietf-routing@2018-03-13.fxs ietf-ipv4-unicast-routing@2018-03-13.fxs \
	ietf-ipv6-unicast-routing@2018-03-13.fxs ietf-mpls@2019-09-11.fxs \
	ietf-mpls-static-extended@2019-09-12.fxs ietf-mpls-static@2019-09-12.fxs \
	ietf-routing-types@2017-12-04.fxs iana-routing-types@2017-12-04.fxs \
	ietf-mpls-ldp@2018-10-22.fxs ietf-mpls-ldp-extended@2018-10-22.yang iana-if-type.fxs \
	$(CDB_DIR) ssh-keydir
	@echo "Build complete"

######################################################################
clean:	iclean
	rm -rf *.trace

######################################################################
start:  stop start_confd 

start_trace:
	$(CONFD) -c confd.conf $(CONFD_FLAGS)	

start_confd:
	$(CONFD) -c confd.conf $(CONFD_FLAGS)

######################################################################
stop:
	$(CONFD) --stop    || true

######################################################################
cli:
	$(CONFD_DIR)/bin/confd_cli --user=admin --groups=admin \
		--interactive || echo Exit

cli-c:
	$(CONFD_DIR)/bin/confd_cli -C --user=admin --groups=admin \
		--interactive  || echo Exit

