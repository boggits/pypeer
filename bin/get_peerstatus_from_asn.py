import sys, argparse
from lxml import etree
import json

sys.path.append('/home/andy/src/pypeer/lib')

from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable 

from pypeer.ConfigDictionary import ConfigDictionary
from pypeer.RouteData import RouteData

config = ConfigDictionary()

username = config.username()
password = config.password()

parser = argparse.ArgumentParser(description='Inspect a routing table to enquire the number of peer/transit/customer adjacencies for a given ASN')
parser.add_argument('--ipaddr', dest='ipaddr', help='bgp router ip address')
parser.add_argument('--asn', dest='bgppeer', help='bgp origin asn')
parser.add_argument('--machine', '-m', help='machine readable output', dest='output', action='store_const', const='machine')

args = parser.parse_args()

device_ip = args.ipaddr
peer_asn  = args.bgppeer

jdev = Device(user=username, host=device_ip, password=password)
jdev.open(gather_facts=False)
jdev.timeout=600
regex_asn = ".* " + peer_asn

try:
	resultxml = jdev.rpc.get_route_information(table='inet.0',aspath_regex=regex_asn,extensive=True)

except Exception as err:
	print "CMD:"   
	etree.dump(err.cmd)   
	print "RSP:"   
	etree.dump(err.rsp)

jdev.close()

sorted_routes = {}
sorted_routes["peer"]=[]
sorted_routes["transit"]=[]
sorted_routes["customer"]=[]
sorted_routes["outofrange"]=[]

for routexml in resultxml.findall('.//rt'):
	route = RouteData(routexml)
	full_prefix = route.prefix()
	session_type  = config.get_type_from_localpref(route.activelocalpref())
	sorted_routes[session_type].append(full_prefix)

if args.output == 'machine':
	print json.dumps(sorted_routes)
else:
	print "Number of routes: " + str(len(sorted_routes["peer"])) + " via peering, " + str(len(sorted_routes["customer"])) + " via customer, and " + str(len(sorted_routes["transit"])) + " via transit. (use -m for full output and breakdown)"
