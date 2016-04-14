#!/usr/bin/env python

from mininet.cli import CLI
from mininet.link import Link,TCLink,Intf
from mininet.net import Mininet
from mininet.node import RemoteController

if '__main__' == __name__:
  net = Mininet(link=TCLink)
  h1 = net.addHost('h1')
  h2 = net.addHost('h2')
  h3 = net.addHost('h3')
  h4 = net.addHost('h4')
  #h5 is a switch
  h5 = net.addHost('h5')
  #h6 is a router
  h6 = net.addHost('h6')

  Link(h1, h5)
  Link(h2, h5)
  Link(h3, h5)
  Link(h4, h5)
  Link(h5, h6)
  net.build()

  h1.cmd("ifconfig h1-eth0 0")
  h2.cmd("ifconfig h2-eth0 0")
  h3.cmd("ifconfig h3-eth0 0")
  h4.cmd("ifconfig h4-eth0 0")
  h5.cmd("ifconfig h5-eth0 0")
  h5.cmd("ifconfig h5-eth1 0")
  h5.cmd("ifconfig h5-eth2 0")
  h5.cmd("ifconfig h5-eth3 0")
  h5.cmd("ifconfig h5-eth4 0")
  h6.cmd("ifconfig h6-eth0 0")

  h5.cmd("vconfig add h5-eth4 10")
  h5.cmd("vconfig add h5-eth4 20")
  h6.cmd("vconfig add h6-eth0 10")
  h6.cmd("vconfig add h6-eth0 20")
  h5.cmd("ifconfig h5-eth4.10 up")
  h5.cmd("ifconfig h5-eth4.20 up")
  h5.cmd("brctl addbr brvlan10")
  h5.cmd("brctl addbr brvlan20")
  h5.cmd("brctl addif brvlan10 h5-eth0")
  h5.cmd("brctl addif brvlan10 h5-eth1")
  h5.cmd("brctl addif brvlan10 h5-eth4.10")
  h5.cmd("brctl addif brvlan20 h5-eth2")
  h5.cmd("brctl addif brvlan20 h5-eth3")
  h5.cmd("brctl addif brvlan20 h5-eth4.20")
  h5.cmd("ifconfig brvlan10 up")
  h5.cmd("ifconfig brvlan20 up")

  h6.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
  h6.cmd("ifconfig h6-eth0.10 10.0.10.254 netmask 255.255.255.0")
  h6.cmd("ifconfig h6-eth0.20 10.0.20.254 netmask 255.255.255.0")
  h1.cmd("ifconfig h1-eth0 10.0.10.1 netmask 255.255.255.0")
  h2.cmd("ifconfig h2-eth0 10.0.10.2 netmask 255.255.255.0")
  h3.cmd("ifconfig h3-eth0 10.0.20.1 netmask 255.255.255.0")
  h4.cmd("ifconfig h4-eth0 10.0.20.2 netmask 255.255.255.0")
  h1.cmd("ip route add default via 10.0.10.254 dev h1-eth0")
  h2.cmd("ip route add default via 10.0.10.254 dev h2-eth0")
  h3.cmd("ip route add default via 10.0.20.254 dev h3-eth0")
  h4.cmd("ip route add default via 10.0.20.254 dev h4-eth0")

  CLI(net)
  net.stop()
