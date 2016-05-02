Create 2 Vlan

![alt tag](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/image/Screenshot%20from%202016-05-03%2003:40:45.png)

1.  Create Topology [[two_Vlan.py]](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/two_vlan.py)
<pre>
root@CO0-19216856-103:/home/mininet/mininet/examples# <b>nano two-vlan.py </b>
</pre>

2.  Running two_vlan.py in mininet
<pre>
root@CO2-19216856-103:/home/mininet/mininet/examples# ./two_vlan.py 
</pre>

![alt tag](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/image/Screenshot%20from%202016-05-03%2003:09:35.png)

2.  Test Vlan
  
  2.a  Test Vlan [Teacher1 > Teacher2]

  <pre>
  mininet><b>teacher1 ping teacher2</b>
  </pre>
  ![alt tag](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/image/Screenshot%20from%202016-05-03%2003:16:55.png)
  
