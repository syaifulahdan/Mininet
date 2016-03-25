# mininet

![alt tag](https://github.com/syaifulahdan/mininet/blob/master/_20160326_015804.png)

<pre>
mininet@10-0-2-15:~$ <b>sudo mn --topo tree,depth=2,fanout=5 --controller=remote,ip=10.0.2.15,port=6633 --switch ovsk,protocols=openflow13, --link tc,bw=1,delay=10ms</b>
sudo: unable to resolve host 10-0-2-15
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 
*** Adding switches:
s1 s2 s3 s4 s5 s6 
*** Adding links:
(1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s1, s2) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s1, s3) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s1, s4) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s1, s5) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s1, s6) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s2, h1) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s2, h2) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s2, h3) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s2, h4) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s2, h5) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s3, h6) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s3, h7) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s3, h8) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s3, h9) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s3, h10) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s4, h11) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s4, h12) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s4, h13) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s4, h14) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s4, h15) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s5, h16) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s5, h17) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s5, h18) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s5, h19) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s5, h20) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s6, h21) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s6, h22) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s6, h23) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s6, h24) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (s6, h25) 
*** Configuring hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 
*** Starting controller
c0 
*** Starting 6 switches
s1 s2 s3 s4 s5 s6 ...(1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) (1.00Mbit 10ms delay) 
*** Starting CLI:
mininet> 

</pre>
