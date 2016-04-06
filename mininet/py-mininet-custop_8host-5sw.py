"""Custom topology example"

""mininet@10-0-2-15:~/mininet/custom$sudo mn --custom topo-2sw-2host.py --topo my topo --controller=remote,ip=10.0.2.15""

   host   (h1, h2, h3, h4, h5,h6,h7,h8)
   switch (s0,s1, s2,s3,s4)


"""

from mininet.topo import Topo

class MyTopo( Topo ):
    def __init__( self ):
        "Create custom topo."
        # Initialize topology
        Topo.__init__( self )

        # tambah host
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )

        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )

        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )

        h7 = self.addHost( 'h7' )
        h8 = self.addHost( 'h8' )

        # tambah switch
        s0 = self.addSwitch( 's0' )
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4')

        # membuat link host ke switch
        self.addLink( h1, s1 )
        self.addLink( h2, s1 )

        self.addLink( h3, s2 )
        self.addLink( h4, s2 )

        self.addLink( h5, s3 )
        self.addLink( h6, s3 )

        self.addLink( h7, s4 )
        self.addLink( h8, s4 )

        # membuat link switch  ke switch

        self.addLink( s1, s0 )
        self.addLink( s2, s0 )
        
topos = { 'mytopo': ( lambda: MyTopo() ) }

