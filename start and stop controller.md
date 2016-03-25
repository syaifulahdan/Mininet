# mininet

Usage: /etc/init.d/openvswitch-controller {start|stop|force-stop|restart|force-reload|status}

<pre>
mininet@10-0-2-15:~$ <b>sudo /etc/init.d/openvswitch-controller start</b>
sudo: unable to resolve host 10-0-2-15
 * Starting ovs-controller  ovs-controller                                                                                                                                   2016-03-26T04:32:39Z|00001|stream_ssl|INFO|Trusting CA cert from /etc/openvswitch-controller/cacert.pem (/C=US/ST=CA/O=Open vSwitch/OU=switchca/CN=OVS switchca CA Certificate (2015 Apr 20 00:30:04)) (fingerprint c4:a8:90:8b:b3:8c:af:43:38:2d:3e:6b:a2:d7:0d:0f:f3:18:ce:8d)
2016-03-26T04:32:39Z|00002|socket_util|ERR|6633: bind: Address already in use
2016-03-26T04:32:39Z|00003|controller|ERR|pssl:: connect: Address already in use
ovs-controller: no active or passive switch connections
mininet@10-0-2-15:~$ sudo /etc/init.d/openvswitch-controller start

</pre>
