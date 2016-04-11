# mininet - Openflow Linier Topology

The network you'll use in this exercise includes hosts and switches connected in a linear
topology, as shown in the figure below.

<img src="https://github.com/syaifulahdan/mininet/blob/master/image/linier_topology.png" width="400" height="400" align="center" title="syaifulahdan/mininet" />

##### Creating Topology Linear Topology (without Performance Settings)

<pre>
#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel

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
