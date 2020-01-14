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


all: ietf-interfaces@2014-05-08.fxs ietf-ip@2014-06-16.fxs \
	mpls-ldp.fxs mpls-rsvp.fxs mpls-sr.fxs \
	mpls-types.fxs mpls.fxs iana-if-type.fxs $(CDB_DIR) ssh-keydir
	@echo "Build complete"


######################################################################
clean:	iclean

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

######################################################################
query:
	$(CONFD_DIR)/bin/netconf-console-tcp cmd-get-dhcpd.xml

######################################################################
