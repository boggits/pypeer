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
parser.add_argument('--bgppeer', dest='bgppeer', help='bgp peer address')

args = parser.parse_args()

device_ip = args.ipaddr
peer_ip = args.bgppeer

print (device_ip + " logging in as " + username)

jdev = Device(user=username, host=device_ip, password=password)
jdev.open(gather_facts=False)
jdev.timeout=600

try:
	resultxml = jdev.rpc.get_route_information(table='inet.0',protocol='bgp',peer=peer_ip,extensive=True)

except Exception as err:
	print "CMD:"   
	etree.dump(err.cmd)   
	print "RSP:"   
	etree.dump(err.rsp)

for route in resultxml.findall('.//rt'):
	full_prefix = route.find('rt-destination').text + "/" + route.find('rt-prefix-length').text
	print "destination: " + full_prefix

	list_aspath = route.find('rt-entry/as-path').text.split()
	clean_aspath = ''
	for asn in list_aspath:
		if asn.isdigit():
			clean_aspath = clean_aspath + " " + asn

	print "as-path: " + clean_aspath

jdev.close()



