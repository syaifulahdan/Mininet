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
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:10', ip='10.0.0.10/8' )
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:20', ip='10.0.0.20/8' )
    h3 = net.addHost( 'h3', mac='00:00:00:00:00:30', ip='10.0.0.30/8' )
    h4 = net.addHost( 'h4', mac='00:00:00:00:00:40', ip='10.0.0.40/8' )
    h5 = net.addHost( 'h5', mac='00:00:00:00:00:50', ip='10.0.0.50/8' )
    h6 = net.addHost( 'h6', mac='00:00:00:00:00:60', ip='10.0.0.60/8' )
    c6 = net.addController( 'c6',ip='127.0.0.1',port=6633 )
    c7 = net.addController( 'c7',ip='127.0.0.1',port=6634 )
    s7 = net.addSwitch( 's7', listenPort=6673, mac='00:00:00:00:00:07' )
    s8 = net.addSwitch( 's8', listenPort=6674, mac='00:00:00:00:00:08' )

    print "*** Creating links"
    net.addLink(h1, s7)
    net.addLink(h2, s7)
    net.addLink(h3, s7)
    net.addLink(h4, s8)
    net.addLink(h5, s8)
    net.addLink(h6, s8)
    net.addLink(s7, s8)

    print "*** Starting network"
    net.build()
    c6.start()
    c7.start()
    s8.start( [c7] )
    s7.start( [c6] )
    
    print "*** Running CLI"
    CLI( net )
    
    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()




