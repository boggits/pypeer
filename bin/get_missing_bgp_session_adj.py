import sys, argparse
from lxml import etree
import json

sys.path.append('/home/andy/src/pypeer/lib')

from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable 

from pypeer.ConfigDictionary import ConfigDictionary
from pypeer.RouteData import RouteData
from pypeer.BgpData import BgpData
from pypeer.Exchange import Exchange
from pypeer.PeeringDBClient import PeeringDBClient

config = ConfigDictionary()
username = config.username()
password = config.password()

parser = argparse.ArgumentParser(description='Inspect a router estate and identify missing opportunities to peer with an asn')
parser.add_argument('--asn', dest='bgppeer', help='bgp peer asn')
args = parser.parse_args()
peer_asn  = args.bgppeer

list_peering_ips_of_target_asn = []

for router in config.get_list_of_router_names():
	jdev = Device(user=username, host=config.get_router_ip(router), password=password)
	jdev.open(gather_facts=False)
	jdev.timeout=600

	try:
		resultxml = jdev.rpc.get_bgp_summary_information()
	except Exception as err:
		print "CMD:"   
		etree.dump(err.cmd)   
		print "RSP:"   
		etree.dump(err.rsp)

	bgpsum = BgpData(resultxml)
	for thispeeringip in bgpsum.get_list_ipaddr_from_asn(peer_asn):
		list_peering_ips_of_target_asn.append(thispeeringip)

exchange = Exchange()
list_sessions_configured_peeringdbid_exchanges_of_target_asn = []
for peering_ip in list_peering_ips_of_target_asn:
	print "peering ip found: " + peering_ip
	peeringdb_id = exchange.get_exchange_from_peerip(peering_ip)['peeringdbid']
	list_sessions_configured_peeringdbid_exchanges_of_target_asn.append(peeringdb_id)

# todo: pull this from config file
list_my_exchanges = [26, 806, 87, 59, 33, 31, 804, 1, 255, 5, 359, 48, 387, 435, 583, 745, 18, 777, 53, 297, 35, 70, 64, 60, 325, 587]

peeringdb = PeeringDBClient()
list_their_exchanges = peeringdb.get_list_connected_ixp(peer_asn)

mutual_exchanges = set(list_my_exchanges).intersection(list_their_exchanges)
missing_exchanges = set(mutual_exchanges).difference(list_sessions_configured_peeringdbid_exchanges_of_target_asn)

print "Missing exchanges are:" + missing_exchanges
