import ConfigParser, os

class ConfigDictionary:

	def __init__(self, configfile = '/home/andy/etc/pypeer.ini'):
		self.localconfig = ConfigParser.RawConfigParser()
		self.localconfig.read(configfile)

	def username(self):
		return self.localconfig.get("auth", "username")

	def password(self):
		return self.localconfig.get("auth", "password")

