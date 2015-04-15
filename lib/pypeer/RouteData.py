

class RouteData:
	def __init__(self, routexml):
		self.routexml = routexml

	def prefix(self):
		return self.routexml.find('rt-destination').text + "/" + self.routexml.find('rt-prefix-length').text

	def activelocalpref(self):
		for bgp_path in self.routexml.findall('.//rt-entry'):
			if bgp_path.find('active-tag').text == '*':
				return bgp_path.find('local-preference').text
