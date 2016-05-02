##### Flow Table 2 VLAN 

![img alt](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/image/Screenshot%20from%202016-05-03%2003:40:45.png)



1.  FLow Switch 2
![alt tag](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/image/Screenshot%20from%202016-05-03%2003:41:33.png)
<pre>
vs2 ofport list:
        ovs2 ofport 1
        ovs1 ofport 2o

 #ingress & egress
 switch2.cmdPrint('ovs-ofctl add-flow ovs2 in_port=1,actions=output:2')
 switch2.cmdPrint('ovs-ofctl add-flow ovs2 in_port=2,actions=output:1')

<pre/>
