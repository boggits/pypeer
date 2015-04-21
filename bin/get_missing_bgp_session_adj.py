#!/usr/bin/env python
import argparse
import sys
from lxml import etree

sys.path.append('./lib')

from jnpr.junos import Device

from pypeer.ConfigDictionary import ConfigDictionary
from pypeer.BgpData import BgpData
from pypeer.Exchange import Exchange
from pypeer.PeeringDBClient import PeeringDBClient

import socket


def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True


def main(peer_asn):
    list_peering_ips_of_target_asn = []

    config = ConfigDictionary("/home/andy/etc/pypeer.ini")
    username = config.username()
    password = config.password()

    for router in config.get_list_of_router_names():
        jdev = Device(user=username, host=config.get_router_ip(router),
                      password=password)
        jdev.open(gather_facts=False)
        jdev.timeout = 600

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
        if not is_valid_ipv4_address(peering_ip):
            next
        else:
            peeringdb_id = exchange.get_exchange_from_peerip(peering_ip)['peeringdbid']
            list_sessions_configured_peeringdbid_exchanges_of_target_asn.append(peeringdb_id)

    peeringdb = PeeringDBClient()
    list_their_exchanges = peeringdb.get_list_connected_ixp(peer_asn)

    mutual_exchanges = set(config.get_list_of_connected_exchanges()).intersection(list_their_exchanges)
    missing_exchanges = set(mutual_exchanges).difference(list_sessions_configured_peeringdbid_exchanges_of_target_asn)

    print "Missing exchanges are:" + str(missing_exchanges)

    for pdbid in missing_exchanges:
        print str(pdbid) + ": " + peeringdb.get_name_of_ixp_from_pdbid(pdbid)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Inspect a router estate and identify missing opportunities to peer with an asn')
    parser.add_argument('--asn', dest='bgppeer', help='bgp peer asn', required=True)
    args = parser.parse_args()
    peer_asn = args.bgppeer
    main(peer_asn)
