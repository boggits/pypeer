import sys, argparse
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