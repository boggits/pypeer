#!/usr/bin/env python

import ConfigParser


class ConfigDictionary:

    def __init__(self, configfile='./etc/example.ini'):
        self.localconfig = ConfigParser.RawConfigParser()
        self.localconfig.read(configfile)
        self.router_ip_dict = {}
        self.router_loc_dict = {}
        self.exchange_dict = {}
        router_items = self.localconfig.items("routers")
        for router, payload in router_items:
            (ip_addr, location) = payload.split(",")
            self.router_ip_dict[router] = ip_addr
            self.router_loc_dict[router] = location
        exchange_items = self.localconfig.items("myexchanges")
        for exchange_id, exchange_router in exchange_items:
            self.exchange_dict[int(exchange_id)] = exchange_router

    def username(self):
        return self.localconfig.get("auth", "username")

    def password(self):
        return self.localconfig.get("auth", "password")

    def get_router_ip(self, router_name):
        return self.router_ip_dict[router_name]

    def get_list_of_router_names(self):
        return self.router_ip_dict.keys()

    def get_type_from_localpref(self, localpref):
        transitconfig = self.localconfig.get("localprefrange", "transit")
        peerconfig = self.localconfig.get("localprefrange", "peer")
        custconfig = self.localconfig.get("localprefrange", "customer")
        transitmin, transitmax = transitconfig.split('-')
        peermin, peermax = peerconfig.split('-')
        custmin, custmax = custconfig.split('-')
        transitrange = range(int(transitmin), int(transitmax))
        peerrange = range(int(peermin), int(peermax))
        custrange = range(int(custmin), int(custmax))
        if localpref in transitrange:
            return "transit"
        if localpref in peerrange:
            return "peer"
        if localpref in custrange:
            return "customer"
        return "outofrange"

    def get_list_of_connected_exchanges(self):
        return self.exchange_dict.keys()
