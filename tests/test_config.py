import sys, argparse
from jnpr.junos import Device

sys.path.append('/home/andy/src/pypeer/lib')
sys.path.append('/Users/andy/src/pypeer/lib')
from pypeer.ConfigDictionary import ConfigDictionary

def test_username():
	config = ConfigDictionary('/Users/andy/src/pypeer/etc/example.ini')
	thisusername = config.username()
	assert thisusername == 'exampleuser' 

def test_can_find_rtr1():
	config = ConfigDictionary('/Users/andy/src/pypeer/etc/example.ini')
	assert config.get_router_ip('rtr1') == '91.194.69.4'

def test_can_login_parse_serial():
	config = ConfigDictionary('/Users/andy/src/pypeer/etc/example.ini')
	jdev = Device(user=config.username(), host=config.get_router_ip('rtr1'), password=config.password())
	jdev.open(gather_facts=False)
	inv = jdev.rpc.get_chassis_inventory()
	print "model: %s" % inv.findtext('.//chassis/description')
	jdev.close()
	assert inv.findtext('.//chassis/description') == 'VMX'
