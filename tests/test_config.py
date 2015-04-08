import sys, argparse
sys.path.append('/home/andy/src/pypeer/lib')

from pypeer.ConfigDictionary import ConfigDictionary

def test_username():
	config = ConfigDictionary('/home/andy/src/pypeer/etc/example.ini')
	thisusername = config.username()
	assert thisusername == 'exampleuser' 
