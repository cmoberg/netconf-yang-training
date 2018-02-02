# Running the examples on the Cisco CSR1000v

This directory contains a set of python scripts to exercise basic NETCONF operations towards a NETCONF server running on the csr1000v. At the time of writing, this works well for me using VMWare Fusion 10.1.1 to run an image called `csr1000v-universalk9.16.06.02` downloaded from [software.cisco.com](http://software.cisco.com). Your mileage may vary.

Since IOS-XE does not (yet) support the `:candidate` capability for NETCONF, exercise `07_cmd-add-mpls-lsp-locking.py` and later will exit without running anything until this is fixed.

There are also a couple of exercises based on the `netconf-console` script further down in this file.

# Setting up for NETCONF and RESTCONF

The first thing to do is to configure the NETCONF and RESTCONF services in the router. The following commands enables the YANG-based NETCONF implementation and starts the RESTCONF server. Feel free to use another username and password, but remember to update the content of `ncenviron.py`.

```
Router> enable
Router# configure terminal
Router# restconf
Router# netconf-yang
Router# username netconf privilege 15 password 0 netconf
Router# aaa new-model
Router# aaa authorization exec default local
Router# exit
```

Now, feel free to work through the numbered python examples, and make sure that you use the right IP address and credentials in `ncenviron.py`.

# Some basic exercises using the 'netconf-console' script

The following describes a number of activities you can do using the `netconf-console` script to perform some basic NETCONF activities including fetching and viewing YANG modules.

The first step is to connect to the NETCONF server and perform the basic hello-exchange. You obviously need to exchange the IP address below for the IP address of the router you are working with. Use the 'show ip int bri' to find out the IP address of the interfaces.

```
$ netconf-console --port=830 --host=192.168.1.126 -u netconf -p netconf --hello
<?xml version="1.0" encoding="UTF-8"?>
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <capabilities>
    <capability>urn:ietf:params:netconf:base:1.0</capability>
    <capability>urn:ietf:params:netconf:base:1.1</capability>
    <capability>urn:ietf:params:netconf:capability:writable-running:1.0</capability>
    <capability>urn:ietf:params:netconf:capability:xpath:1.0</capability>
[...]
```

Now we want to start looking at the modules supported and how they are related to each other. The first thing is to look through the extensive list of modules supported and look for one name `ietf-ip`.

```
$ netconf-console --port=830 --host=192.168.1.126 -u netconf -p netconf --hello | grep ietf-ip
```

Aha, we found one called `ietf-ip`, let's fetch it and look for any `import` statements that would tell us that this module requires additional modules to produce a complete tree.

```
$ netconf-console --port=830 --host=192.168.1.126 -u netconf -p netconf --get-schema=ietf-ip | grep import
 import ietf-interfaces {
 import ietf-inet-types {
 import ietf-yang-types {
```

Now we know that `ietf-ip` requires three modules, we can fetch all of them onto local disk using the `--get-schema` option. The reason we're using the xpath-expression filter here is that we need to pick out the payload content (the YANG module) from the NETCONF XML RPC content.

```
$ mkdir yangfiles
$ cd yangfiles/
$ netconf-console --port=830 --host=192.168.1.126 -u netconf -p netconf --get-schema=ietf-ip | xpath  "/rpc-reply/data/text()" > ietf-ip.yang
$ netconf-console --port=830 --host=192.168.1.126 -u netconf -p netconf --get-schema=ietf-interfaces | xpath  "/rpc-reply/data/text()" > ietf-interfaces.yang
$ netconf-console --port=830 --host=192.168.1.126 -u netconf -p netconf --get-schema=ietf-inet-types | xpath  "/rpc-reply/data/text()" > ietf-inet-types.yang
$ netconf-console --port=830 --host=192.168.1.126 -u netconf -p netconf --get-schema=ietf-yang-types | xpath  "/rpc-reply/data/text()" > ietf-yang-types.yang
```

Now that we have all the YANG modules in the local directory we can start looking at them using the `pyang` tool. We will be looking at the text-based tree rendering of the content by using the `-f tree` option.

```
$ pyang -f tree ietf-interfaces.yang
$ pyang -f tree ietf-ip.yang
$ pyang -f tree ietf-interfaces.yang ietf-ip.yang
```

Please note that the last incantation shows both modules at the same time, creating the augmented tree where `ietf-ip` augments IP-based parameters onto the basic `ietf-interfaces`data structure.

We can also create an HTML rendering of the content of the tree for easy reading by using the `-f jstree` option.

```
$ pyang -f jstree ietf-interfaces.yang ietf-ip.yang
```

