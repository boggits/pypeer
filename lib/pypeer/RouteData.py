#!/usr/bin/env python


class RouteData:
    def __init__(self, routexml):
        self.routexml = routexml

    def prefix(self):
        return self.routexml.find('rt-destination').text + "/" + self.routexml.find('rt-prefix-length').text

    def activelocalpref(self):
        for bgp_path in self.routexml.findall('.//rt-entry'):
            if bgp_path.find('active-tag').text == '*':
                return int(bgp_path.find('local-preference').text)

    def aspath(self):
        for bgp_path in self.routexml.findall('.//rt-entry'):
            if bgp_path.find('active-tag').text == '*':
                list_aspath = bgp_path.find('as-path').text.split()
                clean_aspath = ''
                for asn in list_aspath:
                    if asn.isdigit():
                        if clean_aspath == '':
                            clean_aspath = asn
                        else:
                            clean_aspath = clean_aspath + " " + asn
                return clean_aspath
