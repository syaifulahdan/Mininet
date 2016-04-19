

1. create topology VLAN using tools [[ramonfontes]] (http://www.ramonfontes.com/vnd/#)

![alt img](https://github.com/syaifulahdan/mininet/blob/master/vnd/image/Screenshot%20from%202016-04-20%2003:09:12.png)


2. Save toplogy : File > Export > Export to Mininet > Download .   file name : [[mininetCode81848.sh]](https://github.com/syaifulahdan/mininet/blob/master/vnd/create/createvlan1/mininetCode81848.sh)

3. Save topology : File > Export > Export to openflow Controller > Download .   file name : [[controllerCode915.sh]](https://github.com/syaifulahdan/mininet/blob/master/vnd/create/createvlan1/controllerCode915.sh)


or we can download point 2&3 using script in your terminal :
<pre>
bertopeng17@bertopeng17-ThinkPad-T520:~/mininet/mininet/examples$ <b>wget http://ramonfontes.com/vnd/mininetCode81848.sh</b>
--2016-04-20 03:25:32--  http://ramonfontes.com/vnd/mininetCode81848.sh
Resolving ramonfontes.com (ramonfontes.com)... 138.128.178.82
Connecting to ramonfontes.com (ramonfontes.com)|138.128.178.82|:80... connected.
HTTP request sent, awaiting response... 404 Categoria não encontrada
2016-04-20 03:25:33 ERROR 404: Categoria não encontrada.

bertopeng17@bertopeng17-ThinkPad-T520:~/mininet/mininet/examples$ <b>wget http://ramonfontes.com/vnd/controllerCode915.sh</b>
--2016-04-20 03:26:58--  http://ramonfontes.com/vnd/controllerCode915.sh
Resolving ramonfontes.com (ramonfontes.com)... 138.128.178.82
Connecting to ramonfontes.com (ramonfontes.com)|138.128.178.82|:80... connected.
HTTP request sent, awaiting response... 404 Categoria não encontrada
2016-04-20 03:26:59 ERROR 404: Categoria não encontrada.

</pre>

![alt img](https://github.com/syaifulahdan/mininet/blob/master/vnd/image/Screenshot%20from%202016-04-20%2003:29:35.png)


3. Generate to mininet code python <b>mininetCode81848.sh</b>

   copy or create file mininetCode81848.sh in to editor nano or pico in directori mininet/mininet/examples and controllerCode915.sh into directori ~/pox/ext$
   ![alt img] (https://github.com/syaifulahdan/mininet/blob/master/vnd/image/Screenshot%20from%202016-04-20%2003:37:56.png)
   
   then type script in directory examples : 
   <pre>
   bertopeng17@bertopeng17-ThinkPad-T520:~/mininet/mininet/examples$ <b>chmod +x mininetCode81848.sh </b>
   bertopeng17@bertopeng17-ThinkPad-T520:~/mininet/mininet/examples$ <b>./mininetCode81848.sh </b>
   *** Mininet must run as root.
   bertopeng17@bertopeng17-ThinkPad-T520:~/mininet/mininet/examples$ sudo ./mininetCode81848.sh 
   [sudo] password for bertopeng17:<b>*********</b> 
   *** Creating nodes
   *** Creating links
   *** Starting network
   *** Configuring hosts
   h1 h2 h3 h4 
   *** Running CLI
   *** Starting CLI:
   mininet> 
   </pre>
   
   ![alt img](https://github.com/syaifulahdan/mininet/blob/master/vnd/image/Screenshot%20from%202016-04-20%2003:41:02.png)

   <pre>
   mininet> <b>nodes</b>
   available nodes are: 
   c7 h1 h2 h3 h4 s5 s6
   mininet> 

   </pre>
   
   <pre>
      mininet> <b>dump</b>
      Host h1: h1-eth0:10.0.0,10 pid=8473 
      Host h2: h2-eth0:10.0.0.20 pid=8475 
      Host h3: h3-eth0:10.0.0.40 pid=8477 
      Host h4: h4-eth0:10.0.0.30 pid=8479 
      OVSSwitch s5: lo:127.0.0.1,s5-eth1:None,s5-eth2:None,s5-eth3:None pid=8484
      OVSSwitch s6: lo:127.0.0.1,s6-eth1:None,s6-eth2:None,s6-eth3:None pid=8487 
      Controller c7: 127.0.0.1:6633 pid=8492
      mininet> 
   </pre>
   
4. Generate code controllerCode915.sh to POX controler 
   
   copy controllerCode915.sh to direcotry pox/ext :
   <pre>
   root@bertopeng17-ThinkPad-T520:~/pox/ext# <b>chmod +x controllerCode915.py </b>
   root@bertopeng17-ThinkPad-T520:~/pox/ext# <b>chmod +X controllerCode915.py </b>
   root@bertopeng17-ThinkPad-T520:~/pox/ext# <b>ls</b>
   controllerCode915.py  README  skeleton.py
   root@bertopeng17-ThinkPad-T520:~/pox/ext# <b>nano controllerCode915.py </b>
   root@bertopeng17-ThinkPad-T520:~/pox/ext# <b>cd ..</b>
   root@bertopeng17-ThinkPad-T520:~/pox# <b>./pox.py controllerCode915</b>
   POX 0.2.0 (carp) / Copyright 2011-2013 James McCauley, et al.
   INFO:controllerCode915:*** Starting... ***
   INFO:controllerCode915:*** Waiting for switches to connect.. ***
   INFO:core:POX 0.2.0 (carp) is up.
   ERROR:openflow.of_01:Error 98 while binding socket: Address already in use
   ERROR:openflow.of_01: You may have another controller running.
   ERROR:openflow.of_01: Use openflow.of_01 --port=<port> to run POX on another port.
   INFO:controllerCode915:    *** Installing static flows... ***
   WARNING:openflow:Couldn't send to 00-00-00-00-00-05 because we're not connected to it!
   WARNING:openflow:Couldn't send to 00-00-00-00-00-05 because we're not connected to it!
   WARNING:openflow:Couldn't send to 00-00-00-00-00-06 because we're not connected to it!
   WARNING:openflow:Couldn't send to 00-00-00-00-00-06 because we're not connected to it!
   WARNING:openflow:Couldn't send to 00-00-00-00-00-05 because we're not connected to it!
   WARNING:openflow:Couldn't send to 00-00-00-00-00-05 because we're not connected to it!
   WARNING:openflow:Couldn't send to 00-00-00-00-00-06 because we're not connected to it!
   WARNING:openflow:Couldn't send to 00-00-00-00-00-06 because we're not connected to it!
   INFO:controllerCode915:    *** Static flows installed. ***
     </pre>
5. 
