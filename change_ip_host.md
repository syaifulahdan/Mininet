# mininet Change Ip host 

<pre>
mininet> <b>h1 ifconfig h1-eth0 10.0.2.100 netmask 255.0.0.0 </b>
mininet> <b>h2 ifconfig h2-eth0 10.0.2.101 netmask 255.0.0.0</b>
mininet> <b>h1 ping h2</b>
PING 10.0.2.101 (10.0.2.101) 56(84) bytes of data.
64 bytes from 10.0.2.101: icmp_seq=1 ttl=64 time=235 ms
64 bytes from 10.0.2.101: icmp_seq=2 ttl=64 time=2.39 ms
64 bytes from 10.0.2.101: icmp_seq=3 ttl=64 time=0.899 ms
64 bytes from 10.0.2.101: icmp_seq=4 ttl=64 time=1.02 ms
^C
--- 10.0.2.101 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 0.899/59.973/235.572/101.383 ms
mininet> 

</pre>
