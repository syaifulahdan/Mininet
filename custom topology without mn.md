### mininet- Custom Topology without MN
source : https://www.youtube.com/watch?v=yHUNeyaQKWY&index=2&list=PLyiXK9gbG3lCGVMsxNGidIabUnZeOq9hD

<pre>
mininet@10-0-2-15:~/mininet/examples$ 
</pre>

open the file in the directory emptynet.py , emptynet.py open the file in the directory <b>/mininet/examples$</b> then open it with nano editor

<pre>
mininet@10-0-2-15:~/mininet/examples$<b>nano emptynet.py</b> 
</pre>

<pre>
#!/usr/bin/python

"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""
<b>
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():
</b>
    "Create an empty network and add nodes to it."
<b>
    net = Mininet( controller=Controller )
</b>
    info( '*** Adding controller\n' )
    <b>net.addController( 'c0' )</b>

    info( '*** Adding hosts\n' )
    <b>h1 = net.addHost( 'h1', ip='10.0.0.1' )
    h2 = net.addHost( 'h2', ip='10.0.0.2' )</b>

    info( '*** Adding switch\n' )
    <b>s3 = net.addSwitch( 's3' )</b>

    info( '*** Creating links\n' )
    <b>net.addLink( h1, s3 )
    net.addLink( h2, s3 )</b>

    info( '*** Starting network\n')
    <b>net.start()</b>

    info( '*** Running CLI\n' )
    <b>CLI( net )</b>
    info( '*** Stopping network' )
<b>
if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
</b>
</pre>

####Default Controller
<pre>
<b>
net = Mininet( controller=Controller )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )
</b>
</pre>

####Host
<pre>
<b>
 info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='10.0.0.1' )
    h2 = net.addHost( 'h2', ip='10.0.0.2' )
</b>
</pre>


####Link Host to Single Switch
<pre>
<b>
 info( '*** Creating links\n' )
    net.addLink( h1, s3 )
    net.addLink( h2, s3 )
</b>
</pre>

#####If summarized, the code is as follows

<pre>
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():
    net = Mininet( controller=Controller )
    net.addController( 'c0' )
   
    h1 = net.addHost( 'h1', ip='10.0.0.1' )
    h2 = net.addHost( 'h2', ip='10.0.0.2' )
    
    s3 = net.addSwitch( 's3' )
    
    net.addLink( h1, s3 )
    net.addLink( h2, s3 )
    
    net.start()
    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()


</pre>
