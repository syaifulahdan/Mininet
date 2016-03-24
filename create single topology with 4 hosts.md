Creating single topology with 4 hosts and 1 switches, using command :8ball: 


<b>sudo mn --topo=single,4</b>
Controller = 1
Switches = 1
Hosts      = 4 
<pre>
mininet@controller:~$ <b>sudo mn --topo=single,4</b>
sudo:unable to resolve host controller
*** Creating network
*** Adding controller
*** Adding host:
h1 h2 h3 h4
*** Adding switches:
s1
*** Adding links:
(h1,s1) (h2,s1) (h3,s1) (h4,s1)
*** configuring hosts
h1 h2 h3 h4
*** Starting controller
c0
*** Starting 1 switches
s1 ...
*** Starting CLI:
mininet>
</pre>

<pre>
mininet>dump
<host h1: h1-eth0:10.0.0.1 pid=1215>
</pre>
<host h2: h2-eth0:10.0.0.2 pid=1219>
<host h3: h3-eth0:10.0.0.3 pid=1221>
<host h4: h4-eth0:10.0.0.4 pid=1223>
<OVSSwitch s1: lo:127.0.0.1,s1-eth1:none,s1-eth2:none,s1-eth3:none,s1-eth4:none
pid=1228>
<Controller c0:127.0.0.1:6633 pid=1208>
mininet> 


