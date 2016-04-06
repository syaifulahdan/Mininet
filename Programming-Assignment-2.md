##### Programming Assignment 2: Using Mininet and Mininet Python API: Instructions

In this exercise, you will be learning how to build custom topologies using Mininet Python API and how certain parameters like bandwidth, delay, loss and queue size can be set individually
for different links in the topology. You’ll also learn how to do performance testing of these custom topologies using ping and iperf.
After the overview, you will be asked to create and submit your own custom topology based on the most common 3-tier Datacenter architecture i.e., core, aggregation and edge. More details
on creating and submitting the code will be provided later on in the instructions. So, make sure that you follow each step carefully.

Overview

The network you'll use in this exercise includes hosts and switches connected in a linear
topology, as shown in the figure below.

<img src="https://github.com/syaifulahdan/mininet/blob/master/image/linier_topology.png" width="400" height="400" align="center" title="syaifulahdan/mininet" />

<b>Creating Topology </b>
Mininet supports parametrized topologies. With a few lines of Python code, you can create a flexible topology which can be configured based on the parameters you pass into it, and reused for multiple experiments. For example, here is a simple network topology (based on Figure 1) which consists of a specified number of hosts (h1 through hN) connected to their individual switches (s1 through sN):

<b>Linear Topology (without Performance Settings)</b>
<pre>
#!/usr/bin/python
from
from
from
from
mininet.topo import Topo
mininet.net import Mininet
mininet.util import irange,dumpNodeConnections
mininet.log import setLogLevel
class LinearTopo (Topo):
"Linear topology of k switches, with one host per switch."
def __init__(self, k=2, **opts):
"""Init.
k: number of switches (and hosts)
hconf: host configuration options
lconf: link configuration options"""
super(LinearTopo, self).__init__(**opts)
self.k = k
lastSwitch = None
for i in irange(1, k):
host = self.addHost('h%s' % i)
switch = self.addSwitch('s%s' % i)
self.addLink( host, switch)
if lastSwitch:
self.addLink( switch, lastSwitch)
lastSwitch = switch
def simpleTest():
"Create and test a simple network"
topo = LinearTopo(k=4)
net = Mininet(topo)
net.start()
print "Dumping host connections"
dumpNodeConnections(net.hosts)
print "Testing network connectivity"
net.pingAll()
net.stop()
if __name__ == '__main__':
# Tell mininet to print useful information
setLogLevel('info')
simpleTest()
</pre>

The important classes, methods, functions and variables in the above code include:

Topo: the base class for Mininet topologies
- addSwitch(): adds a switch to a topology and returns the switch name
- addHost(): adds a host to a topology and returns the host name
- addLink(): adds a bidirectional link to a topology (and returns a link key, but this is not important). Links in Mininet are bidirectional unless noted otherwise.
- Mininet: main class to create and manage a network
- start(): starts your network
- pingAll(): tests connectivity by trying to have all nodes ping each other
- stop(): stops your network
- net.hosts: all the hosts in a network
- dumpNodeConnections(): dumps connections to/from a set of nodes.
