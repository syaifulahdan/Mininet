
##Create topology Single 3 Host , 1 Switch  with mac & Controller

<pre>
bertopeng17@bertopeng17-ThinkPad-T520:~$ <b>sudo mn --topo single,3 --mac --switch ovs<b>
</pre>

<pre>
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
<pre>


