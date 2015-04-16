import sys, argparse
from lxml import etree

sys.path.append('/home/andy/src/pypeer/lib')

from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable 

from pypeer.ConfigDictionary import ConfigDictionary

config = ConfigDictionary()

username = config.username()
password = config.password()

parser = argparse.ArgumentParser(description='Dump a routing table as offered by a BGP neighbo(u)r')
parser.add_argument('--ipaddr', dest='ipaddr', help='bgp router ip address')
parser.add_argument('--asn', dest='bgppeer', help='bgp origin asn')

args = parser.parse_args()

device_ip = args.ipaddr
peer_asn  = args.bgppeer

print (device_ip + " logging in as " + username)

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

for routexml in resultxml.findall('.//rt'):
	route = RouteData(routexml)
	full_prefix = route.prefix()
	session_type  = config.get_type_from_localpref(route.activelocalpref())
	print "destination: " + full_prefix + "localpref: " + session_type

jdev.close()
