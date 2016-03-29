##### mininet Vaiable, class, methode, functions
The important classes, methods, functions and variables in the above code include:

- <b>Topo</b>                 : the base class for Mininet topologies
- <b>addSwitch()</b>          : adds a switch to a topology and returns the switch name
- <b>addHost()</b>            : adds a host to a topology and returns the host name
- </b>addLink()</b>           : adds a bidirectional link to a topology (and returns a link key, but this is not important).                                  Links in Mininet are bidirectional unless noted otherwise. 
- <b>Mininet</b>              : main class to create and manage a network
- <b>start()</b>              : starts your network
- <b>pingAll()</b>            : tests connectivity by trying to have all nodes ping each other
- <b>stop()<?b>               : stops your network
-<b>net.hosts</b>             : all the hosts in a network
-<b>dumpNodeConnections()</b> : dumps connections to/from a set of nodes.
