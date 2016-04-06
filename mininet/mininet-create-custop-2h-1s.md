# mininet

sudo bash
### Membuat host namespaces
<pre>
root@controller:~#<b>ip netns add h1</b>
root@controller:~#<b>ip netns add h2</b>
</pre>
### Membuat switch
<pre>
root@controller:~#<b>ovs-vsctl add-br s1</b>
</pre>
### Membuat links
<pre>
root@controller:~#<b>ip link add h1-eth0 type veth peer name s1-eth1</b>
root@controller:~#<b>ip link add h2-eth0 type veth peer name s1-eth2</b>
</pre>

<pre>
root@controller:~#<b>ip link show</b>
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 08:00:27:92:85:46 brd ff:ff:ff:ff:ff:ff
11: ovs-system: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default 
    link/ether 26:ec:c7:65:ed:84 brd ff:ff:ff:ff:ff:ff
26: s1: <BROADCAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN mode DEFAULT group default 
    link/ether 92:ed:2c:30:54:47 brd ff:ff:ff:ff:ff:ff
27: s1-eth1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 12:95:68:fe:29:3d brd ff:ff:ff:ff:ff:ff
28: h1-eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 66:6b:d7:05:b6:7c brd ff:ff:ff:ff:ff:ff
29: s1-eth2: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 3e:4d:2e:33:6d:2b brd ff:ff:ff:ff:ff:ff
30: h2-eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 56:8e:59:a4:9e:7f brd ff:ff:ff:ff:ff:ff

</pre>


### Memindahkan port host ke namespace
<pre>
root@controller:~#<b>ip link set h1-eth0 netns h1</b>
root@controller:~#<b>ip link set h2-eth0 netns h2</b>
</pre>

<b>ip netns exec h1 ip link show</b>
<pre>
root@controller:~#<b>ip netns exec h1 ip link show</b>
1: lo: <LOOPBACK> mtu 65536 qdisc noop state DOWN mode DEFAULT group default 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
28: h1-eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 66:6b:d7:05:b6:7c brd ff:ff:ff:ff:ff:ff
root@controller:~# 

</pre>

<b>ip netns exec h2 ip link show</b>

<pre>
root@controller:~#<b>ip netns exec h2 ip link show</b>
1: lo: <LOOPBACK> mtu 65536 qdisc noop state DOWN mode DEFAULT group default 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
30: h2-eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 56:8e:59:a4:9e:7f brd ff:ff:ff:ff:ff:ff
root@controller:~# 
</pre>

### menghubungkan switch ports to OVS
<pre>
root@controller:~# <b>ovs-vsctl add-port s1 s1-eth1</b>
root@controller:~# <b>ovs-vsctl add-port s1 s1-eth2</b>
</pre>

<pre>
root@controller:~# <b>ovs-vsctl show</b>
aaa4c93f-aa5a-4e41-b565-47c6f100c291
    Bridge "s1"
        Port "s1-eth2"
            Interface "s1-eth2"
        Port "s1-eth1"
            Interface "s1-eth1"
        Port "s1"
            Interface "s1"
                type: internal
    ovs_version: "2.0.2"

</pre>






### Set up OpenFlow controller
<pre>
root@controller:~# <b>ovs-vsctl set-controller s1 tcp:127.0.0.1</b>
root@controller:~# <b>ovs-controller ptcp: &</b>
[1] 6423
root@controller:~# 2016-02-28T00:52:02Z|00001|socket_util|ERR|6633: bind: Address already in use
2016-02-28T00:52:02Z|00002|controller|ERR|ptcp:: connect: Address already in use
ovs-controller: no active or passive switch connections

[1]+  Exit 1                  ovs-controller ptcp:

</pre>

<pre>
root@controller:~#<b>ovs-vsctl show</b>
aaa4c93f-aa5a-4e41-b565-47c6f100c291
    Bridge "s1"
        Controller "tcp:127.0.0.1"
            is_connected: true
        Port "s1-eth2"
            Interface "s1-eth2"
        Port "s1-eth1"
            Interface "s1-eth1"
        Port "s1"
            Interface "s1"
                type: internal
    ovs_version: "2.0.2"
root@controller:~# 

</pre>


###Configure network
<pre>
root@controller:~# <b>ip netns exec h1 ifconfig h1-eth0 10.1</b>
root@controller:~# <b>ip netns exec h1 ifconfig lo up</b>
root@controller:~# <b>ip netns exec h2 ifconfig h2-eth0 10.2</b>
root@controller:~# <b>ip netns exec h2 ifconfig lo up </b>
root@controller:~# <b>ifconfig s1-eth1 up</b>
root@controller:~# <b>ifconfig s1-eth2 up</b>
</pre>
### Test network
<pre>
root@controller:~# <b>ip netns exec h1 ifconfig h2-eth0 10.2</b>
SIOCSIFADDR: No such device
h2-eth0: ERROR while getting interface flags: No such device
root@controller:~# ip netns exec h2 ifconfig h2-eth0 10.2
root@controller:~# ip netns exec h2 ifconfig lo up
root@controller:~# ifconfig s1-eth1 up
root@controller:~# ifconfig s1-eth2 up
root@controller:~# ip netns exec h1 ping -c1 10.2
PING 10.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=6.14 ms

--- 10.2 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 6.142/6.142/6.142/0.000 ms
root@controller:~# 

</pre>

