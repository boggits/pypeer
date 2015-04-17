import sys
import pymysql

class PeeringDBClient:
	def __init__(self):
		self.db = pymysql.connect(host='peeringdb.com', port=3306, user='peeringdb', passwd='peeringdb', db='Peering')

	def get_list_connected_ixp(self, asn):
		list_of_ixps = []
		cur = self.db.cursor()
		cur.execute("SELECT public_id FROM peerParticipantsPublics WHERE local_asn=%s", asn)
		for row in cur.fetchall():
			list_of_ixps.append(int(row[0]))
		return list_of_ixps
