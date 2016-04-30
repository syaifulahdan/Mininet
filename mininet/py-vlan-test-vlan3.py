#!/usr/bin/env python
from mininet.cli import CLI
from mininet.link import Link,TCLink,Intf
from mininet.net import Mininet
from mininet.node import RemoteController
 
if '__main__' == __name__:
  net = Mininet(link=TCLink)
  #h1 is under vlan10
  h1 = net.addHost('h1')
  #h2 is under vlan20
  h2 = net.addHost('h2')
  #h3 is a switch
  h3 = net.addHost('h3')
  #h4 is a switch
  h4 = net.addHost('h4')
  #h5 is under vlan10
  h5 = net.addHost('h5')
  #h6 is under vlan20
  h6 = net.addHost('h6')
  Link(h1, h3)
  Link(h2, h3)
  Link(h3, h4)
  Link(h5, h4)
  Link(h6, h4)
  net.build()
  h3.cmd("ifconfig h3-eth2 0")
  h4.cmd("ifconfig h4-eth0 0")
  h3.cmd("vconfig add h3-eth2 10")
  h3.cmd("vconfig add h3-eth2 20")
  h4.cmd("vconfig add h4-eth0 10")
  h4.cmd("vconfig add h4-eth0 20")
  h3.cmd("ifconfig h3-eth2.10 up")
  h3.cmd("ifconfig h3-eth2.20 up")
  h4.cmd("ifconfig h4-eth0.10 up")
  h4.cmd("ifconfig h4-eth0.20 up")
  h3.cmd("brctl addbr brvlan10")
  h3.cmd("brctl addbr brvlan20")
  h3.cmd("brctl addif brvlan10 h3-eth0")
  h3.cmd("brctl addif brvlan20 h3-eth1")
  h3.cmd("brctl addif brvlan10 h3-eth2.10")
  h3.cmd("brctl addif brvlan20 h3-eth2.20")
  h4.cmd("brctl addbr brvlan10")
  h4.cmd("brctl addbr brvlan20")
  h4.cmd("brctl addif brvlan10 h4-eth1")
  h4.cmd("brctl addif brvlan20 h4-eth2")
  h4.cmd("brctl addif brvlan10 h4-eth0.10")
  h4.cmd("brctl addif brvlan20 h4-eth0.20")
  h3.cmd("ifconfig brvlan10 up")
  h3.cmd("ifconfig brvlan20 up")
  h4.cmd("ifconfig brvlan10 up")
  h4.cmd("ifconfig brvlan20 up")
  CLI(net)
  net.stop()
