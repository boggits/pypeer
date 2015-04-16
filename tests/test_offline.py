import sys, argparse
import os
from jnpr.junos import Device
from lxml import etree

sys.path.append('/home/andy/src/pypeer/lib')
sys.path.append('/Users/andy/src/pypeer/lib')
from pypeer.ConfigDictionary import ConfigDictionary
from pypeer.RouteData import RouteData
from pypeer.BgpData import BgpData

def test_username():
	config = ConfigDictionary('/Users/andy/src/pypeer/etc/example.ini')
	thisusername = config.username()
	assert thisusername == 'exampleuser' 

def test_can_find_rtr1():
	config = ConfigDictionary('/Users/andy/src/pypeer/etc/example.ini')
	assert config.get_router_ip('rtr1') == '91.194.69.4'

def test_can_read_prefix_from_route_object():
	resultxml = etree.fromstring(open('/Users/andy/src/pypeer/tests/test_data/bgp_route.xml').read())
	route = RouteData(resultxml.find('.//rt'))
	assert route.prefix() == '199.87.242.0/24'

def test_can_get_localpref_for_active_prefix():
	resultxml = etree.fromstring(open('/Users/andy/src/pypeer/tests/test_data/bgp_route.xml').read())
	route = RouteData(resultxml.find('.//rt'))
	assert route.activelocalpref() == 1000

def test_can_obtain_clean_aspath_for_route():
	resultxml = etree.fromstring(open('/Users/andy/src/pypeer/tests/test_data/bgp_route.xml').read())
	route = RouteData(resultxml.find('.//rt'))
	assert route.aspath() == '6939 6461 12536'

def test_can_parse_peering_localpref_range():
	config = ConfigDictionary('/Users/andy/src/pypeer/etc/example.ini')
	assert config.get_type_from_localpref(2500) == "peer"

def test_can_get_ipaddr_of_peer():
	resultxml = etree.fromstring(open('/Users/andy/src/pypeer/tests/test_data/bgp_summary.xml').read())
	bgpsum = BgpData(resultxml)
	assert bgpsum.get_list_ipaddr_from_asn(6939)[0] == '5.57.80.128'
