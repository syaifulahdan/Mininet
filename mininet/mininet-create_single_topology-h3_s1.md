
##Create topology Single 3 Host , 1 Switch  with mac & Controller

<pre>
bertopeng17@bertopeng17-ThinkPad-T520:~$ <b>sudo mn --topo single,3 --mac --switch ovs<b>
k --controller=remote
*** Creating network
*** Adding controller
Unable to contact the remote controller at 127.0.0.1:6633
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

![alt img](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/image/Screenshot%20from%202016-04-28%2016:04:46.png)

<pre>
mininet> <b>dump</b>
<Host h1: h1-eth0:10.0.0.1 pid=4918> 
<Host h2: h2-eth0:10.0.0.2 pid=4920> 
<Host h3: h3-eth0:10.0.0.3 pid=4922> 
<OVSSwitch s1: lo:127.0.0.1,s1-eth1:None,s1-eth2:None,s1-eth3:None pid=4927> 
<RemoteController c0: 127.0.0.1:6633 pid=4912> 
</pre>

