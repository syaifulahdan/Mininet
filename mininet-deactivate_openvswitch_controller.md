# mininet
<pre>
mininet@10-0-2-15:~$ <b>sudo service openvswitch-controller stop</b>
sudo: unable to resolve host 10-0-2-15
 * Stopping ovs-controller ovs-controller                                                                                                                             [ OK ] 
mininet@10-0-2-15:~$ 
</pre>

<pre>
mininet@10-0-2-15:~$ <b>sudo update-rc.d openvswitch-controller disable</b>
sudo: unable to resolve host 10-0-2-15
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
	LANGUAGE = "en_US:",
	LC_ALL = (unset),
	LC_PAPER = "id_ID.UTF-8",
	LC_ADDRESS = "id_ID.UTF-8",
	LC_MONETARY = "id_ID.UTF-8",
	LC_NUMERIC = "id_ID.UTF-8",
	LC_TELEPHONE = "id_ID.UTF-8",
	LC_IDENTIFICATION = "id_ID.UTF-8",
	LC_MEASUREMENT = "id_ID.UTF-8",
	LC_TIME = "id_ID.UTF-8",
	LC_NAME = "id_ID.UTF-8",
	LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
update-rc.d: warning:  start runlevel arguments (none) do not match openvswitch-controller Default-Start values (2 3 4 5)
update-rc.d: warning:  stop runlevel arguments (none) do not match openvswitch-controller Default-Stop values (0 1 6)
 Disabling system startup links for /etc/init.d/openvswitch-controller ...
 Removing any system startup links for /etc/init.d/openvswitch-controller ...
   /etc/rc0.d/K20openvswitch-controller
   /etc/rc1.d/K20openvswitch-controller
   /etc/rc2.d/K80openvswitch-controller
   /etc/rc3.d/K80openvswitch-controller
   /etc/rc4.d/K80openvswitch-controller
   /etc/rc5.d/K80openvswitch-controller
   /etc/rc6.d/K20openvswitch-controller
 Adding system startup for /etc/init.d/openvswitch-controller ...
   /etc/rc0.d/K20openvswitch-controller -> ../init.d/openvswitch-controller
   /etc/rc1.d/K20openvswitch-controller -> ../init.d/openvswitch-controller
   /etc/rc6.d/K20openvswitch-controller -> ../init.d/openvswitch-controller
   /etc/rc2.d/K80openvswitch-controller -> ../init.d/openvswitch-controller
   /etc/rc3.d/K80openvswitch-controller -> ../init.d/openvswitch-controller
   /etc/rc4.d/K80openvswitch-controller -> ../init.d/openvswitch-controller
   /etc/rc5.d/K80openvswitch-controller -> ../init.d/openvswitch-controller
mininet@10-0-2-15:~$ 

</pre>
