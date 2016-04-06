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

#####ping host
<pre>
mininet> <b>h1 ping h2</b>
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=2.30 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=17.3 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=18.0 ms
64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=12.3 ms
64 bytes from 10.0.0.2: icmp_seq=5 ttl=64 time=12.6 ms
^C
--- 10.0.0.2 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 2.308/12.538/18.019/5.620 ms
mininet> 

</pre>
