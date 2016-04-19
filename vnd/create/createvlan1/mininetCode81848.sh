#!/usr/bin/python

"""
Script created by VND - Visual Network Description (SDN version)
"""
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, IVSSwitch, UserSwitch
from mininet.link import Link, TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

def topology():

    "Create a network."
    net = Mininet( controller=Controller, link=TCLink, switch=OVSKernelSwitch )

    print "*** Creating nodes"
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.0,10/8' )
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:02', ip='10.0.0.20/8' )
    h3 = net.addHost( 'h3', mac='00:00:00:00:00:03', ip='10.0.0.40/8' )
    h4 = net.addHost( 'h4', mac='00:00:00:00:00:04', ip='10.0.0.30/8' )
    s5 = net.addSwitch( 's5', protocols='OpenFlow10', listenPort=6673, mac='00:00:00:00:00:05' )
    s6 = net.addSwitch( 's6', protocols='OpenFlow10', listenPort=6674, mac='00:00:00:00:00:06' )
    c7 = net.addController( 'c7' )

    print "*** Creating links"
    net.addLink(s5, s6)
    net.addLink(h4, s6)
    net.addLink(h3, s6)
    net.addLink(h2, s5)
    net.addLink(h1, s5)

    print "*** Starting network"
    net.build()
    c7.start()
    s6.start( [c7] )
    s5.start( [c7] )

    print "*** Running CLI"
    CLI( net )

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()


