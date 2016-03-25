# mininet

<pre>
mininet@10-0-2-15:~$ sudo bash
sudo: unable to resolve host 10-0-2-15
</pre>

### create 6 host namespaces
<pre>
root@10-0-2-15:~# ip netns add h1
root@10-0-2-15:~# ip netns add h2
root@10-0-2-15:~# ip netns add h3
root@10-0-2-15:~# ip netns add h4
root@10-0-2-15:~# ip netns add h5
root@10-0-2-15:~# ip netns add h6
</pre>

### create 4 switches
<pre>
root@10-0-2-15:~# ovs-vsctl add-br s1
root@10-0-2-15:~# ovs-vsctl add-br s2
root@10-0-2-15:~# ovs-vsctl add-br s3
root@10-0-2-15:~# ovs-vsctl add-br s4
root@10-0-2-15:~#
</pre>

### create link host 1(h1-eth0) to switch1 (s1-eth1) and host 2 (h2-eth0) to switch1 (s1-eth2)
<pre>
root@10-0-2-15:~# ip link add h1-eth0 type veth peer name s1-eth1
root@10-0-2-15:~# ip link add h2-eth0 type veth peer name s1-eth2
</pre>

### create link host 3(h3-eth0) to switch2 (s2-eth1) and host 4 (h4-eth0) to switch2 (s2-eth2)
<pre>
root@10-0-2-15:~# ip link add h3-eth0 type veth peer name s2-eth1
root@10-0-2-15:~# ip link add h4-eth0 type veth peer name s2-eth2
</pre>
