

class RouteData:
	def __init__(self, routexml):
		self.routexml = routexml

	def prefix(self):
		return self.routexml.find('rt-destination').text + "/" + self.routexml.find('rt-prefix-length').text