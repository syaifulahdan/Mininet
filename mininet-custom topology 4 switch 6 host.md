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
