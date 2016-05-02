##### Flow Table 2 VLAN 

![img alt](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/image/Screenshot%20from%202016-05-03%2003:40:45.png)



1.  FLow Switch all table
![alt tag](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/image/Screenshot%20from%202016-05-03%2003:42:01.png)
<pre>
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

<pre/>
