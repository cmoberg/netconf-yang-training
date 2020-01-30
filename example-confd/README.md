# Running the examples using the ConfD NETCONF server

This directory contains a set of python scripts to exercise basic NETCONF operations towards a ConfD-based environment. At the time of writing, this works well for me using ConfD 7.3 downloaded from the [Tail-f website](http://www.tail-f.com/confd-basic/). Your mileage may vary.

# Setting up ConfD

There is a `Makefile` in this directory should help you with the lifecycle of the examples. It provides targets to build the configuration for ConfD (`all`), to start and stop ConfD (`start`, `stop`) and also to reset the examples (`clean`).

The Makefile that you have the ConfD environment variables setup, so make sure to source the `confdrc` file from the ConfD installation before you build and start the example.

Now, feel free to work through the numbered python examples, and make sure that you use the right IP address and credentials in `ncenviron.py`.