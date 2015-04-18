# pypeer
Lazy network operator.  Lazy.

# Install
```
sudo apt-get install -y python-setuptools python-dev libxml2-dev libxslt-dev python-pip
sudo pip install junos-eznc
sudo pip install pymysql
```

# Running

### Get missing BGP peer session adjancencies
```
python bin/get_missing_bgp_session_adj.py [-h] --asn BGPPEER
```

### Get peer status from ASN
python bin/get_peerstatus_from_asn.py [-h] --ipaddr IPADDR --asn BGPPEER [--machine]

### Get routes from session
```
python bin/get_routes_from_session.py [-h] --ipaddr IPADDR --bgppeer BGPPEER
```

# Running Tests
```
python tests/test_offline.py
python tests/test_online.py
```
 
