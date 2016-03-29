Skip to content
This repository
Search
Pull requests
Issues
Gist
 @syaifulahdan
 Unwatch 1
  Star 0
  Fork 0 syaifulahdan/mininet
 Code  Issues 0  Pull requests 0  Wiki  Pulse  Graphs  Settings
Tree: b64724798f Find file Copy pathmininet/py-linier-topology-without-performance.py
b647247  a minute ago
@syaifulahdan syaifulahdan Update py-linier-topology-without-performance.py
1 contributor
RawBlameHistory    45 lines (36 sloc)  1.06 KB

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
