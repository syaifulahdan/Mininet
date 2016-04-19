#!/usr/bin/python
"""
#Script created by VND - Visual Network Description (SDN version) 
"""
from pox.core import core
from pox.lib.addresses import IPAddr
from pox.lib.addresses import EthAddr
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

#flow0: 
switch0 = 0000000000000005
flow0msg = of.ofp_flow_mod() 
flow0msg.cookie = 0 
flow0msg.priority = 32768
flow0msg.match.in_port = 1
# ACTIONS---------------------------------
flow0vlan_id = of.ofp_action_vlan_vid (vlan_vid = 10)
flow0out = of.ofp_action_output (port = 3)
flow0msg.actions = [flow0vlan_id, flow0out] 

#flow1: 
switch1 = 0000000000000005
flow1msg = of.ofp_flow_mod() 
flow1msg.cookie = 0 
flow1msg.priority = 32768
flow1msg.match.in_port = 2
# ACTIONS---------------------------------
flow1vlan_id = of.ofp_action_vlan_vid (vlan_vid = 20)
flow1out = of.ofp_action_output (port = 3)
flow1msg.actions = [flow1vlan_id, flow1out] 

#flow2: 
switch2 = 0000000000000006
flow2msg = of.ofp_flow_mod() 
flow2msg.cookie = 0 
flow2msg.priority = 32768
flow2msg.match.in_port = 2
# ACTIONS---------------------------------
flow2vlan_id = of.ofp_action_vlan_vid (vlan_vid = 20)
flow2out = of.ofp_action_output (port = 1)
flow2msg.actions = [flow2vlan_id, flow2out] 

#flow3: 
switch3 = 0000000000000006
flow3msg = of.ofp_flow_mod() 
flow3msg.cookie = 0 
flow3msg.priority = 32768
flow3msg.match.in_port = 3
# ACTIONS---------------------------------
flow3vlan_id = of.ofp_action_vlan_vid (vlan_vid = 7)
flow3out = of.ofp_action_output (port = 1)
flow3msg.actions = [flow3vlan_id, flow3out] 

#flow4: 
switch4 = 0000000000000005
flow4msg = of.ofp_flow_mod() 
flow4msg.cookie = 0 
flow4msg.priority = 32768
# ACTIONS---------------------------------
flow4vlan_id = of.ofp_action_vlan_vid (vlan_vid = 10)
flow4stripvlan = of.ofp_action_strip_vlan () 
flow4out = of.ofp_action_output (port = 1)
flow4msg.actions = [flow4vlan_id, flow4stripvlan, flow4out] 

#flow5: 
switch5 = 0000000000000005
flow5msg = of.ofp_flow_mod() 
flow5msg.cookie = 0 
flow5msg.priority = 32768
# ACTIONS---------------------------------
flow5vlan_id = of.ofp_action_vlan_vid (vlan_vid = 20)
flow5out = of.ofp_action_output (port = 2)
flow5msg.actions = [flow5vlan_id, flow5out] 

#flow6: 
switch6 = 0000000000000006
flow6msg = of.ofp_flow_mod() 
flow6msg.cookie = 0 
flow6msg.priority = 32768
# ACTIONS---------------------------------
flow6vlan_id = of.ofp_action_vlan_vid (vlan_vid = 20)
flow6stripvlan = of.ofp_action_strip_vlan () 
flow6out = of.ofp_action_output (port = 1)
flow6msg.actions = [flow6vlan_id, flow6stripvlan, flow6out] 

#flow7: 
switch7 = 0000000000000006
flow7msg = of.ofp_flow_mod() 
flow7msg.cookie = 0 
flow7msg.priority = 32768
# ACTIONS---------------------------------
flow7vlan_id = of.ofp_action_vlan_vid (vlan_vid = 10)
flow7out = of.ofp_action_output (port = 2)
flow7msg.actions = [flow7vlan_id, flow7out] 

def install_flows(): 
   log.info("    *** Installing static flows... ***")
   # Push flows to switches
   core.openflow.sendToDPID(switch0, flow0msg)
   core.openflow.sendToDPID(switch1, flow1msg)
   core.openflow.sendToDPID(switch2, flow2msg)
   core.openflow.sendToDPID(switch3, flow3msg)
   core.openflow.sendToDPID(switch4, flow4msg)
   core.openflow.sendToDPID(switch5, flow5msg)
   core.openflow.sendToDPID(switch6, flow6msg)
   core.openflow.sendToDPID(switch7, flow7msg)
   log.info("    *** Static flows installed. ***")

def launch (): 
   log.info("*** Starting... ***")
   core.callDelayed (15, install_flows)
   log.info("*** Waiting for switches to connect.. ***")
