#!/usr/bin/env python

import sys
from lxml import etree

sys.path.append('./lib')

from pypeer.ConfigDictionary import ConfigDictionary
from pypeer.RouteData import RouteData
from pypeer.BgpData import BgpData
from pypeer.Exchange import Exchange
from pypeer.PeeringDBClient import PeeringDBClient

import unittest
# Can run with -a '!internet' when offline to skip peeringdb shit tests.


class OfflineTests(unittest.TestCase):
    def test_username(self):
        config = ConfigDictionary('./etc/example.ini')
        thisusername = config.username()
        self.assertTrue(thisusername == 'exampleuser')

    def test_can_find_rtr1_ipaddr(self):
        config = ConfigDictionary('./etc/example.ini')
        self.assertTrue(config.get_router_ip('rtr1') == '91.194.69.4')

    def test_can_see_rtr2_in_list_of_routers(self):
        config = ConfigDictionary('./etc/example.ini')
        self.assertTrue("rtr2" in config.get_list_of_router_names())

    def test_can_read_prefix_from_route_object(self):
        resultxml = etree.fromstring(open('./tests/test_data/bgp_route.xml').read())
        route = RouteData(resultxml.find('.//rt'))
        self.assertTrue(route.prefix() == '199.87.242.0/24')

    def test_can_get_localpref_for_active_prefix(self):
        resultxml = etree.fromstring(open('./tests/test_data/bgp_route.xml').read())
        route = RouteData(resultxml.find('.//rt'))
        self.assertTrue(route.activelocalpref() == 1000)

    def test_can_obtain_clean_aspath_for_route(self):
        resultxml = etree.fromstring(open('./tests/test_data/bgp_route.xml').read())
        route = RouteData(resultxml.find('.//rt'))
        self.assertTrue(route.aspath() == '6939 6461 12536')

    def test_can_parse_peering_localpref_range(self):
        config = ConfigDictionary('./etc/example.ini')
        self.assertTrue(config.get_type_from_localpref(2500) == "peer")

    def test_can_get_ipaddr_of_peer(self):
        resultxml = etree.fromstring(open('./tests/test_data/bgp_summary.xml').read())
        bgpsum = BgpData(resultxml)
        self.assertTrue(bgpsum.get_list_ipaddr_from_asn(6939)[0] == '5.57.80.128')

    def test_can_detect_exchange_of_peer(self):
        resultxml = etree.fromstring(open('./tests/test_data/bgp_summary.xml').read())
        bgpsum = BgpData(resultxml)
        exchange = Exchange()
        self.assertTrue(exchange.get_exchange_from_peerip(bgpsum.get_list_ipaddr_from_asn(6939)[0])['name'] == 'LONAP')

    def test_can_get_list_of_connected_exchanges(self):
        config = ConfigDictionary('./etc/example.ini')
        self.assertTrue("18" in config.get_list_of_connected_exchanges())

#   @unittest.skip("Offline!")
    def test_can_obtain_list_of_connected_exchanges_from_peeringdb(self):
        peeringdb = PeeringDBClient()
        self.assertTrue(53 in peeringdb.get_list_connected_ixp(12536))

#   @unittest.skip("Offline!")
    def test_can_get_name_of_IXP(self):
        peeringdb = PeeringDBClient()
        self.assertTrue("LINX Juniper LAN (London Internet Exchange Ltd.)" == peeringdb.get_name_of_ixp_from_pdbid(18))


if __name__ == "__main__":
    unittest.main()
