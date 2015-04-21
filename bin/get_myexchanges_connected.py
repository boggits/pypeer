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


def main():
    list_peeringdbid_of_connected_exchanges = []

    config = ConfigDictionary("/home/andy/etc/pypeer.ini")
    username = config.username()
    password = config.password()
    exchange = Exchange()
    peeringdb = PeeringDBClient()

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
        for thispeeringip in bgpsum.get_list_peering_ips():
            if not is_valid_ipv4_address(thispeeringip):
                next
            else:
                peeringdb_id = exchange.get_exchange_from_peerip(thispeeringip)['peeringdbid']
                if peeringdb_id==0:
                    next 
                elif peeringdb_id in list_peeringdbid_of_connected_exchanges:
                    next
                else:
                    list_peeringdbid_of_connected_exchanges.append(peeringdb_id)
                    print "%s: %s   # %s" % (peeringdb_id, router, peeringdb.get_name_of_ixp_from_pdbid(peeringdb_id))



if __name__ == "__main__":
    main()

