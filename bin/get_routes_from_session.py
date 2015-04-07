import sys, argparse
sys.path.append('/home/andy/src/pypeer/lib')

from pypeer.ConfigDictionary import ConfigDictionary

config = ConfigDictionary()

username = config.username()
password = config.password()

parser = argparse.ArgumentParser(description='Dump a routing table as offered by a BGP neighbo(u)r')
parser.add_argument('--ipaddr', dest='ipaddr', help='bgp router ip address')
args = parser.parse_args()

print (args.ipaddr + " logging in as " + username)
