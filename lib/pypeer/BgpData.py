class BgpData:
	def __init__(self, bgpsumxml):
		self.bgpxml = bgpsumxml

	def get_list_ipaddr_from_asn(self, asn):
		list_peer_ip=[]
		for bgp_sum in self.bgpxml.findall('.//bgp-peer'):
			if bgp_sum.find('peer-as').text == str(asn):
				list_peer_ip.append(bgp_sum.find('peer-address').text)
		return list_peer_ip

