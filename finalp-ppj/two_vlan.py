#!/usr/bin/env python2
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import Intf
from mininet.util import dumpNodeConnections



'''
two_vlan.py
teacher{1,2}: vlan 100
student{1,2}: vlan 200
'''

REMOTE_CONTROLLER_IP="127.0.0.1"

def MininetTopo():
    '''
    Prepare Your Topology
    '''
    net = Mininet (topo=None, build=False)

    controller = net.addController(name='controller0',
                                    controller=RemoteController,
                                    ip=REMOTE_CONTROLLER_IP,
                                    port=6633)

    info("Create Host node\n")
    teacher1 = net.addHost('teacher1', ip='10.0.0.1')
    teacher2 = net.addHost('teacher2', ip='10.0.0.2')
    student1 = net.addHost('student1', ip='10.0.0.3')
    student2 = net.addHost('student2', ip='10.0.0.4')

    info("Create Switch node\n")
    switch1 = net.addSwitch('ovs1')
    switch2 = net.addSwitch('ovs2')
    switch3 = net.addSwitch('ovs3')

    info("Link switch to host\n")
    net.addLink(switch1, student1)
    net.addLink(switch3, student2)
    net.addLink(switch1, teacher1)
    net.addLink(switch3, teacher2)
    net.addLink(switch1, switch2)
    net.addLink(switch2, switch3)


    '''
    Working your topology
    '''
    info("Start network\n")
    net.start()

    info("Dumping host connections\n")
    dumpNodeConnections(net.hosts)

    info("Testing network connectivity\n")
    net.pingAll()

    info("Set vlan id\n")

    '''
    ovs1 ofport list:
        teacher1 ofport 1
        student1 ofport 2
        ovs2 ofport 3
    '''
    #Ingress
    switch1.cmdPrint('ovs-ofctl add-flow ovs1 in_port=1,dl_vlan=0xffff,actions=mod_vlan_vid:100,output:3')
    switch1.cmdPrint('ovs-ofctl add-flow ovs1 in_port=2,dl_vlan=0xffff,actions=mod_vlan_vid:200,output:3')
    #Egress
    switch1.cmdPrint('ovs-ofctl add-flow ovs1 in_port=3,dl_vlan=100,actions=strip_vlan,output:1')
    switch1.cmdPrint('ovs-ofctl add-flow ovs1 in_port=3,dl_vlan=200,actions=strip_vlan,output:2')


    '''
    ovs3 ofport list:
        teacher2 ofport 1
        student2 ofport 2
        ovs2 ofport 3
    '''
    #Ingress
    switch3.cmdPrint('ovs-ofctl add-flow ovs3 in_port=1,dl_vlan=0xffff,actions=mod_vlan_vid:100,output:3')
    switch3.cmdPrint('ovs-ofctl add-flow ovs3 in_port=2,dl_vlan=0xffff,actions=mod_vlan_vid:200,output:3')
    #Egress
    switch3.cmdPrint('ovs-ofctl add-flow ovs3 in_port=3,dl_vlan=100,actions=strip_vlan,output:1')
    switch3.cmdPrint('ovs-ofctl add-flow ovs3 in_port=3,dl_vlan=200,actions=strip_vlan,output:2')

    '''
    ovs2 ofport list:
        ovs2 ofport 1
        ovs1 ofport 2
    '''
    switch2.cmdPrint('ovs-ofctl add-flow ovs2 in_port=1,actions=output:2')
    switch2.cmdPrint('ovs-ofctl add-flow ovs2 in_port=2,actions=output:1')

    info("Try vlan\n")
    net.pingAll()

    CLI(net)


    '''
    Clean mininet
    '''
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    MininetTopo()
