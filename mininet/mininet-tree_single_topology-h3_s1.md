![alt img](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/image/Screenshot%20from%202016-04-28%2020:53:36.png)

<pre>
bertopeng17@bertopeng17-ThinkPad-T520:~$ <b>sudo mn --topo tree,3 --mac --switch ovsk --controller=remote</b>
[sudo] password for bertopeng17: 
*** Creating network
*** Adding controller
Unable to contact the remote controller at 127.0.0.1:6633
*** Adding hosts:
h1 h2 h3 h4 h5 h6 h7 h8 
*** Adding switches:
s1 s2 s3 s4 s5 s6 s7 
*** Adding links:
(s1, s2) (s1, s5) (s2, s3) (s2, s4) (s3, h1) (s3, h2) (s4, h3) (s4, h4) (s5, s6) (s5, s7) (s6, h5) (s6, h6) (s7, h7) (s7, h8) 
*** Configuring hosts
h1 h2 h3 h4 h5 h6 h7 h8 
*** Starting controller
c0 
*** Starting 7 switches
s1 s2 s3 s4 s5 s6 s7 ...
*** Starting CLI:
mininet> 
</pre>

<Pre>
mininet> dump
<Host h1: h1-eth0:10.0.0.1 pid=8237> 
<Host h2: h2-eth0:10.0.0.2 pid=8239> 
<Host h3: h3-eth0:10.0.0.3 pid=8241> 
<Host h4: h4-eth0:10.0.0.4 pid=8243> 
<Host h5: h5-eth0:10.0.0.5 pid=8245> 
<Host h6: h6-eth0:10.0.0.6 pid=8247> 
<Host h7: h7-eth0:10.0.0.7 pid=8249> 
<Host h8: h8-eth0:10.0.0.8 pid=8251> 
<OVSSwitch s1: lo:127.0.0.1,s1-eth1:None,s1-eth2:None pid=8256> 
<OVSSwitch s2: lo:127.0.0.1,s2-eth1:None,s2-eth2:None,s2-eth3:None pid=8259> 
<OVSSwitch s3: lo:127.0.0.1,s3-eth1:None,s3-eth2:None,s3-eth3:None pid=8262> 
<OVSSwitch s4: lo:127.0.0.1,s4-eth1:None,s4-eth2:None,s4-eth3:None pid=8265> 
<OVSSwitch s5: lo:127.0.0.1,s5-eth1:None,s5-eth2:None,s5-eth3:None pid=8268> 
<OVSSwitch s6: lo:127.0.0.1,s6-eth1:None,s6-eth2:None,s6-eth3:None pid=8271> 
<OVSSwitch s7: lo:127.0.0.1,s7-eth1:None,s7-eth2:None,s7-eth3:None pid=8274> 
<RemoteController c0: 127.0.0.1:6633 pid=8231> 
mininet> 
</pre>

<pre>
mininet> nodes
available nodes are: 
c0 h1 h2 h3 h4 h5 h6 h7 h8 s1 s2 s3 s4 s5 s6 s7
mininet> h1 ping s3

</pre>
