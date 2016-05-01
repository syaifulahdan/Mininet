![alt tag](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/image/Screenshot%20from%202016-05-02%2000:32:10.png)

1.  Desain Topology via Python [[2controller.py]](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/2controller.py)
<pre>
root@bertopeng17-ThinkPad-T520:/home/bertopeng17# <b>ssh mininet@192.168.56.103 -p 2222</b>
mininet@CO2-19216856-103:~/mininet/mininet/examples$ <b>nano 2controller.sh</b>
</pre>

2.  Running Controller 1 [c6]
<pre>
mininet@CO2-19216856-103:~/pox$ <b>./pox.py openflow.of_01 --port=6633 forwarding.l2_learning</b>
POX 0.2.0 (carp) / Copyright 2011-2013 James McCauley, et al.
INFO:core:POX 0.2.0 (carp) is up.
</pre>

3. Running Controller 2 [c7]
<pre>
mininet@CO2-19216856-103:~/pox$ <b>./pox.py openflow.of_01 --port=6634 forwarding.l2_learning</b>
POX 0.2.0 (carp) / Copyright 2011-2013 James McCauley, et al.
INFO:core:POX 0.2.0 (carp) is up.
</pre>

4.  Running in MIninet
<pre>
root@CO2-19216856-103:/home/mininet/mininet/examples# chmod +x 2controller.sh
root@CO2-19216856-103:/home/mininet/mininet/examples# ./2controller.sh
*** Creating nodes
*** Creating links
*** Starting network
*** Configuring hosts
h1 h2 h3 h4 h5 h6 
*** Running CLI
*** Starting CLI:
mininet>
</pre>

5.  Teste Connection 

![alt tag](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/image/Screenshot%20from%202016-05-02%2000:40:56.png)
