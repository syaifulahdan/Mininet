# mininet single Switch


![alt tag](http://sdnhub.org/wp-content/uploads/2014/03/mininet_single_switch1.png)

Following command spawns a single switch with 3 hosts attached to it. The hosts will be assigned static IP addresses and MAC addresses.
<pre>
mininet@10-0-2-15:~$ <b>sudo mn  --arp --topo single,3 --mac --switch ovsk --controller remote</b>
sudo: unable to resolve host 10-0-2-15
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 
*** Adding switches:
s1 
*** Adding links:
(h1, s1) (h2, s1) (h3, s1) 
*** Configuring hosts
h1 h2 h3 
*** Starting controller
c0 
*** Starting 1 switches
s1 ...
*** Starting CLI:
mininet> 

</pre>


