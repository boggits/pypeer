import ConfigParser, os

class ConfigDictionary:

	def __init__(self, configfile = '/home/andy/etc/pypeer.ini'):
		self.localconfig = ConfigParser.RawConfigParser()
		self.localconfig.read(configfile)
		self.router_ip_dict  = {}
		self.router_loc_dict = {}
		router_items = self.localconfig.items("routers")
		for router, payload in router_items:
			(ip_addr, location) = payload.split(",")
			self.router_ip_dict[router] = ip_addr
			self.router_loc_dict[router] = location

	def username(self):
		return self.localconfig.get("auth", "username")

	def password(self):
		return self.localconfig.get("auth", "password")

	def get_router_ip(self, router_name):
		return self.router_ip_dict[router_name]