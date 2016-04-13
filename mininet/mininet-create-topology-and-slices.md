
### <b>Create Topology and Slices</b>

![alt img](https://github.com/syaifulahdan/mininet/blob/master/image/Screenshot%20from%202016-04-13%2012:19:29.png)



### <b>FlowVisor</b>
-  A special OpenFlow controller that can slice the network
-  Allows multiple tenants to use the same physical network

### <b>FlowVisor Installation</b>
-  Download flowvisor : git clone git://github.com/OPENNETWORKINGLAB/flowvisor.git
<pre>
bertopeng17@bertopeng17-ThinkPad-T520:~$ git clone git://github.com/OPENNETWORKINGLAB/flowvisor.git
Cloning into 'flowvisor'...
remote: Counting objects: 6356, done.
remote: Total 6356 (delta 0), reused 0 (delta 0), pack-reused 6356
Receiving objects: 100% (6356/6356), 8.67 MiB | 484.00 KiB/s, done.
Resolving deltas: 100% (3823/3823), done.
Checking connectivity... done.
bertopeng17@bertopeng17-ThinkPad-T520:~$ 
<?pre>

### <b>Create Mininet Topology</b>
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
