# mininet

<pre>
mininet@10-0-2-15:~$ <b>sudo bash</b>
sudo: unable to resolve host 10-0-2-15
</pre>

##### create 6 host namespaces
<pre>
root@10-0-2-15:~# <b>ip netns add h1</b>
root@10-0-2-15:~# <b>ip netns add h2</b>
root@10-0-2-15:~# <b>ip netns add h3</b>
root@10-0-2-15:~# <b>ip netns add h4</b>
root@10-0-2-15:~# <b>ip netns add h5</b>
root@10-0-2-15:~# <b>ip netns add h6</b>
</pre>

##### create 4 switches
<pre>
root@10-0-2-15:~# <b>ovs-vsctl add-br s1</b>
root@10-0-2-15:~# <b>ovs-vsctl add-br s2</b>
root@10-0-2-15:~# <b>ovs-vsctl add-br s3</b>
root@10-0-2-15:~# <b>ovs-vsctl add-br s4</b>
root@10-0-2-15:~#
</pre>

##### create link host 1(h1-eth0) to switch1 (s1-eth1) and host 2 (h2-eth0) to switch1 (s1-eth2)
<pre>
root@10-0-2-15:~# <b>ip link add h1-eth0 type veth peer name s1-eth1</b>
root@10-0-2-15:~# <b>ip link add h2-eth0 type veth peer name s1-eth2</b>
</pre>

##### create link host 3(h3-eth0) to switch2 (s2-eth1) and host 4 (h4-eth0) to switch2 (s2-eth2)
<pre>
root@10-0-2-15:~# <b>ip link add h3-eth0 type veth peer name s2-eth1</b>
root@10-0-2-15:~# <b>ip link add h4-eth0 type veth peer name s2-eth2</b>
</pre>

##### create link host 5(h5-eth0) to switch3 (s3-eth1) and host 6 (h6-eth0) to switch3 (s2-eth2)
<pre>
root@10-0-2-15:~# <b>ip link add h5-eth0 type veth peer name s3-eth1</b>
root@10-0-2-15:~# <b>ip link add h6-eth0 type veth peer name s3-eth2</b>
</pre>

![alt tag](https://github.com/syaifulahdan/mininet/blob/master/Screenshot%20from%202016-03-25%2016:43:47.png)

##### create link switch 1(s1-eth0) to switch4 (s4-eth1) and switch 2(s2-eth0) to switch4 (s4-eth2) and switch 3(s3-eth0) to switch4 (s4-eth3)

<pre>
root@10-0-2-15:~# ip link add s1-eth0 type veth peer name s4-eth1
root@10-0-2-15:~# ip link add s2-eth0 type veth peer name s4-eth2
root@10-0-2-15:~# ip link add s3-eth0 type veth peer name s4-eth3
</pre>
![alt tag](https://github.com/syaifulahdan/mininet/blob/master/Screenshot%20from%202016-03-25%2016:51:07.png)





##### IP Link Show

<pre>
root@10-0-2-15:~# <b>ip link show</b>
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 08:00:27:89:28:1d brd ff:ff:ff:ff:ff:ff
3: ovs-system: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default 
    link/ether ee:aa:28:e3:46:cf brd ff:ff:ff:ff:ff:ff
4: s1: <BROADCAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN mode DEFAULT group default 
    link/ether ea:c5:d8:df:c6:4b brd ff:ff:ff:ff:ff:ff
5: s2: <BROADCAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN mode DEFAULT group default 
    link/ether 9a:06:86:8f:4c:4c brd ff:ff:ff:ff:ff:ff
6: s3: <BROADCAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN mode DEFAULT group default 
    link/ether 82:61:cc:e3:65:48 brd ff:ff:ff:ff:ff:ff
7: s4: <BROADCAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN mode DEFAULT group default 
    link/ether 2a:63:77:3d:20:4e brd ff:ff:ff:ff:ff:ff
8: s1-eth1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 7a:c2:f6:a8:d1:72 brd ff:ff:ff:ff:ff:ff
9: h1-eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 4a:7c:e3:72:cd:f0 brd ff:ff:ff:ff:ff:ff
10: s1-eth2: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 86:f8:3c:11:23:35 brd ff:ff:ff:ff:ff:ff
11: h2-eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 46:7e:f3:f4:84:63 brd ff:ff:ff:ff:ff:ff
12: s2-eth1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 72:11:24:2a:2c:fa brd ff:ff:ff:ff:ff:ff
13: h3-eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether de:08:7f:6e:2d:2a brd ff:ff:ff:ff:ff:ff
14: s2-eth2: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 06:57:e9:59:23:36 brd ff:ff:ff:ff:ff:ff
15: h4-eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether e2:93:6e:ba:42:83 brd ff:ff:ff:ff:ff:ff
16: s3-eth1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 4e:23:d2:87:3b:9b brd ff:ff:ff:ff:ff:ff
17: h5-eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether da:6f:b7:a8:08:7e brd ff:ff:ff:ff:ff:ff
18: s3-eth2: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 7e:c5:95:45:25:d6 brd ff:ff:ff:ff:ff:ff
19: h6-eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether c6:62:35:a0:f0:fb brd ff:ff:ff:ff:ff:ff
root@10-0-2-15:~# 
</pre>

![alt tag](https://github.com/syaifulahdan/mininet/blob/master/Screenshot%20from%202016-03-25%2016:58:50.png)
