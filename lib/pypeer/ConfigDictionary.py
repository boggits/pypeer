import ConfigParser, os

class ConfigDictionary:

	def __init__(self):
		self.localconfig = ConfigParser.RawConfigParser()
		self.localconfig.read("/home/andy/etc/pypeer.ini")

	def username(self):
		return self.localconfig.get("auth", "username")

	def password(self):
		return self.localconfig.get("auth", "password")

