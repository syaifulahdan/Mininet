# mininet
learn mininet how to create topology custom depth = 2 , fanout = 32, create example file tree1024.py

code python
<pre>
#!/usr/bin/python

"""
Create a 1024-host network, and run the CLI on it.
If this fails because of kernel limits, you may have
to adjust them, e.g. by adding entries to /etc/sysctl.conf
and running sysctl -p. Check util/sysctl_addon.
"""

from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import OVSSwitch
from mininet.topolib import TreeNet

if __name__ == '__main__':
    setLogLevel( 'info' )
    network = TreeNet( depth=2, fanout=32, switch=OVSSwitch )
    network.run( CLI, network )

</pre>

<pre>
mininet@10-0-2-15:~/mininet/examples$ <b>sudo python tree1024.py</b>


</pre>
