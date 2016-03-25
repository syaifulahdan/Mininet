open a terminal in ubuntu and typing the following command

<pre>
bertopeng17@bertopeng17-ThinkPad-T520:~$ <b>ssh mininet@10.0.2.15 -p 2222</b>
mininet@10.0.2.15's password: 
Welcome to Ubuntu 14.04.4 LTS (GNU/Linux 3.13.0-77-generic i686)

 * Documentation:  https://help.ubuntu.com/
Last login: Fri Mar 25 15:06:21 2016
</pre>

after the computer is connected to mininet in virtualbox via ssh, then typing the following command

<pre>
mininet@10-0-2-15:~$ <b>cd ~/distribution-karaf-0.2.0-Helium/</b>
mininet@10-0-2-15:~/distribution-karaf-0.2.0-Helium$ <b>./bin/karaf</b>
karaf: JAVA_HOME not set; results may vary
                                                                                           
    ________                       ________                .__  .__       .__     __       
    \_____  \ ______   ____   ____ \______ \ _____  ___.__.|  | |__| ____ |  |___/  |_     
     /   |   \\____ \_/ __ \ /    \ |    |  \\__  \<   |  ||  | |  |/ ___\|  |  \   __\    
    /    |    \  |_> >  ___/|   |  \|    `   \/ __ \\___  ||  |_|  / /_/  >   Y  \  |      
    \_______  /   __/ \___  >___|  /_______  (____  / ____||____/__\___  /|___|  /__|      
            \/|__|        \/     \/        \/     \/\/            /_____/      \/          
                                                                                           

Hit '<tab>' for a list of available commands
and '[cmd] --help' for help on a specific command.
Hit '<ctrl-d>' or type 'system:shutdown' or 'logout' to shutdown OpenDaylight.

opendaylight-user@root>Exception in thread "JMX Connector Thread [service:jmx:rmi://0.0.0.0:44444/jndi/rmi://0.0.0.0:1099/karaf-root]" java.lang.RuntimeException: Could not start JMX connector server
	at org.apache.karaf.management.ConnectorServerFactory$1.run(ConnectorServerFactory.java:258)
Caused by: java.io.IOException: Cannot bind to URL [rmi://0.0.0.0:1099/karaf-root]: javax.naming.ConfigurationException [Root exception is java.rmi.UnknownHostException: Unknown host: 0.0.0.0; nested exception is: 
	java.net.UnknownHostException: 10-0-2-15: 10-0-2-15]
	at javax.management.remote.rmi.RMIConnectorServer.newIOException(RMIConnectorServer.java:826)
	at javax.management.remote.rmi.RMIConnectorServer.start(RMIConnectorServer.java:431)
	at org.apache.karaf.management.ConnectorServerFactory$1.run(ConnectorServerFactory.java:245)
Caused by: javax.naming.ConfigurationException [Root exception is java.rmi.UnknownHostException: Unknown host: 0.0.0.0; nested exception is: 
	java.net.UnknownHostException: 10-0-2-15: 10-0-2-15]
	at com.sun.jndi.rmi.registry.RegistryContext.bind(RegistryContext.java:143)
	at com.sun.jndi.toolkit.url.GenericURLContext.bind(GenericURLContext.java:226)
	at javax.naming.InitialContext.bind(InitialContext.java:419)
	at javax.management.remote.rmi.RMIConnectorServer.bind(RMIConnectorServer.java:643)
	at javax.management.remote.rmi.RMIConnectorServer.start(RMIConnectorServer.java:426)
	... 1 more
Caused by: java.rmi.UnknownHostException: Unknown host: 0.0.0.0; nested exception is: 
	java.net.UnknownHostException: 10-0-2-15: 10-0-2-15
	at sun.rmi.transport.tcp.TCPEndpoint.newSocket(TCPEndpoint.java:616)
	at sun.rmi.transport.tcp.TCPChannel.createConnection(TCPChannel.java:216)
	at sun.rmi.transport.tcp.TCPChannel.newConnection(TCPChannel.java:202)
	at sun.rmi.server.UnicastRef.newCall(UnicastRef.java:341)
	at sun.rmi.registry.RegistryImpl_Stub.bind(Unknown Source)
	at com.sun.jndi.rmi.registry.RegistryContext.bind(RegistryContext.java:137)
	... 5 more
Caused by: java.net.UnknownHostException: 10-0-2-15: 10-0-2-15
	at java.net.InetAddress.getLocalHost(InetAddress.java:1496)
	at java.net.AbstractPlainSocketImpl.connectToAddress(AbstractPlainSocketImpl.java:198)
	at java.net.AbstractPlainSocketImpl.connect(AbstractPlainSocketImpl.java:182)
	at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:392)
	at java.net.Socket.connect(Socket.java:579)
	at java.net.Socket.connect(Socket.java:528)
	at java.net.Socket.<init>(Socket.java:425)
	at java.net.Socket.<init>(Socket.java:208)
	at sun.rmi.transport.proxy.RMIDirectSocketFactory.createSocket(RMIDirectSocketFactory.java:40)
	at sun.rmi.transport.proxy.RMIMasterSocketFactory.createSocket(RMIMasterSocketFactory.java:147)
	at sun.rmi.transport.tcp.TCPEndpoint.newSocket(TCPEndpoint.java:613)
	... 10 more
Caused by: java.net.UnknownHostException: 10-0-2-15
	at java.net.Inet4AddressImpl.lookupAllHostAddr(Native Method)
	at java.net.InetAddress$1.lookupAllHostAddr(InetAddress.java:922)
	at java.net.InetAddress.getAddressesFromNameService(InetAddress.java:1316)
	at java.net.InetAddress.getLocalHost(InetAddress.java:1492)
	... 20 more
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [bundleresource://323.fwk9795434:1/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [bundleresource://323.fwk9795434:2/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [bundleresource://323.fwk9795434:3/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.slf4j.impl.JDK14LoggerFactory]
GossipRouter started at Fri Mar 25 15:24:52 PDT 2016
Listening on port 12001 bound on address 0.0.0.0/0.0.0.0
Backlog is 1000, linger timeout is 2000, and read timeout is 0

opendaylight-user@root>

</pre>
