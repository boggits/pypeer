import sys, argparse
from jnpr.junos import Device

sys.path.append('./lib')

from pypeer.ConfigDictionary import ConfigDictionary

import unittest

class OnlineTests(unittest.TestCase):
    def test_can_login_parse_serial(self):
    	config = ConfigDictionary('./etc/example.ini')
    	jdev = Device(user=config.username(), host=config.get_router_ip('rtr1'), password=config.password())
    	jdev.open(gather_facts=False)
    	inv = jdev.rpc.get_chassis_inventory()
    	print "model: %s" % inv.findtext('.//chassis/description')
    	jdev.close()
    	assert inv.findtext('.//chassis/description') == 'VMX'

if __name__ == "__main__":
    unittest.main()