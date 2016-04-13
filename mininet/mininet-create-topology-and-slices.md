
### <b>Create Topology and Slices</b>

![alt img](https://github.com/syaifulahdan/mininet/blob/master/image/Screenshot%20from%202016-04-13%2012:19:29.png)



### <b>FlowVisor</b>
-  A special OpenFlow controller that can slice the network
-  Allows multiple tenants to use the same physical network


### <b>1.Create Mininet Topology</b>
<b>sudo mn --topo=linear,4 --arp --mac --controller=remote</b>

<pre>
mininet@CO0-19216856-101:~$ <b>sudo mn --topo=linear,4 --arp --mac --controller=remote</b>
sudo: unable to resolve host CO0-19216856-101
*** Creating network
*** Adding controller
Unable to contact the remote controller at 127.0.0.1:6633
*** Adding hosts:
h1 h2 h3 h4 
*** Adding switches:
s1 s2 s3 s4 
*** Adding links:
(h1, s1) (h2, s2) (h3, s3) (h4, s4) (s2, s1) (s3, s2) (s4, s3) 
*** Configuring hosts
h1 h2 h3 h4 
*** Starting controller
c0 
*** Starting 4 switches
s1 s2 s3 s4 ...
*** Starting CLI:
mininet> 

</pre>

open new Terminal
### <b>Check the nodes and links from flowvisor</b>

<pre>
bertopeng17@bertopeng17-ThinkPad-T520:~$ <b>cd flowvisor && make</b>
ant
Error: JAVA_HOME is not defined correctly.
  We cannot execute /usr/lib/jvm/java-7-openjdk-amd64/bin/java
make: *** [all] Error 1
bertopeng17@bertopeng17-ThinkPad-T520:~/flowvisor$
bertopeng17@bertopeng17-ThinkPad-T520:~/flowvisor$ <b>fvctl list-datapaths</b>
Password: <b>123456789</b>
Connected switches: 
  1 : 00:00:00:00:00:00:00:01
  2 : 00:00:00:00:00:00:00:02
  3 : 00:00:00:00:00:00:00:03
  4 : 00:00:00:00:00:00:00:04
  
bertopeng17@bertopeng17-ThinkPad-T520:~/flowvisor$ <b>fvctl list-links</b>
Password: <b>123456789</b>
[
  {
    "attributes": "fakeLink=true", 
    "dstDPID": "00:00:00:00:00:00:00:04", 
    "dstPort": "1", 
    "srcDPID": "00:00:00:00:00:00:00:03", 
    "srcPort": "0"
  }, 
  {
    "attributes": "fakeLink=true", 
    "dstDPID": "00:00:00:00:00:00:00:02", 
    "dstPort": "1", 
    "srcDPID": "00:00:00:00:00:00:00:04", 
    "srcPort": "0"
  }, 
  {
    "attributes": "fakeLink=true", 
    "dstDPID": "00:00:00:00:00:00:00:01", 
    "dstPort": "1", 
    "srcDPID": "00:00:00:00:00:00:00:02", 
    "srcPort": "0"
  }, 
  {
    "attributes": "fakeLink=true", 
    "dstDPID": "00:00:00:00:00:00:00:03", 
    "dstPort": "1", 
    "srcDPID": "00:00:00:00:00:00:00:01", 
    "srcPort": "0"
  }
]
bertopeng17@bertopeng17-ThinkPad-T520:~/flowvisor$ 
  
</pre>

