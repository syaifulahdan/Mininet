##### Flow Table 3 VLAN 

![img alt](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/image/Screenshot%20from%202016-05-03%2003:40:45.png)



1.  FLow Switch 1
![alt tag](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/image/Screenshot%20from%202016-05-03%2003:41:09.png)
<pre>
ovs3 ofport list:
 teacher2 ofport 1
        student2 ofport 2
        ovs2 ofport 3

 #ingress
 switch3.cmdPrint('ovs-ofctl add-flow ovs3 in_port=1,dl_vlan=0xffff,actions=mod_vlan_vid:100,output:3')
 switch3.cmdPrint('ovs-ofctl add-flow ovs3 in_port=2,dl_vlan=0xffff,actions=mod_vlan_vid:200,output:3')
 
 #egress
 switch3.cmdPrint('ovs-ofctl add-flow ovs3 in_port=3,dl_vlan=100,actions=strip_vlan,output:1')
 switch3.cmdPrint('ovs-ofctl add-flow ovs3 in_port=3,dl_vlan=200,actions=strip_vlan,output:2')

<pre/>
