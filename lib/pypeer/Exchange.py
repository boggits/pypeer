from netaddr import *
# Hacky auto generated

class Exchange:
	def __init__(self):
		return

	def get_exchange_from_peerip(self, peerip):
		ip = IPAddress(peerip)
		ipnum = int(ip)
		ixp = {}
		if ipnum==0:
			return 'error'
		elif 1729127936 <= ipnum <= 1729128447:    # SGIX does have ip prefix 103.16.102.0/23
			ixp['peeringdbid'] = 429
			ixp['city']        = "Singapore"
			ixp['name']        = "SGIX"
			ixp['name_long']   = "Singapore Internet Exchange"
			return ixp
		elif 1728214016 <= ipnum <= 1728214271:    # IX Australia QLD does have ip prefix 103.2.116.0/24
			ixp['peeringdbid'] = 576
			ixp['city']        = "Brisbane/Queensland"
			ixp['name']        = "IX Australia QLD"
			ixp['name_long']   = "Queensland Internet Exchange (QLD-IX)"
			return ixp
		elif 1743230976 <= ipnum <= 1743231999:    # BBIX Hong Kong / Singapore does have ip prefix 103.231.152.0/22
			ixp['peeringdbid'] = 909
			ixp['city']        = "Hong Kong / Singapore"
			ixp['name']        = "BBIX Hong Kong / Singapore"
			ixp['name_long']   = "BroadBand Internet eXchange Hong Kong / Singapore"
			return ixp
		elif 1744234496 <= ipnum <= 1744234751:    # JPIX OSAKA does have ip prefix 103.246.232.0/24
			ixp['peeringdbid'] = 564
			ixp['city']        = "Osaka"
			ixp['name']        = "JPIX OSAKA"
			ixp['name_long']   = "Japan Internet Exchange Osaka"
			return ixp
		elif 1744276224 <= ipnum <= 1744276351:    # AMS-IX Hong Kong does have ip prefix 103.247.139.0/25
			ixp['peeringdbid'] = 577
			ixp['city']        = "Hong Kong"
			ixp['name']        = "AMS-IX Hong Kong"
			ixp['name_long']   = "Amsterdam Internet Exchange Hong Kong"
			return ixp
		elif 1729750016 <= ipnum <= 1729750271:    # VIX.VU does have ip prefix 103.25.228.0/24
			ixp['peeringdbid'] = 971
			ixp['city']        = "Port Vila"
			ixp['name']        = "VIX.VU"
			ixp['name_long']   = "Vanuatu Internet Exchange"
			return ixp
		elif 1729774592 <= ipnum <= 1729775103:    # Megaport-IX Sydney does have ip prefix 103.26.68.0/23
			ixp['peeringdbid'] = 780
			ixp['city']        = "Sydney"
			ixp['name']        = "Megaport-IX Sydney"
		elif 1729775104 <= ipnum <= 1729775359:    # Megaport-IX Brisbane does have ip prefix 103.26.70.0/24
			ixp['peeringdbid'] = 781
			ixp['city']        = "Brisbane"
			ixp['name']        = "Megaport-IX Brisbane"
		elif 1729775360 <= ipnum <= 1729775615:    # Megaport-IX Melbourne does have ip prefix 103.26.71.0/24
			ixp['peeringdbid'] = 779
			ixp['city']        = "Victoria"
			ixp['name']        = "Megaport-IX Melbourne"
		elif 1730743296 <= ipnum <= 1730744319:    # Megaport IX Singapore does have ip prefix 103.41.12.0/22
			ixp['peeringdbid'] = 965
			ixp['city']        = "Singapore"
			ixp['name']        = "Megaport IX Singapore"
		elif 1731211264 <= ipnum <= 1731211775:    # Megaport IX Hong Kong does have ip prefix 103.48.48.0/23
			ixp['peeringdbid'] = 1037
			ixp['city']        = "Hong Kong"
			ixp['name']        = "Megaport IX Hong Kong"
		elif 2003727104 <= ipnum <= 2003727359:    # MCIX - Matrix Networks does have ip prefix 119.110.115.0/24
			ixp['peeringdbid'] = 469
			ixp['city']        = "Jakarta"
			ixp['name']        = "MCIX - Matrix Networks"
			ixp['name_long']   = "Matrix Cable Internet eXchange"
			return ixp
		elif 2003727360 <= ipnum <= 2003727871:    # MCIX - Matrix Networks does have ip prefix 119.110.116.0/23
			ixp['peeringdbid'] = 469
			ixp['city']        = "Jakarta"
			ixp['name']        = "MCIX - Matrix Networks"
			ixp['name_long']   = "Matrix Cable Internet eXchange"
			return ixp
		elif 2003727872 <= ipnum <= 2003728127:    # MCIX - Matrix Networks does have ip prefix 119.110.118.0/24
			ixp['peeringdbid'] = 469
			ixp['city']        = "Jakarta"
			ixp['name']        = "MCIX - Matrix Networks"
			ixp['name_long']   = "Matrix Cable Internet eXchange"
			return ixp
		elif 1998274304 <= ipnum <= 1998274559:    # Equinix Hong Kong does have ip prefix 119.27.63.0/24
			ixp['peeringdbid'] = 125
			ixp['city']        = "Hong Kong"
			ixp['name']        = "Equinix Hong Kong"
			ixp['name_long']   = "Equinix Hong Kong"
			return ixp
		elif 2422008288 <= ipnum <= 2422008319:    # MadIX does have ip prefix 144.92.233.224/27
			ixp['peeringdbid'] = 89
			ixp['city']        = "Madison"
			ixp['name']        = "MadIX"
			ixp['name_long']   = "Madison Internet Exchange"
			return ixp
		elif 2987581440 <= ipnum <= 2987581951:    # DATAIX does have ip prefix 178.18.224.0/23
			ixp['peeringdbid'] = 358
			ixp['city']        = "St.Petersburg,Moscow,Ekaterinburg,Novosibirs,Omsk,Khabarovsk/RU."
			ixp['name']        = "DATAIX"
			ixp['name_long']   = "Peering, LTD"
			return ixp
		elif 2987582976 <= ipnum <= 2987583231:    # DATAIX does have ip prefix 178.18.230.0/24
			ixp['peeringdbid'] = 358
			ixp['city']        = "St.Petersburg,Moscow,Ekaterinburg,Novosibirs,Omsk,Khabarovsk/RU."
			ixp['name']        = "DATAIX"
			ixp['name_long']   = "Peering, LTD"
			return ixp
		elif 2987583488 <= ipnum <= 2987583743:    # DATAIX does have ip prefix 178.18.232.0/24 
			ixp['peeringdbid'] = 358
			ixp['city']        = "St.Petersburg,Moscow,Ekaterinburg,Novosibirs,Omsk,Khabarovsk/RU."
			ixp['name']        = "DATAIX"
			ixp['name_long']   = "Peering, LTD"
			return ixp
		elif 2987583744 <= ipnum <= 2987583999:    # DATAIX does have ip prefix 178.18.233.0/24
			ixp['peeringdbid'] = 358
			ixp['city']        = "St.Petersburg,Moscow,Ekaterinburg,Novosibirs,Omsk,Khabarovsk/RU."
			ixp['name']        = "DATAIX"
			ixp['name_long']   = "Peering, LTD"
			return ixp
		elif 3103854336 <= ipnum <= 3103854591:    # SH-IX does have ip prefix 185.1.15.0/24
			ixp['peeringdbid'] = 866
			ixp['city']        = "Fujairah, UAE"
			ixp['name']        = "SH-IX"
			ixp['name_long']   = "SMARTHUB Internet Exchange"
			return ixp
		elif 3103855104 <= ipnum <= 3103855359:    # DO-IX does have ip prefix 185.1.18.0/24
			ixp['peeringdbid'] = 762
			ixp['city']        = "Dortmund"
			ixp['name']        = "DO-IX"
			ixp['name_long']   = "Dortmund Internet eXchange"
			return ixp
		elif 3103858176 <= ipnum <= 3103858431:    # B-IX does have ip prefix 185.1.30.0/24
			ixp['peeringdbid'] = 326
			ixp['city']        = "Sofia"
			ixp['name']        = "B-IX"
			ixp['name_long']   = "Balkan Internet Exchange"
			return ixp
		elif 3103858432 <= ipnum <= 3103858687:    # Tirol-IX does have ip prefix 185.1.31.0/24
			ixp['peeringdbid'] = 1009
			ixp['city']        = "Innsbruck/Tirol"
			ixp['name']        = "Tirol-IX"
			ixp['name_long']   = "Tirol-IX Internet Exchange"
			return ixp
		elif 3103859456 <= ipnum <= 3103859711:    # BREM-IX does have ip prefix 185.1.35.0/24
			ixp['peeringdbid'] = 796
			ixp['city']        = "Bremen"
			ixp['name']        = "BREM-IX"
			ixp['name_long']   = "BREM-IX"
			return ixp
		elif 3103852544 <= ipnum <= 3103852799:    # UAE-IX does have ip prefix 185.1.8.0/24
			ixp['peeringdbid'] = 587
			ixp['city']        = "Dubai, UAE"
			ixp['name']        = "UAE-IX"
			ixp['name_long']   = "UAE Internet Exchange"
			return ixp
		elif 3138437120 <= ipnum <= 3138437375:    # PTT-SJC does have ip prefix 187.16.192.0/24
			ixp['peeringdbid'] = 638
			ixp['city']        = "Sao Jose dos Campos/SP"
			ixp['name']        = "PTT-SJC"
			ixp['name_long']   = "PTT Sao Jose dos Campos"
			return ixp
		elif 3138437376 <= ipnum <= 3138437631:    # PTT-AME does have ip prefix 187.16.193.0/24
			ixp['peeringdbid'] = 418
			ixp['city']        = "Americana/SP"
			ixp['name']        = "PTT-AME"
			ixp['name_long']   = "PTT Americana"
			return ixp
		elif 3138437632 <= ipnum <= 3138437887:    # PTT-VIX does have ip prefix 187.16.194.0/24
			ixp['peeringdbid'] = 706
			ixp['city']        = "Vitoria/ES"
			ixp['name']        = "PTT-VIX"
			ixp['name_long']   = "PTT Vitoria"
			return ixp
		elif 3138437888 <= ipnum <= 3138438143:    # PTT-BEL does have ip prefix 187.16.195.0/24
			ixp['peeringdbid'] = 711
			ixp['city']        = "Belem/PA"
			ixp['name']        = "PTT-BEL"
			ixp['name_long']   = "PTT Belem"
			return ixp
		elif 3138438144 <= ipnum <= 3138438399:    # PTT-NAT does have ip prefix 187.16.196.0/24
			ixp['peeringdbid'] = 708
			ixp['city']        = "Natal/RN"
			ixp['name']        = "PTT-NAT"
			ixp['name_long']   = "PTT Natal"
			return ixp
		elif 3138438400 <= ipnum <= 3138438655:    # PTT-CXJ does have ip prefix 187.16.197.0/24
			ixp['peeringdbid'] = 558
			ixp['city']        = "Caxias do Sul/RS"
			ixp['name']        = "PTT-CXJ"
			ixp['name_long']   = "PTT Caxias do Sul"
			return ixp
		elif 3138438656 <= ipnum <= 3138438911:    # PTT-MAO does have ip prefix 187.16.198.0/24
			ixp['peeringdbid'] = 707
			ixp['city']        = "Manaus/AM"
			ixp['name']        = "PTT-MAO"
			ixp['name_long']   = "PTT Manaus"
			return ixp
		elif 3138438912 <= ipnum <= 3138439167:    # PTT-SJP does have ip prefix 187.16.199.0/24
			ixp['peeringdbid'] = 709
			ixp['city']        = "Sao Jose do Rio Preto/SP"
			ixp['name']        = "PTT-SJP"
			ixp['name_long']   = "PTT Sao Jose do Rio Preto"
			return ixp
		elif 3138443264 <= ipnum <= 3138445311:    # PTT-SP does have ip prefix 187.16.216.0/21
			ixp['peeringdbid'] = 171
			ixp['city']        = "Sao Paulo/SP"
			ixp['name']        = "PTT-SP"
			ixp['name_long']   = "PTT Sao Paulo"
			return ixp
		elif 3161730304 <= ipnum <= 3161730559:    # GIX Gdansk does have ip prefix 188.116.45.0/24
			ixp['peeringdbid'] = 498
			ixp['city']        = "Gdansk"
			ixp['name']        = "GIX Gdansk"
			ixp['name_long']   = "Gdansk Internet eXchange"
			return ixp
		elif 3228341248 <= ipnum <= 3228341503:    # SIX.SK does have ip prefix 192.108.148.0/24
			ixp['peeringdbid'] = 84
			ixp['city']        = "Bratislava"
			ixp['name']        = "SIX.SK"
			ixp['name_long']   = "Slovak Internet Exchange"
			return ixp
		elif 3229175808 <= ipnum <= 3229176063:    # STHIX does have ip prefix 192.121.80.0/24
			ixp['peeringdbid'] = 172
			ixp['city']        = "Stockholm"
			ixp['name']        = "STHIX"
			ixp['name_long']   = "Stockholm Internet eXchange"
			return ixp
		elif 3232238080 <= ipnum <= 3232238335:    # MOZIX does have ip prefix 192.168.10.0/24
			ixp['peeringdbid'] = 528
			ixp['city']        = "Maputo"
			ixp['name']        = "MOZIX"
			ixp['name_long']   = "Mozambique Internet Exchange"
			return ixp
		elif 3234568704 <= ipnum <= 3234568959:    # APE does have ip prefix 192.203.154.0/24
			ixp['peeringdbid'] = 97
			ixp['city']        = "Auckland"
			ixp['name']        = "APE"
			ixp['name_long']   = "Auckland Peering Exchange"
			return ixp
		elif 3223717632 <= ipnum <= 3223717887:    # DIX does have ip prefix 192.38.7.0/24
			ixp['peeringdbid'] = 78
			ixp['city']        = "Copenhagen"
			ixp['name']        = "DIX"
			ixp['name_long']   = "Danish Internet Exchange"
			return ixp
		elif 3225532672 <= ipnum <= 3225532927:    # CIXP does have ip prefix 192.65.185.0/24
			ixp['peeringdbid'] = 33
			ixp['city']        = "Geneva"
			ixp['name']        = "CIXP"
			ixp['name_long']   = "CERN Internet eXchange Point"
			return ixp
		elif 3244913664 <= ipnum <= 3244913919:    # Content-IX does have ip prefix 193.105.116.0/24
			ixp['peeringdbid'] = 536
			ixp['city']        = "Copenhagen"
			ixp['name']        = "Content-IX"
			ixp['name_long']   = "GlobalConnect Content-IX"
			return ixp
		elif 3244925696 <= ipnum <= 3244925951:    # SOX d.o.o. Serbia does have ip prefix 193.105.163.0/24
			ixp['peeringdbid'] = 424
			ixp['city']        = "Belgrade/Serbia"
			ixp['name']        = "SOX d.o.o. Serbia"
			ixp['name_long']   = "Serbian Open eXchange"
			return ixp
		elif 3244938752 <= ipnum <= 3244939007:    # GraX does have ip prefix 193.105.214.0/24
			ixp['peeringdbid'] = 430
			ixp['city']        = "Graz"
			ixp['name']        = "GraX"
			ixp['name_long']   = "Grazer Internet eXchange"
			return ixp
		elif 3245202176 <= ipnum <= 3245202431:    # LIPEX does have ip prefix 193.109.219.0/24
			ixp['peeringdbid'] = 49
			ixp['city']        = "London"
			ixp['name']        = "LIPEX"
			ixp['name_long']   = "London Internet Providers Exchange"
			return ixp
		elif 3245214720 <= ipnum <= 3245214975:    # SOL-IX / SOLIX does have ip prefix 193.110.12.0/24
			ixp['peeringdbid'] = 128
			ixp['city']        = "Stockholm"
			ixp['name']        = "SOL-IX / SOLIX"
			ixp['name_long']   = "Stockholm Open Local Internet Exchange"
			return ixp
		elif 3245214976 <= ipnum <= 3245215231:    # SOL-IX / SOLIX does have ip prefix 193.110.13.0/24
			ixp['peeringdbid'] = 128
			ixp['city']        = "Stockholm"
			ixp['name']        = "SOL-IX / SOLIX"
			ixp['name_long']   = "Stockholm Open Local Internet Exchange"
			return ixp
		elif 3245268992 <= ipnum <= 3245269247:    # FICIX does have ip prefix 193.110.224.0/24
			ixp['peeringdbid'] = 98
			ixp['city']        = "Helsinki"
			ixp['name']        = "FICIX"
			ixp['name_long']   = "Finnish Communication and Internet Exchange"
			return ixp
		elif 3245321216 <= ipnum <= 3245321471:    # GN-IX does have ip prefix 193.111.172.0/24
			ixp['peeringdbid'] = 76
			ixp['city']        = "Groningen"
			ixp['name']        = "GN-IX"
			ixp['name_long']   = "Groningen Internet Exchange"
			return ixp
		elif 3246979584 <= ipnum <= 3246979839:    # GigaPix does have ip prefix 193.136.250.0/24
			ixp['peeringdbid'] = 72
			ixp['city']        = "Lisbon"
			ixp['name']        = "GigaPix"
			ixp['name_long']   = "GIGAbit Portuguese Internet eXchange"
			return ixp
		elif 3247054592 <= ipnum <= 3247054847:    # S-IX does have ip prefix 193.138.31.0/24
			ixp['peeringdbid'] = 212
			ixp['city']        = "Stuttgart"
			ixp['name']        = "S-IX"
			ixp['name_long']   = "Stuttgarter Internet eXchange"
			return ixp
		elif 3247767808 <= ipnum <= 3247767935:    # ESPANIX does have ip prefix 193.149.1.0/25
			ixp['peeringdbid'] = 63
			ixp['city']        = "Madrid"
			ixp['name']        = "ESPANIX"
			ixp['name_long']   = "Espana Internet Exchange"
			return ixp
		elif 3247767936 <= ipnum <= 3247768063:    # ESPANIX does have ip prefix 193.149.1.128/25
			ixp['peeringdbid'] = 63
			ixp['city']        = "Madrid"
			ixp['name']        = "ESPANIX"
			ixp['name_long']   = "Espana Internet Exchange"
			return ixp
		elif 3248257024 <= ipnum <= 3248257279:    # NIX2 does have ip prefix 193.156.120.0/24
			ixp['peeringdbid'] = 298
			ixp['city']        = "Oslo"
			ixp['name']        = "NIX2"
			ixp['name_long']   = "Norwegian Internet Exchange (location 2)"
			return ixp
		elif 3248249344 <= ipnum <= 3248249599:    # NIX does have ip prefix 193.156.90.0/24
			ixp['peeringdbid'] = 83
			ixp['city']        = "Oslo"
			ixp['name']        = "NIX"
			ixp['name_long']   = "Norwegian Internet Exchange"
			return ixp
		elif 3249045248 <= ipnum <= 3249045503:    # LIX does have ip prefix 193.168.127.0/24
			ixp['peeringdbid'] = 77
			ixp['city']        = "Luxemburg"
			ixp['name']        = "LIX"
			ixp['name_long']   = "Luxemburg Internet Exchange"
			return ixp
		elif 3249128960 <= ipnum <= 3249129471:    # BIX.BG does have ip prefix 193.169.198.0/23
			ixp['peeringdbid'] = 331
			ixp['city']        = "Sofia"
			ixp['name']        = "BIX.BG"
			ixp['name_long']   = "Bulgarian Internet eXchange"
			return ixp
		elif 3239136768 <= ipnum <= 3239137023:    # MD-IX does have ip prefix 193.17.78.0/24
			ixp['peeringdbid'] = 392
			ixp['city']        = "Chisinau"
			ixp['name']        = "MD-IX"
			ixp['name_long']   = "Internet eXchange Moldova"
			return ixp
		elif 3249715456 <= ipnum <= 3249715711:    # BCIX does have ip prefix 193.178.185.0/24
			ixp['peeringdbid'] = 87
			ixp['city']        = "Berlin"
			ixp['name']        = "BCIX"
			ixp['name_long']   = "Berlin Commercial Internet Exchange"
			return ixp
		elif 3250358528 <= ipnum <= 3250358783:    # BiX does have ip prefix 193.188.137.0/24
			ixp['peeringdbid'] = 55
			ixp['city']        = "Budapest"
			ixp['name']        = "BiX"
			ixp['name_long']   = "Budapest Internet Exchange"
			return ixp
		elif 3250422272 <= ipnum <= 3250422527:    # ENLIX does have ip prefix 193.189.130.0/24
			ixp['peeringdbid'] = 208
			ixp['city']        = "Manchester"
			ixp['name']        = "ENLIX"
			ixp['name_long']   = "Enlightened Internet Exchange"
			return ixp
		elif 3250409984 <= ipnum <= 3250410495:    # KleyReX does have ip prefix 193.189.82.0/23
			ixp['peeringdbid'] = 123
			ixp['city']        = "Frankfurt"
			ixp['name']        = "KleyReX"
			ixp['name_long']   = "KleyReX"
			return ixp
		elif 3250589504 <= ipnum <= 3250589567:    # CIX does have ip prefix 193.192.15.64/26
			ixp['peeringdbid'] = 303
			ixp['city']        = "Zagreb"
			ixp['name']        = "CIX"
			ixp['name_long']   = "Croatian Internet Exchange"
			return ixp
		elif 3251182592 <= ipnum <= 3251182719:    # NaMeX does have ip prefix 193.201.28.0/25
			ixp['peeringdbid'] = 121
			ixp['city']        = "Rome"
			ixp['name']        = "NaMeX"
			ixp['name_long']   = "Nautilus Mediterranean Exchange Point"
			return ixp
		elif 3251182848 <= ipnum <= 3251182975:    # NaMeX does have ip prefix 193.201.29.0/25
			ixp['peeringdbid'] = 121
			ixp['city']        = "Rome"
			ixp['name']        = "NaMeX"
			ixp['name_long']   = "Nautilus Mediterranean Exchange Point"
			return ixp
		elif 3251306496 <= ipnum <= 3251306751:    # VIX does have ip prefix 193.203.0.0/24
			ixp['peeringdbid'] = 50
			ixp['city']        = "Vienna"
			ixp['name']        = "VIX"
			ixp['name_long']   = "Vienna Internet Exchange"
			return ixp
		elif 3252289536 <= ipnum <= 3252289791:    # NetIX does have ip prefix 193.218.0.0/24
			ixp['peeringdbid'] = 699
			ixp['city']        = "Sofia"
			ixp['name']        = "NetIX"
			ixp['name_long']   = "NetIX Communications Ltd."
			return ixp
		elif 3252358464 <= ipnum <= 3252358527:    # LIPTAM does have ip prefix 193.219.13.64/26
			ixp['peeringdbid'] = 400
			ixp['city']        = "Vilnius"
			ixp['name']        = "LIPTAM"
		elif 3253241600 <= ipnum <= 3253241855:    # SMR-IX does have ip prefix 193.232.135.0/24
			ixp['peeringdbid'] = 379
			ixp['city']        = "Samara"
			ixp['name']        = "SMR-IX"
			ixp['name_long']   = "Samara IX"
			return ixp
		elif 3253242880 <= ipnum <= 3253243135:    # RND-IX does have ip prefix 193.232.140.0/24
			ixp['peeringdbid'] = 380
			ixp['city']        = "Rostov-on-Don"
			ixp['name']        = "RND-IX"
			ixp['name_long']   = "Rostov-on-Don IX"
			return ixp
		elif 3253269504 <= ipnum <= 3253270015:    # MSK-IX does have ip prefix 193.232.244.0/23
			ixp['peeringdbid'] = 100
			ixp['city']        = "Moscow"
			ixp['name']        = "MSK-IX"
			ixp['name_long']   = "Moscow Internet Exchange"
			return ixp
		elif 3253270016 <= ipnum <= 3253270527:    # MSK-IX does have ip prefix 193.232.246.0/23
			ixp['peeringdbid'] = 100
			ixp['city']        = "Moscow"
			ixp['name']        = "MSK-IX"
			ixp['name_long']   = "Moscow Internet Exchange"
			return ixp
		elif 3253229312 <= ipnum <= 3253229567:    # NSK-IX does have ip prefix 193.232.87.0/24
			ixp['peeringdbid'] = 223
			ixp['city']        = "Novosibirsk/Russia"
			ixp['name']        = "NSK-IX"
			ixp['name_long']   = "Novosibirsk Internet Exchange"
			return ixp
		elif 3253695488 <= ipnum <= 3253695999:    # NL-IX does have ip prefix 193.239.116.0/23
			ixp['peeringdbid'] = 64
			ixp['city']        = "Amsterdam"
			ixp['name']        = "NL-IX"
			ixp['name_long']   = "Neutral Internet Exchange"
			return ixp
		elif 3253890816 <= ipnum <= 3253890943:    # INEX LAN1 does have ip prefix 193.242.111.0/25
			ixp['peeringdbid'] = 48
			ixp['city']        = "Dublin"
			ixp['name']        = "INEX LAN1"
			ixp['name_long']   = "Internet Neutral Exchange Association Ltd."
			return ixp
		elif 3253887488 <= ipnum <= 3253887743:    # CATNIX does have ip prefix 193.242.98.0/24
			ixp['peeringdbid'] = 62
			ixp['city']        = "Barcelona"
			ixp['name']        = "CATNIX"
			ixp['name_long']   = "Catalunya Neutral Internet Exchange"
			return ixp
		elif 3253974848 <= ipnum <= 3253974911:    # MalmIX Malmo / IXOR does have ip prefix 193.243.183.64/26
			ixp['peeringdbid'] = 231
		elif 3239684608 <= ipnum <= 3239685119:    # RBIEX does have ip prefix 193.25.170.0/23
			ixp['peeringdbid'] = 56
			ixp['city']        = "London"
			ixp['name']        = "RBIEX"
			ixp['name_long']   = "RBIEX Limited"
			return ixp
		elif 3254507520 <= ipnum <= 3254507775:    # PARIX does have ip prefix 193.251.216.0/24
			ixp['peeringdbid'] = 40
			ixp['city']        = "Paris"
			ixp['name']        = "PARIX"
		elif 3239839232 <= ipnum <= 3239839487:    # PIRIX does have ip prefix 193.28.6.0/24
			ixp['peeringdbid'] = 512
			ixp['city']        = "St.Petersburg"
			ixp['name']        = "PIRIX"
			ixp['name_long']   = "Pirix Internet Exchange"
			return ixp
		elif 3240464384 <= ipnum <= 3240464639:    # AAIX does have ip prefix 193.37.144.0/24
			ixp['peeringdbid'] = 377
			ixp['city']        = "Klagenfurt"
			ixp['name']        = "AAIX"
			ixp['name_long']   = "Alpes Adria Internet eXchange"
			return ixp
		elif 3240794880 <= ipnum <= 3240795135:    # ECIX-HAM does have ip prefix 193.42.155.0/24
			ixp['peeringdbid'] = 291
			ixp['city']        = "Hamburg"
			ixp['name']        = "ECIX-HAM"
			ixp['name_long']   = "European Commercial Internet Exchange Hamburg"
			return ixp
		elif 3238542784 <= ipnum <= 3238542847:    # CePIX.pl does have ip prefix 193.8.61.192/26
			ixp['peeringdbid'] = 524
			ixp['city']        = "Mogilno"
			ixp['name']        = "CePIX.pl"
			ixp['name_long']   = "Central Polish Internet eXchange"
			return ixp
		elif 3262406656 <= ipnum <= 3262406911:    # TOP-IX does have ip prefix 194.116.96.0/24
			ixp['peeringdbid'] = 115
			ixp['city']        = "Turin"
			ixp['name']        = "TOP-IX"
			ixp['name_long']   = "Consorzio Top-IX"
			return ixp
		elif 3262461056 <= ipnum <= 3262461183:    # COPHIX does have ip prefix 194.117.52.128/25
			ixp['peeringdbid'] = 457
			ixp['city']        = "Copenhagen"
			ixp['name']        = "COPHIX"
			ixp['name_long']   = "Copenhagen Internet eXchange"
			return ixp
		elif 3264378368 <= ipnum <= 3264378623:    # ECIX-DUS does have ip prefix 194.146.118.0/24
			ixp['peeringdbid'] = 91
			ixp['city']        = "Duesseldorf"
			ixp['name']        = "ECIX-DUS"
			ixp['name_long']   = "European Commercial Internet Exchange Duesseldorf"
			return ixp
		elif 3265601536 <= ipnum <= 3265601791:    # GIX Gothenburg does have ip prefix 194.165.32.0/24
			ixp['peeringdbid'] = 146
			ixp['city']        = "Gothenburg"
			ixp['name']        = "GIX Gothenburg"
			ixp['name_long']   = "Gothenburg Internet Exchange"
			return ixp
		elif 3267262208 <= ipnum <= 3267262463:    # KZN-IX does have ip prefix 194.190.119.0/24
			ixp['peeringdbid'] = 398
			ixp['city']        = "Kazan/Tatarstan"
			ixp['name']        = "KZN-IX"
			ixp['name_long']   = "Kazan Internet Exchange"
			return ixp
		elif 3256793856 <= ipnum <= 3256794111:    # NIX.SK does have ip prefix 194.30.187.0/24
			ixp['peeringdbid'] = 299
			ixp['city']        = "Bratislava"
			ixp['name']        = "NIX.SK"
			ixp['name_long']   = "Neutral Internet eXchange Slovakia"
			return ixp
		elif 3257544704 <= ipnum <= 3257544959:    # Equinix Zurich does have ip prefix 194.42.48.0/24
			ixp['peeringdbid'] = 29
			ixp['city']        = "Zurich"
			ixp['name']        = "Equinix Zurich"
			ixp['name_long']   = "Equinix Zurich, formerly TIX"
			return ixp
		elif 3258297344 <= ipnum <= 3258297471:    # BNIX does have ip prefix 194.53.172.0/25
			ixp['peeringdbid'] = 59
			ixp['city']        = "Brussels"
			ixp['name']        = "BNIX"
			ixp['name_long']   = "Belgian National Internet eXchange"
			return ixp
		elif 3258342400 <= ipnum <= 3258342527:    # OCIX Duesseldorf does have ip prefix 194.54.92.0/25
			ixp['peeringdbid'] = 170
			ixp['city']        = "Duesseldorf"
			ixp['name']        = "OCIX Duesseldorf"
			ixp['name_long']   = "OpenCarrier eG Member IX Duesseldorf "
			return ixp
		elif 3258342656 <= ipnum <= 3258342783:    # OCIX Frankfurt does have ip prefix 194.54.93.0/25
			ixp['peeringdbid'] = 867
			ixp['city']        = "Frankfurt"
			ixp['name']        = "OCIX Frankfurt"
			ixp['name_long']   = "OpenCarrier eG Member-IX Frankfurt"
			return ixp
		elif 3258580352 <= ipnum <= 3258580383:    # REUNIX does have ip prefix 194.57.253.128/27
			ixp['peeringdbid'] = 381
			ixp['city']        = "Saint-Denis, La Reunion"
			ixp['name']        = "REUNIX"
			ixp['name_long']   = "REUNIX"
			return ixp
		elif 3258695168 <= ipnum <= 3258695423:    # INXS does have ip prefix 194.59.190.0/24
			ixp['peeringdbid'] = 73
			ixp['city']        = "Munich"
			ixp['name']        = "INXS"
			ixp['name_long']   = "Internet Exchange Service"
			return ixp
		elif 3259267840 <= ipnum <= 3259268095:    # Netnod Stockholm does have ip prefix 194.68.123.0/24
			ixp['peeringdbid'] = 70
			ixp['city']        = "Stockholm"
			ixp['name']        = "Netnod Stockholm"
			ixp['name_long']   = "Netnod Internet Exchange i Sverige AB"
			return ixp
		elif 3259269120 <= ipnum <= 3259269375:    # Netnod Stockholm does have ip prefix 194.68.128.0/24
			ixp['peeringdbid'] = 70
			ixp['city']        = "Stockholm"
			ixp['name']        = "Netnod Stockholm"
			ixp['name_long']   = "Netnod Internet Exchange i Sverige AB"
			return ixp
		elif 3259269376 <= ipnum <= 3259269631:    # SFINX does have ip prefix 194.68.129.0/24
			ixp['peeringdbid'] = 34
			ixp['city']        = "Paris"
			ixp['name']        = "SFINX"
			ixp['name_long']   = "Service for French INternet eXchange"
			return ixp
		elif 3260377856 <= ipnum <= 3260378111:    # EKT-IX does have ip prefix 194.85.107.0/24
			ixp['peeringdbid'] = 350
			ixp['city']        = "Ekaterinburg"
			ixp['name']        = "EKT-IX"
			ixp['name_long']   = "Ekaterinburg IX"
			return ixp
		elif 3260608512 <= ipnum <= 3260608639:    # INEX LAN2 does have ip prefix 194.88.240.0/25
			ixp['peeringdbid'] = 387
			ixp['city']        = "Dublin"
			ixp['name']        = "INEX LAN2"
			ixp['name_long']   = "Internet Neutral Exchange Association Ltd."
			return ixp
		elif 3255399680 <= ipnum <= 3255399935:    # ECIX-BER does have ip prefix 194.9.117.0/24
			ixp['peeringdbid'] = 209
			ixp['city']        = "Berlin"
			ixp['name']        = "ECIX-BER"
			ixp['name_long']   = "European Commercial Internet Exchange Berlin"
			return ixp
		elif 3281381376 <= ipnum <= 3281381887:    # TPIX does have ip prefix 195.149.232.0/23
			ixp['peeringdbid'] = 482
			ixp['city']        = "Warsaw"
			ixp['name']        = "TPIX"
			ixp['name_long']   = "TPIX"
			return ixp
		elif 3283540480 <= ipnum <= 3283540991:    # PLIX does have ip prefix 195.182.218.0/23
			ixp['peeringdbid'] = 264
			ixp['city']        = "Warsaw"
			ixp['name']        = "PLIX"
			ixp['name_long']   = "Polish Internet Exchange"
			return ixp
		elif 3287663616 <= ipnum <= 3287663871:    # MAD-IX does have ip prefix 195.245.196.0/24
			ixp['peeringdbid'] = 90
			ixp['city']        = "Madrid"
			ixp['name']        = "MAD-IX"
			ixp['name_long']   = "Madrid Internet Exchange"
			return ixp
		elif 3287674880 <= ipnum <= 3287675135:    # Netnod Stockholm does have ip prefix 195.245.240.0/24
			ixp['peeringdbid'] = 70
			ixp['city']        = "Stockholm"
			ixp['name']        = "Netnod Stockholm"
			ixp['name_long']   = "Netnod Internet Exchange i Sverige AB"
			return ixp
		elif 3273867520 <= ipnum <= 3273867775:    # UA-IX does have ip prefix 195.35.65.0/24
			ixp['peeringdbid'] = 184
			ixp['city']        = "Kiev"
			ixp['name']        = "UA-IX"
			ixp['name_long']   = "Ukranian Internet Exchange"
			return ixp
		elif 3274346496 <= ipnum <= 3274347007:    # Equinix Paris does have ip prefix 195.42.144.0/23
			ixp['peeringdbid'] = 255
			ixp['city']        = "Paris"
			ixp['name']        = "Equinix Paris"
			ixp['name_long']   = "Equinix Internet Exchange Paris"
			return ixp
		elif 3275510912 <= ipnum <= 3275511039:    # MerieX does have ip prefix 195.60.84.128/25
			ixp['peeringdbid'] = 161
			ixp['city']        = "London"
			ixp['name']        = "MerieX"
			ixp['name_long']   = "Meridian Gate Internet Exchange"
			return ixp
		elif 3275512064 <= ipnum <= 3275512319:    # CBIX does have ip prefix 195.60.89.0/24
			ixp['peeringdbid'] = 477
			ixp['city']        = "Brno"
			ixp['name']        = "CBIX"
			ixp['name_long']   = "Commercial Brno Internet Exchange"
			return ixp
		elif 3275939840 <= ipnum <= 3275940863:    # LINX Juniper LAN does have ip prefix 195.66.224.0/22
			ixp['peeringdbid'] = 18
			ixp['city']        = "London"
			ixp['name']        = "LINX Juniper LAN"
			ixp['name_long']   = "London Internet Exchange Ltd."
			return ixp
		elif 3275942912 <= ipnum <= 3275943935:    # LINX Extreme LAN does have ip prefix 195.66.236.0/22
			ixp['peeringdbid'] = 321
			ixp['city']        = "London"
			ixp['name']        = "LINX Extreme LAN"
			ixp['name_long']   = "London Internet Exchange Ltd."
			return ixp
		elif 3275944960 <= ipnum <= 3275945215:    # IXManchester does have ip prefix 195.66.244.0/24
			ixp['peeringdbid'] = 583
			ixp['city']        = "Manchester"
			ixp['name']        = "IXManchester"
			ixp['name_long']   = "IXManchester powered by LINX"
			return ixp
		elif 3275945472 <= ipnum <= 3275945727:    # IXScotland does have ip prefix 195.66.246.0/24
			ixp['peeringdbid'] = 745
			ixp['city']        = "Scotland"
			ixp['name']        = "IXScotland"
			ixp['name_long']   = "IXScotland powered by LINX"
			return ixp
		elif 3276109568 <= ipnum <= 3276109823:    # Netnod Stockholm does have ip prefix 195.69.119.0/24
			ixp['peeringdbid'] = 70
			ixp['city']        = "Stockholm"
			ixp['name']        = "Netnod Stockholm"
			ixp['name_long']   = "Netnod Internet Exchange i Sverige AB"
			return ixp
		elif 3277177600 <= ipnum <= 3277177855:    # WIX does have ip prefix 195.85.195.0/24
			ixp['peeringdbid'] = 96
			ixp['city']        = "Warsaw"
			ixp['name']        = "WIX"
			ixp['name_long']   = "Warsaw Internet eXchange"
			return ixp
		elif 3277179648 <= ipnum <= 3277179903:    # FreeBIX does have ip prefix 195.85.203.0/24
			ixp['peeringdbid'] = 58
			ixp['city']        = "Belgium"
			ixp['name']        = "FreeBIX"
			ixp['name_long']   = "Free Belgian Internet Exchange"
			return ixp
		elif 3289025536 <= ipnum <= 3289025791:    # NAPAfrica IX Cape Town does have ip prefix 196.10.140.0/24
			ixp['peeringdbid'] = 597
			ixp['city']        = "Cape Town"
			ixp['name']        = "NAPAfrica IX Cape Town"
			ixp['name_long']   = "NAPAfrica IX Cape Town"
			return ixp
		elif 3289025792 <= ipnum <= 3289026047:    # NAPAfrica IX Durban does have ip prefix 196.10.141.0/24
			ixp['peeringdbid'] = 969
			ixp['city']        = "Durban"
			ixp['name']        = "NAPAfrica IX Durban"
			ixp['name_long']   = "NAPAfrica IX Durban"
			return ixp
		elif 3289115136 <= ipnum <= 3289115391:    # angonix does have ip prefix 196.11.234.0/24
			ixp['peeringdbid'] = 1007
			ixp['city']        = "Luanda"
			ixp['name']        = "angonix"
			ixp['name_long']   = "Angola Internet Exchange Point"
			return ixp
		elif 3302528000 <= ipnum <= 3302528255:    # IXPN Lagos does have ip prefix 196.216.148.0/24
			ixp['peeringdbid'] = 488
			ixp['city']        = "Lagos"
			ixp['name']        = "IXPN Lagos"
			ixp['name_long']   = "Internet Exchange Point of Nigeria"
			return ixp
		elif 3302951680 <= ipnum <= 3302951935:    # AMS-IX East Africa does have ip prefix 196.223.11.0/24
			ixp['peeringdbid'] = 873
			ixp['city']        = "Mombasa"
			ixp['name']        = "AMS-IX East Africa"
			ixp['name_long']   = "AMS-IX East Africa Exchange Point"
			return ixp
		elif 3302951936 <= ipnum <= 3302952191:    # RINEX does have ip prefix 196.223.12.0/24
			ixp['peeringdbid'] = 1032
			ixp['city']        = "Kigali"
			ixp['name']        = "RINEX"
			ixp['name_long']   = "Rwanda Internet Exchange"
			return ixp
		elif 3302951936 <= ipnum <= 3302952191:    # JINX does have ip prefix 196.223.14.0/24 (Data)
			ixp['peeringdbid'] = 129
			ixp['city']        = "Johannesburg"
			ixp['name']        = "JINX"
			ixp['name_long']   = "Johannesburg Internet Exchange"
			return ixp
		elif 3302951936 <= ipnum <= 3302952191:    # JINX does have ip prefix 196.223.15.0/24 (VoIP)
			ixp['peeringdbid'] = 129
			ixp['city']        = "Johannesburg"
			ixp['name']        = "JINX"
			ixp['name_long']   = "Johannesburg Internet Exchange"
			return ixp
		elif 3302954240 <= ipnum <= 3302954495:    # KIXP does have ip prefix 196.223.21.0/24
			ixp['peeringdbid'] = 236
			ixp['city']        = "Nairobi"
			ixp['name']        = "KIXP"
			ixp['name_long']   = "Kenya Internet Exchange Point"
			return ixp
		elif 3302954240 <= ipnum <= 3302954495:    # CINX does have ip prefix 196.223.22.0/24 (Data)
			ixp['peeringdbid'] = 344
			ixp['city']        = "Cape Town"
			ixp['name']        = "CINX"
			ixp['name_long']   = "Cape Town Internet Exchange"
			return ixp
		elif 3302954240 <= ipnum <= 3302954495:    # CINX does have ip prefix 196.223.23.0/24 (VoiP)
			ixp['peeringdbid'] = 344
			ixp['city']        = "Cape Town"
			ixp['name']        = "CINX"
			ixp['name_long']   = "Cape Town Internet Exchange"
			return ixp
		elif 3302955264 <= ipnum <= 3302955391:    # UIXP does have ip prefix 196.223.25.0/25
			ixp['peeringdbid'] = 422
			ixp['city']        = "Kampala"
			ixp['name']        = "UIXP"
			ixp['name_long']   = "Uganda Internet Exchange Point"
			return ixp
		elif 3302956032 <= ipnum <= 3302956287:    # RDC-IX Kinshasa does have ip prefix 196.223.28.0/24
			ixp['peeringdbid'] = 628
			ixp['city']        = "Kinshasa"
			ixp['name']        = "RDC-IX Kinshasa"
			ixp['name_long']   = "Kinix"
			return ixp
		elif 3302958592 <= ipnum <= 3302958847:    # DjIX does have ip prefix 196.223.38.0/24
			ixp['peeringdbid'] = 967
			ixp['city']        = "Djibouti"
			ixp['name']        = "DjIX"
			ixp['name_long']   = "The Djibouti Internet Exchange"
			return ixp
		elif 3302950144 <= ipnum <= 3302950399:    # TIX - Tanzania does have ip prefix 196.223.5.0/24
			ixp['peeringdbid'] = 361
			ixp['city']        = "Dar es Salaam"
			ixp['name']        = "TIX - Tanzania"
			ixp['name_long']   = "Tanzania Internet eXchange"
			return ixp
		elif 3302950656 <= ipnum <= 3302950911:    # MEIX does have ip prefix 196.223.7.0/24
			ixp['peeringdbid'] = 281
			ixp['city']        = "Cairo"
			ixp['name']        = "MEIX"
			ixp['name_long']   = "GPX Cairo"
			return ixp
		elif 3291355520 <= ipnum <= 3291355647:    # NAPAfrica IX Johannesburg does have ip prefix 196.46.25.128/25
			ixp['peeringdbid'] = 592
			ixp['city']        = "Johannesburg"
			ixp['name']        = "NAPAfrica IX Johannesburg"
			ixp['name_long']   = "NAPAfrica IX Johannesburg"
			return ixp
		elif 3323014656 <= ipnum <= 3323014911:    # SD-NAP does have ip prefix 198.17.46.0/24
			ixp['peeringdbid'] = 81
			ixp['city']        = "San Diego"
			ixp['name']        = "SD-NAP"
			ixp['name_long']   = "San Diego NAP"
			return ixp
		elif 3333624320 <= ipnum <= 3333624575:    # QIX does have ip prefix 198.179.18.0/24
			ixp['peeringdbid'] = 355
			ixp['city']        = "Montreal"
			ixp['name']        = "QIX"
			ixp['name_long']   = "Quebec Internet Exchange"
			return ixp
		elif 3324015104 <= ipnum <= 3324015359:    # Equinix Miami does have ip prefix 198.32.114.0/24
			ixp['peeringdbid'] = 593
			ixp['city']        = "Miami"
			ixp['name']        = "Equinix Miami"
			ixp['name_long']   = "Equinix Internet Exchange Miami"
			return ixp
		elif 3324016128 <= ipnum <= 3324016383:    # Equinix New York does have ip prefix 198.32.118.0/24
			ixp['peeringdbid'] = 12
			ixp['city']        = "New York"
			ixp['name']        = "Equinix New York"
			ixp['name_long']   = "Equinix Internet Exchange New York"
			return ixp
		elif 3324016640 <= ipnum <= 3324016895:    # ISTIX / IST-IX does have ip prefix 198.32.120.0/24
			ixp['peeringdbid'] = 343
			ixp['city']        = "Istanbul"
			ixp['name']        = "ISTIX / IST-IX"
			ixp['name_long']   = "Istanbul Internet Exchange"
			return ixp
		elif 3324017152 <= ipnum <= 3324017407:    # NDB does have ip prefix 198.32.122.0/24
			ixp['peeringdbid'] = 119
		elif 3324017664 <= ipnum <= 3324018175:    # NOTA does have ip prefix 198.32.124.0/23
			ixp['peeringdbid'] = 17
			ixp['city']        = "Miami"
			ixp['name']        = "NOTA"
			ixp['name_long']   = "NAP Of The Americas"
			return ixp
		elif 3324018944 <= ipnum <= 3324019199:    # SFIX does have ip prefix 198.32.129.0/24
			ixp['peeringdbid'] = 32
			ixp['city']        = "San Francisco"
			ixp['name']        = "SFIX"
			ixp['name_long']   = "San Francisco Internet Exchange"
			return ixp
		elif 3324019200 <= ipnum <= 3324019455:    # CyrusOne IX Dallas does have ip prefix 198.32.130.0/24
			ixp['peeringdbid'] = 672
			ixp['city']        = "Dallas"
			ixp['name']        = "CyrusOne IX Dallas"
			ixp['name_long']   = "CyrusOne Internet Exchange"
			return ixp
		elif 3324019456 <= ipnum <= 3324019711:    # KD-X does have ip prefix 198.32.131.0/24
			ixp['peeringdbid'] = 65
			ixp['city']        = "San Jose"
			ixp['name']        = "KD-X"
			ixp['name_long']   = "KDWEB Exchange"
			return ixp
		elif 3324019712 <= ipnum <= 3324019967:    # Telx Atlanta does have ip prefix 198.32.132.0/24
			ixp['peeringdbid'] = 22
			ixp['city']        = "Atlanta"
			ixp['name']        = "Telx Atlanta"
			ixp['name_long']   = "TIE:Atlanta, Atlanta Internet Exchange, AtlantaIX"
			return ixp
		elif 3324020224 <= ipnum <= 3324020479:    # Equinix Seattle does have ip prefix 198.32.134.0/24
			ixp['peeringdbid'] = 11
			ixp['city']        = "Seattle"
			ixp['name']        = "Equinix Seattle"
			ixp['name_long']   = "Equinix Internet Exchange Seattle"
			return ixp
		elif 3324020736 <= ipnum <= 3324020991:    # NASA-AIX does have ip prefix 198.32.136.0/24
			ixp['peeringdbid'] = 428
			ixp['city']        = "Mountain View, CA"
			ixp['name']        = "NASA-AIX"
			ixp['name_long']   = "NASA Ames Internet eXchange"
			return ixp
		elif 3324021504 <= ipnum <= 3324021759:    # MAE Central does have ip prefix 198.32.139.0/24
			ixp['peeringdbid'] = 20
			ixp['city']        = "Dallas & Chicago"
			ixp['name']        = "MAE Central"
		elif 3324022016 <= ipnum <= 3324022271:    # SOX does have ip prefix 198.32.141.0/24
			ixp['peeringdbid'] = 93
			ixp['city']        = "Singapore"
			ixp['name']        = "SOX"
			ixp['name_long']   = "Singapore Open Exchange"
			return ixp
		elif 3324023296 <= ipnum <= 3324023551:    # LAIIX does have ip prefix 198.32.146.0/24
			ixp['peeringdbid'] = 23
			ixp['city']        = "Los Angeles"
			ixp['name']        = "LAIIX"
			ixp['name_long']   = "Los Angeles International Internet eXchange"
			return ixp
		elif 3324025088 <= ipnum <= 3324025343:    # NASA-AIX does have ip prefix 198.32.153.0/24
			ixp['peeringdbid'] = 428
			ixp['city']        = "Mountain View, CA"
			ixp['name']        = "NASA-AIX"
			ixp['name_long']   = "NASA Ames Internet eXchange"
			return ixp
		elif 3324026880 <= ipnum <= 3324027135:    # NYIIX does have ip prefix 198.32.160.0/24
			ixp['peeringdbid'] = 14
			ixp['city']        = "New York"
			ixp['name']        = "NYIIX"
			ixp['name_long']   = "New York International Internet eXchange"
			return ixp
		elif 3324030720 <= ipnum <= 3324030975:    # Equinix Palo Alto does have ip prefix 198.32.175.0/24
			ixp['peeringdbid'] = 7
			ixp['city']        = "Palo Alto"
			ixp['name']        = "Equinix Palo Alto"
			ixp['name_long']   = "Equinix Internet Exchange Palo Alto"
			return ixp
		elif 3324030976 <= ipnum <= 3324031231:    # Equinix Palo Alto does have ip prefix 198.32.176.0/24
			ixp['peeringdbid'] = 7
			ixp['city']        = "Palo Alto"
			ixp['name']        = "Equinix Palo Alto"
			ixp['name_long']   = "Equinix Internet Exchange Palo Alto"
			return ixp
		elif 3324031488 <= ipnum <= 3324031743:    # MXP does have ip prefix 198.32.178.0/24
			ixp['peeringdbid'] = 25
			ixp['city']        = "Boston"
			ixp['name']        = "MXP"
			ixp['name_long']   = "Massachusetts eXchange Point"
			return ixp
		elif 3324032256 <= ipnum <= 3324032511:    # Equinix Atlanta does have ip prefix 198.32.181.0/24
			ixp['peeringdbid'] = 9
			ixp['city']        = "Atlanta"
			ixp['name']        = "Equinix Atlanta"
			ixp['name_long']   = "Equinix Internet Exchange Atlanta"
			return ixp
		elif 3324032256 <= ipnum <= 3324032511:    # Equinix Toronto does have ip prefix 198.32.181.0/24
			ixp['peeringdbid'] = 373
			ixp['city']        = "Toronto"
			ixp['name']        = "Equinix Toronto"
			ixp['name_long']   = "Equinix Internet Exchange Toronto"
			return ixp
		elif 3324032512 <= ipnum <= 3324032767:    # Equinix Atlanta does have ip prefix 198.32.182.0/24
			ixp['peeringdbid'] = 9
			ixp['city']        = "Atlanta"
			ixp['name']        = "Equinix Atlanta"
			ixp['name_long']   = "Equinix Internet Exchange Atlanta"
			return ixp
		elif 3324033536 <= ipnum <= 3324033791:    # Telx Phoenix does have ip prefix 198.32.186.0/24
			ixp['peeringdbid'] = 256
			ixp['city']        = "Phoenix"
			ixp['name']        = "Telx Phoenix"
			ixp['name_long']   = "TIE:Phoenix, Telx Internet Exchange Phoenix"
			return ixp
		elif 3324033792 <= ipnum <= 3324034047:    # MAE East does have ip prefix 198.32.187.0/24
			ixp['peeringdbid'] = 15
			ixp['city']        = "No. VA & NYC"
			ixp['name']        = "MAE East"
		elif 3324034560 <= ipnum <= 3324034815:    # Equinix Vienna (VA) does have ip prefix 198.32.190.0/24
			ixp['peeringdbid'] = 10
			ixp['city']        = "Vienna"
			ixp['name']        = "Equinix Vienna (VA)"
			ixp['name_long']   = "Equinix Internet Exchange Vienna, VA"
			return ixp
		elif 3324034816 <= ipnum <= 3324035071:    # Equinix Vienna (VA) does have ip prefix 198.32.191.0/24
			ixp['peeringdbid'] = 10
			ixp['city']        = "Vienna"
			ixp['name']        = "Equinix Vienna (VA)"
			ixp['name_long']   = "Equinix Internet Exchange Vienna, VA"
			return ixp
		elif 3324035840 <= ipnum <= 3324036095:    # NWAX does have ip prefix 198.32.195.0/24
			ixp['peeringdbid'] = 165
			ixp['city']        = "Portland, Oregon"
			ixp['name']        = "NWAX"
			ixp['name_long']   = "Northwest Access Exchange, Inc."
			return ixp
		elif 3324037120 <= ipnum <= 3324037375:    # MAE West does have ip prefix 198.32.200.0/24
			ixp['peeringdbid'] = 16
			ixp['city']        = "San Jose & Los Angeles"
			ixp['name']        = "MAE West"
		elif 3324040192 <= ipnum <= 3324040447:    # IX Australia WA does have ip prefix 198.32.212.0/24
			ixp['peeringdbid'] = 21
			ixp['city']        = "Perth/WA"
			ixp['name']        = "IX Australia WA"
			ixp['name_long']   = "West Australian Internet Exchange (WAIX)"
			return ixp
		elif 3324044544 <= ipnum <= 3324044799:    # NYCX does have ip prefix 198.32.229.0/24
			ixp['peeringdbid'] = 41
			ixp['city']        = "New York"
			ixp['name']        = "NYCX"
			ixp['name_long']   = "Free NYIIX Alternative"
			return ixp
		elif 3324046848 <= ipnum <= 3324047103:    # BigApe does have ip prefix 198.32.238.0/24
			ixp['peeringdbid'] = 151
			ixp['city']        = "New York"
			ixp['name']        = "BigApe"
			ixp['name_long']   = "The Big Apple Peering Exchange"
			return ixp
		elif 3324049152 <= ipnum <= 3324049407:    # PARIX does have ip prefix 198.32.247.0/24
			ixp['peeringdbid'] = 40
			ixp['city']        = "Paris"
			ixp['name']        = "PARIX"
		elif 3324010496 <= ipnum <= 3324011007:    # CyrusOne IX Houston does have ip prefix 198.32.96.0/23
			ixp['peeringdbid'] = 673
			ixp['city']        = "Houston"
			ixp['name']        = "CyrusOne IX Houston"
			ixp['name_long']   = "CyrusOne Internet Exchange"
			return ixp
		elif 3324011008 <= ipnum <= 3324011263:    # CyrusOne IX Phoenix does have ip prefix 198.32.98.0/24
			ixp['peeringdbid'] = 760
			ixp['city']        = "Phoenix"
			ixp['name']        = "CyrusOne IX Phoenix"
			ixp['name_long']   = "CyrusOne Internet Exchange"
			return ixp
		elif 3327001856 <= ipnum <= 3327002111:    # MiamiIX does have ip prefix 198.78.5.0/24
			ixp['peeringdbid'] = 957
			ixp['city']        = "Miami, Florida"
			ixp['name']        = "MiamiIX"
			ixp['name_long']   = "Miami Internet Exchange"
			return ixp
		elif 3349709568 <= ipnum <= 3349709823:    # midwest-ix does have ip prefix 199.168.131.0/24
			ixp['peeringdbid'] = 986
			ixp['city']        = "Indianapolis, Indiana"
			ixp['name']        = "midwest-ix"
			ixp['name_long']   = "Midwest Internet Exchange"
			return ixp
		elif 3355447552 <= ipnum <= 3355447807:    # CABASE-BUE does have ip prefix 200.0.17.0/24
			ixp['peeringdbid'] = 181
			ixp['city']        = "Buenos Aires"
			ixp['name']        = "CABASE-BUE"
			ixp['name_long']   = "CABASE NAP Buenos Aires"
			return ixp
		elif 3355447808 <= ipnum <= 3355448063:    # HIX Haiti does have ip prefix 200.0.18.0/24
			ixp['peeringdbid'] = 573
			ixp['city']        = "Port-au-Prince"
			ixp['name']        = "HIX Haiti"
			ixp['name_long']   = "Haiti Internet Exchange"
			return ixp
		elif 3355448064 <= ipnum <= 3355448319:    # CABASE-NQN does have ip prefix 200.0.19.0/24
			ixp['peeringdbid'] = 930
		elif 3355448320 <= ipnum <= 3355448575:    # AMS-IX Caribbean does have ip prefix 200.0.20.0/24
			ixp['peeringdbid'] = 366
			ixp['city']        = "Curacao"
			ixp['name']        = "AMS-IX Caribbean"
			ixp['name_long']   = "Amsterdam Internet Exchange Caribbean"
			return ixp
		elif 3355448832 <= ipnum <= 3355449343:    # OCIX does have ip prefix 200.0.22.0/23
			ixp['peeringdbid'] = 260
			ixp['city']        = "Philipsburg"
			ixp['name']        = "OCIX"
			ixp['name_long']   = "Open Caribbean Internet eXchange"
			return ixp
		elif 3355510272 <= ipnum <= 3355510527:    # NAP.EC-UIO does have ip prefix 200.1.6.0/24
			ixp['peeringdbid'] = 253
			ixp['city']        = "Quito/UIO"
			ixp['name']        = "NAP.EC-UIO"
			ixp['name_long']   = "NAP.EC Quito"
			return ixp
		elif 3363000576 <= ipnum <= 3363000831:    # CABASE-LPL does have ip prefix 200.115.81.0/24
			ixp['peeringdbid'] = 904
			ixp['city']        = "La Plata"
			ixp['name']        = "CABASE-LPL"
			ixp['name_long']   = "CABASE NAP La Plata"
			return ixp
		elif 3363000832 <= ipnum <= 3363001087:    # CABASE-MDQ does have ip prefix 200.115.82.0/24
			ixp['peeringdbid'] = 1069
			ixp['city']        = "Mar Del Plata"
			ixp['name']        = "CABASE-MDQ"
			ixp['name_long']   = "CABASE NAP Mar Del Plata"
			return ixp
		elif 3363001088 <= ipnum <= 3363001343:    # CABASE-POS does have ip prefix 200.115.83.0/24
			ixp['peeringdbid'] = 911
			ixp['city']        = "Posadas"
			ixp['name']        = "CABASE-POS"
			ixp['name_long']   = "CABASE NAP Posadas"
			return ixp
		elif 3363001344 <= ipnum <= 3363001599:    # CABASE-PMY does have ip prefix 200.115.84.0/24
			ixp['peeringdbid'] = 1071
			ixp['city']        = "Puerto Madryn"
			ixp['name']        = "CABASE-PMY"
			ixp['name_long']   = "CABASE NAP Puerto Madryn"
			return ixp
		elif 3356316416 <= ipnum <= 3356316671:    # CABASE-ROS does have ip prefix 200.13.83.0/24
			ixp['peeringdbid'] = 945
			ixp['city']        = "Rosario"
			ixp['name']        = "CABASE-ROS"
			ixp['name_long']   = "CABASE NAP Rosario"
			return ixp
		elif 3364364800 <= ipnum <= 3364365055:    # NDB does have ip prefix 200.136.34.0/24
			ixp['peeringdbid'] = 119
		elif 3356370176 <= ipnum <= 3356370431:    # CABASE-BHB does have ip prefix 200.14.37.0/24
			ixp['peeringdbid'] = 1066
		elif 3356370432 <= ipnum <= 3356370687:    # CABASE-MZA does have ip prefix 200.14.38.0/24
			ixp['peeringdbid'] = 1070
			ixp['city']        = "Mendoza"
			ixp['name']        = "CABASE-MZA"
			ixp['name_long']   = "CABASE NAP Mendoza"
			return ixp
		elif 3356370688 <= ipnum <= 3356370943:    # CABASE-DLC does have ip prefix 200.14.39.0/24
			ixp['peeringdbid'] = 1068
			ixp['city']        = "De La Costa"
			ixp['name']        = "CABASE-DLC"
			ixp['name_long']   = "CABASE NAP De La Costa"
			return ixp
		elif 3356379648 <= ipnum <= 3356379903:    # CABASE-SFE does have ip prefix 200.14.74.0/24
			ixp['peeringdbid'] = 1072
		elif 3356379904 <= ipnum <= 3356380159:    # CABASE-COR does have ip prefix 200.14.75.0/24
			ixp['peeringdbid'] = 1067
		elif 3368053760 <= ipnum <= 3368054015:    # PTT-CAS does have ip prefix 200.192.108.0/24
			ixp['peeringdbid'] = 415
			ixp['city']        = "Campinas/SP"
			ixp['name']        = "PTT-CAS"
			ixp['name_long']   = "PTT Campinas"
			return ixp
		elif 3368054016 <= ipnum <= 3368054271:    # PTT-CPV does have ip prefix 200.192.109.0/24
			ixp['peeringdbid'] = 603
			ixp['city']        = "Campina Grande/PB"
			ixp['name']        = "PTT-CPV"
			ixp['name_long']   = "PTT Campina Grande"
			return ixp
		elif 3368054272 <= ipnum <= 3368054527:    # PTT-DF does have ip prefix 200.192.110.0/24
			ixp['peeringdbid'] = 178
			ixp['city']        = "Brasilia/DF"
			ixp['name']        = "PTT-DF"
			ixp['name_long']   = "PTT Brasilia"
			return ixp
		elif 3368054528 <= ipnum <= 3368054783:    # PTT-GYN does have ip prefix 200.192.111.0/24
			ixp['peeringdbid'] = 575
			ixp['city']        = "Goiania/GO"
			ixp['name']        = "PTT-GYN"
			ixp['name_long']   = "PTT Goiania"
			return ixp
		elif 3369830912 <= ipnum <= 3369831167:    # PTT-RJ does have ip prefix 200.219.138.0/24
			ixp['peeringdbid'] = 177
			ixp['city']        = "Rio de Janeiro/RJ"
			ixp['name']        = "PTT-RJ"
			ixp['name_long']   = "PTT Rio de Janeiro"
			return ixp
		elif 3369831168 <= ipnum <= 3369831423:    # PTT-MG does have ip prefix 200.219.139.0/24
			ixp['peeringdbid'] = 176
			ixp['city']        = "Belo Horizonte/MG"
			ixp['name']        = "PTT-MG"
			ixp['name_long']   = "PTT Belo Horizonte"
			return ixp
		elif 3369831424 <= ipnum <= 3369831679:    # PTT-PR does have ip prefix 200.219.140.0/24
			ixp['peeringdbid'] = 174
			ixp['city']        = "Curitiba/PR"
			ixp['name']        = "PTT-PR"
			ixp['name_long']   = "PTT Curitiba"
			return ixp
		elif 3369831680 <= ipnum <= 3369831935:    # PTT-SC does have ip prefix 200.219.141.0/24
			ixp['peeringdbid'] = 175
			ixp['city']        = "Florianopolis/SC"
			ixp['name']        = "PTT-SC"
			ixp['name_long']   = "PTT Florianopolis"
			return ixp
		elif 3369832192 <= ipnum <= 3369832447:    # PTT-RS does have ip prefix 200.219.143.0/24
			ixp['peeringdbid'] = 173
			ixp['city']        = "Porto Alegre/RS"
			ixp['name']        = "PTT-RS"
			ixp['name_long']   = "PTT Porto Alegre"
			return ixp
		elif 3369832448 <= ipnum <= 3369832703:    # PTT-LDA does have ip prefix 200.219.144.0/24
			ixp['peeringdbid'] = 314
			ixp['city']        = "Londrina/PR"
			ixp['name']        = "PTT-LDA"
			ixp['name_long']   = "PTT Londrina"
			return ixp
		elif 3369832704 <= ipnum <= 3369832959:    # PTT-BA does have ip prefix 200.219.145.0/24
			ixp['peeringdbid'] = 556
			ixp['city']        = "Salvador/BA"
			ixp['name']        = "PTT-BA"
			ixp['name_long']   = "PTT Salvador"
			return ixp
		elif 3369832960 <= ipnum <= 3369833215:    # PTT-CE does have ip prefix 200.219.146.0/24
			ixp['peeringdbid'] = 710
			ixp['city']        = "Fortaleza/CE"
			ixp['name']        = "PTT-CE"
			ixp['name_long']   = "PTT Fortaleza"
			return ixp
		elif 3369833216 <= ipnum <= 3369833471:    # PTT-PE does have ip prefix 200.219.147.0/24
			ixp['peeringdbid'] = 705
			ixp['city']        = "Recife/PE"
			ixp['name']        = "PTT-PE"
			ixp['name_long']   = "PTT Recife"
			return ixp
		elif 3389020928 <= ipnum <= 3389021183:    # Manila IX does have ip prefix 202.0.91.0/24
			ixp['peeringdbid'] = 44
			ixp['city']        = "Manila "
			ixp['name']        = "Manila IX"
			ixp['name_long']   = "Manila Internet Exchange"
			return ixp
		elif 3397389312 <= ipnum <= 3397389375:    # GU-IX does have ip prefix 202.128.12.0/26
			ixp['peeringdbid'] = 463
			ixp['city']        = "Guam"
			ixp['name']        = "GU-IX"
			ixp['name_long']   = "Guam Internet Exchange"
			return ixp
		elif 3400000512 <= ipnum <= 3400000767:    # Equinix Sydney does have ip prefix 202.167.228.0/24
			ixp['peeringdbid'] = 94
			ixp['city']        = "Sydney"
			ixp['name']        = "Equinix Sydney"
			ixp['name_long']   = "Equinix Sydney Exchange"
			return ixp
		elif 3405316608 <= ipnum <= 3405316863:    # DIX-IE does have ip prefix 202.249.2.0/24
			ixp['peeringdbid'] = 92
			ixp['city']        = "Tokyo"
			ixp['name']        = "DIX-IE"
			ixp['name_long']   = "Distributed IX in EDO (former NSPIXP2)"
			return ixp
		elif 3391660032 <= ipnum <= 3391660543:    # HKIX does have ip prefix 202.40.160.0/23
			ixp['peeringdbid'] = 42
			ixp['city']        = "Hong Kong"
			ixp['name']        = "HKIX"
			ixp['name_long']   = "Hong Kong Internet Exchange"
			return ixp
		elif 3389456384 <= ipnum <= 3389456895:    # WIX-NZ does have ip prefix 202.7.0.0/23
			ixp['peeringdbid'] = 348
			ixp['city']        = "Wellington"
			ixp['name']        = "WIX-NZ"
			ixp['name_long']   = "Wellington Internet Exchange"
			return ixp
		elif 3394140416 <= ipnum <= 3394140671:    # BAYANTEL does have ip prefix 202.78.121.0/24
			ixp['peeringdbid'] = 154
			ixp['city']        = "Quezon City"
			ixp['name']        = "BAYANTEL"
			ixp['name_long']   = "Bayan Telecommunications Internet and Gaming Exchange"
			return ixp
		elif 3394225408 <= ipnum <= 3394225663:    # Equinix Singapore does have ip prefix 202.79.197.0/24
			ixp['peeringdbid'] = 158
			ixp['city']        = "Singapore"
			ixp['name']        = "Equinix Singapore"
			ixp['name_long']   = "Equinix Singapore Exchange"
			return ixp
		elif 3416514048 <= ipnum <= 3416514303:    # TPIX-TW does have ip prefix 203.163.222.0/24
			ixp['peeringdbid'] = 823
			ixp['city']        = "Taichung/Taiwan"
			ixp['name']        = "TPIX-TW"
			ixp['name_long']   = "Taipei Internet Exchange "
			return ixp
		elif 3418285568 <= ipnum <= 3418285823:    # Equinix Tokyo does have ip prefix 203.190.230.0/24
			ixp['peeringdbid'] = 167
			ixp['city']        = "Tokyo"
			ixp['name']        = "Equinix Tokyo"
			ixp['name_long']   = "Equinix Tokyo"
			return ixp
		elif 3429595648 <= ipnum <= 3429595775:    # MKE-IX does have ip prefix 204.107.122.0/25
			ixp['peeringdbid'] = 499
			ixp['city']        = "Milwaukee"
			ixp['name']        = "MKE-IX"
			ixp['name_long']   = "The Milwaukee IX"
			return ixp
		elif 3437534720 <= ipnum <= 3437534975:    # SLIX does have ip prefix 204.228.158.0/24
			ixp['peeringdbid'] = 829
			ixp['city']        = "Utah"
			ixp['name']        = "SLIX"
			ixp['name_long']   = "Salt Lake Internet Exchange"
			return ixp
		elif 3463213568 <= ipnum <= 3463213823:    # TPAIX does have ip prefix 206.108.114.0/24
			ixp['peeringdbid'] = 833
			ixp['city']        = "Tampa"
			ixp['name']        = "TPAIX"
			ixp['name_long']   = "Tampa Internet Exchange"
			return ixp
		elif 3463213824 <= ipnum <= 3463214079:    # AMS-IX Chicago does have ip prefix 206.108.115.0/24
			ixp['peeringdbid'] = 944
			ixp['city']        = "Chicago"
			ixp['name']        = "AMS-IX Chicago"
			ixp['name_long']   = "AMS-IX Chicago"
			return ixp
		elif 3463244800 <= ipnum <= 3463245055:    # Boston Internet Exchange does have ip prefix 206.108.236.0/24
			ixp['peeringdbid'] = 565
			ixp['city']        = "Boston/Massachusetts"
			ixp['name']        = "Boston Internet Exchange"
			ixp['name_long']   = "Markley Boston Internet Exchange"
			return ixp
		elif 3463249664 <= ipnum <= 3463249919:    # MICE does have ip prefix 206.108.255.0/24
			ixp['peeringdbid'] = 446
			ixp['city']        = "Minneapolis, MN"
			ixp['name']        = "MICE"
			ixp['name_long']   = "Midwest Internet Cooperative Exchange"
			return ixp
		elif 3463193088 <= ipnum <= 3463193599:    # TorIX does have ip prefix 206.108.34.0/23
			ixp['peeringdbid'] = 24
			ixp['city']        = "Toronto"
			ixp['name']        = "TorIX"
			ixp['name_long']   = "Toronto Internet Exchange Community"
			return ixp
		elif 3464167424 <= ipnum <= 3464167679:    # GTIIX does have ip prefix 206.123.0.0/24
			ixp['peeringdbid'] = 506
			ixp['city']        = "Toronto"
			ixp['name']        = "GTIIX"
			ixp['name_long']   = "Greater Toronto International Internet Exchange"
			return ixp
		elif 3464175104 <= ipnum <= 3464175359:    # GCIIX does have ip prefix 206.123.30.0/24
			ixp['peeringdbid'] = 640
			ixp['city']        = "Chicago"
			ixp['name']        = "GCIIX"
			ixp['name_long']   = "Greater Chicago International Internet Exchange"
			return ixp
		elif 3464169216 <= ipnum <= 3464169471:    # JXIX does have ip prefix 206.123.7.0/24
			ixp['peeringdbid'] = 563
			ixp['city']        = "Jacksonville"
			ixp['name']        = "JXIX"
			ixp['name_long']   = "Jacksonville Internet Exchange"
			return ixp
		elif 3464391936 <= ipnum <= 3464392191:    # WPGIX does have ip prefix 206.126.109.0/24
			ixp['peeringdbid'] = 776
			ixp['city']        = "Winnipeg"
			ixp['name']        = "WPGIX"
			ixp['name_long']   = "Winnipeg Internet Exchange"
			return ixp
		elif 3464393216 <= ipnum <= 3464393471:    # Telx Dallas does have ip prefix 206.126.114.0/24
			ixp['peeringdbid'] = 322
			ixp['city']        = "Dallas"
			ixp['name']        = "Telx Dallas"
			ixp['name_long']   = "TIE:Dallas, Telx Internet Exchange Dallas "
			return ixp
		elif 3464393472 <= ipnum <= 3464393727:    # Telx New York does have ip prefix 206.126.115.0/24
			ixp['peeringdbid'] = 325
			ixp['city']        = "New York"
			ixp['name']        = "Telx New York"
			ixp['name_long']   = "TIE:New York, Telx Internet Exchange New York"
			return ixp
		elif 3464421632 <= ipnum <= 3464421887:    # YYCIX does have ip prefix 206.126.225.0/24
			ixp['peeringdbid'] = 639
			ixp['city']        = "Calgary"
			ixp['name']        = "YYCIX"
			ixp['name_long']   = "YYCIX Calgary Internet Exchange"
			return ixp
		elif 3464422400 <= ipnum <= 3464422655:    # PHLIX does have ip prefix 206.126.228.0/24
			ixp['peeringdbid'] = 671
			ixp['city']        = "Philadelphia"
			ixp['name']        = "PHLIX"
			ixp['name_long']   = "Philadelphia Internet Exchange"
			return ixp
		elif 3464424192 <= ipnum <= 3464424255:    # OmahaIX does have ip prefix 206.126.235.0/26
			ixp['peeringdbid'] = 809
			ixp['city']        = "Omaha"
			ixp['name']        = "OmahaIX"
			ixp['name_long']   = "Omaha Internet Exchange"
			return ixp
		elif 3464424448 <= ipnum <= 3464425471:    # Equinix Ashburn does have ip prefix 206.126.236.0/22
			ixp['peeringdbid'] = 1
			ixp['city']        = "Ashburn"
			ixp['name']        = "Equinix Ashburn"
			ixp['name_long']   = "Equinix Ashburn Exchange"
			return ixp
		elif 3464425472 <= ipnum <= 3464425727:    # AMS-IX NY does have ip prefix 206.126.240.0/24
			ixp['peeringdbid'] = 806
			ixp['city']        = "New York"
			ixp['name']        = "AMS-IX NY"
			ixp['name_long']   = "AMS-IX New York"
			return ixp
		elif 3464626176 <= ipnum <= 3464626431:    # AlbertaIX does have ip prefix 206.130.0.0/24
			ixp['peeringdbid'] = 825
			ixp['city']        = "Calgary"
			ixp['name']        = "AlbertaIX"
			ixp['name_long']   = "AlbertaIX"
			return ixp
		elif 3464628736 <= ipnum <= 3464628991:    # DE-CIX New York does have ip prefix 206.130.10.0/24
			ixp['peeringdbid'] = 804
			ixp['city']        = "New York / New Jersey"
			ixp['name']        = "DE-CIX New York"
			ixp['name_long']   = "DE-CIX, the New York / New Jersey  Internet Exchange"
			return ixp
		elif 3464641792 <= ipnum <= 3464642047:    # BNIIX does have ip prefix 206.130.61.0/24
			ixp['peeringdbid'] = 496
			ixp['city']        = "Buffalo"
			ixp['name']        = "BNIIX"
			ixp['name_long']   = "Buffalo Niagara International Internet Exchange"
			return ixp
		elif 3469050624 <= ipnum <= 3469050879:    # COIX does have ip prefix 206.197.131.0/24
			ixp['peeringdbid'] = 514
			ixp['city']        = "Bend Oregon"
			ixp['name']        = "COIX"
			ixp['name_long']   = "Central Oregon Internet eXchange"
			return ixp
		elif 3469064960 <= ipnum <= 3469065215:    # SFMIX does have ip prefix 206.197.187.0/24
			ixp['peeringdbid'] = 155
			ixp['city']        = "San Francisco"
			ixp['name']        = "SFMIX"
			ixp['name_long']   = "San Francisco Metropolitan Internet Exchange"
			return ixp
		elif 3469070848 <= ipnum <= 3469071103:    # DRF IX does have ip prefix 206.197.210.0/24
			ixp['peeringdbid'] = 267
			ixp['city']        = "Honolulu"
			ixp['name']        = "DRF IX"
			ixp['name_long']   = "DRFortress Exchange"
			return ixp
		elif 3470750720 <= ipnum <= 3470750975:    # Equinix San Jose does have ip prefix 206.223.116.0/24
			ixp['peeringdbid'] = 5
			ixp['city']        = "San Jose"
			ixp['name']        = "Equinix San Jose"
			ixp['name_long']   = "Equinix San Jose / Bay Area Exchange"
			return ixp
		elif 3470751232 <= ipnum <= 3470751487:    # Equinix Dallas does have ip prefix 206.223.118.0/24
			ixp['peeringdbid'] = 3
			ixp['city']        = "Dallas"
			ixp['name']        = "Equinix Dallas"
			ixp['name_long']   = "Equinix Dallas Exchange"
			return ixp
		elif 3470751488 <= ipnum <= 3470751743:    # Equinix Chicago does have ip prefix 206.223.119.0/24
			ixp['peeringdbid'] = 2
			ixp['city']        = "Chicago"
			ixp['name']        = "Equinix Chicago"
			ixp['name_long']   = "Equinix Chicago Exchange"
			return ixp
		elif 3470751744 <= ipnum <= 3470751999:    # AZIX does have ip prefix 206.223.120.0/24
			ixp['peeringdbid'] = 476
			ixp['city']        = "Phoenix, Arizona"
			ixp['name']        = "AZIX"
			ixp['name_long']   = "Arizona Internet Exchange"
			return ixp
		elif 3470752512 <= ipnum <= 3470752767:    # Equinix Los Angeles does have ip prefix 206.223.123.0/24
			ixp['peeringdbid'] = 4
			ixp['city']        = "Los Angeles"
			ixp['name']        = "Equinix Los Angeles"
			ixp['name_long']   = "Equinix Los Angeles Exchange"
			return ixp
		elif 3470753024 <= ipnum <= 3470753151:    # TP-IX does have ip prefix 206.223.125.0/25
			ixp['peeringdbid'] = 624
			ixp['city']        = "Duluth"
			ixp['name']        = "TP-IX"
			ixp['name_long']   = "Twin Ports Internet Exchange"
			return ixp
		elif 3470753536 <= ipnum <= 3470753663:    # PIX Vancouver does have ip prefix 206.223.127.0/25
			ixp['peeringdbid'] = 195
			ixp['city']        = "Vancouver"
			ixp['name']        = "PIX Vancouver"
			ixp['name_long']   = "Peer1 Internet Exchange - Vancouver"
			return ixp
		elif 3458820352 <= ipnum <= 3458820607:    # Phoenix IX does have ip prefix 206.41.105.0/24
			ixp['peeringdbid'] = 662
			ixp['city']        = "Phoenix"
			ixp['name']        = "Phoenix IX"
			ixp['name_long']   = "Phoenix IX"
			return ixp
		elif 3458820608 <= ipnum <= 3458820863:    # AMS-IX BAY does have ip prefix 206.41.106.0/24
			ixp['peeringdbid'] = 935
			ixp['city']        = "San Francisco, San Jose"
			ixp['name']        = "AMS-IX BAY"
			ixp['name_long']   = "AMS-IX Bay Area"
			return ixp
		elif 3458821120 <= ipnum <= 3458821375:    # FL-IX does have ip prefix 206.41.108.0/24
			ixp['peeringdbid'] = 954
			ixp['city']        = "Miami"
			ixp['name']        = "FL-IX"
			ixp['name_long']   = "FL-IX - The South Florida Internet Exchange"
			return ixp
		elif 3458821632 <= ipnum <= 3458821887:    # ChIX does have ip prefix 206.41.110.0/24
			ixp['peeringdbid'] = 239
			ixp['city']        = "Chicago"
			ixp['name']        = "ChIX"
			ixp['name_long']   = "United IX - Chicago"
			return ixp
		elif 3459456512 <= ipnum <= 3459456767:    # NYIIX does have ip prefix 206.51.30.0/24
			ixp['peeringdbid'] = 14
			ixp['city']        = "New York"
			ixp['name']        = "NYIIX"
			ixp['name_long']   = "New York International Internet eXchange"
			return ixp
		elif 3459459072 <= ipnum <= 3459459327:    # CoreSite - Any2 NorthEast does have ip prefix 206.51.40.0/24
			ixp['peeringdbid'] = 204
			ixp['city']        = "DC, Reston, Boston, New York"
			ixp['name']        = "CoreSite - Any2 NorthEast"
			ixp['name_long']   = "CoreSite - Any2 NorthEast"
			return ixp
		elif 3459459328 <= ipnum <= 3459459583:    # CoreSite - Any2 Northern California does have ip prefix 206.51.41.0/24
			ixp['peeringdbid'] = 338
			ixp['city']        = "San Jose, CA"
			ixp['name']        = "CoreSite - Any2 Northern California"
			ixp['name_long']   = "CoreSite - Any2 Northern California"
			return ixp
		elif 3459459584 <= ipnum <= 3459459839:    # CoreSite - Any2 Boston does have ip prefix 206.51.42.0/24
			ixp['peeringdbid'] = 333
			ixp['city']        = "Boston"
			ixp['name']        = "CoreSite - Any2 Boston"
			ixp['name_long']   = "CoreSite - Any2 Boston"
			return ixp
		elif 3459459840 <= ipnum <= 3459460095:    # CoreSite - Any2 Chicago does have ip prefix 206.51.43.0/24
			ixp['peeringdbid'] = 226
			ixp['city']        = "Chicago"
			ixp['name']        = "CoreSite - Any2 Chicago"
			ixp['name_long']   = "CoreSite - Any2 Chicago"
			return ixp
		elif 3459460096 <= ipnum <= 3459460351:    # CoreSite - Any2 Miami does have ip prefix 206.51.44.0/24
			ixp['peeringdbid'] = 205
			ixp['city']        = "Miami"
			ixp['name']        = "CoreSite - Any2 Miami"
			ixp['name_long']   = "CoreSite - Any2 Miami"
			return ixp
		elif 3459460352 <= ipnum <= 3459460607:    # CoreSite - Any2 New York does have ip prefix 206.51.45.0/24
			ixp['peeringdbid'] = 332
			ixp['city']        = "New York"
			ixp['name']        = "CoreSite - Any2 New York"
			ixp['name_long']   = "CoreSite - Any2 New York"
			return ixp
		elif 3459460608 <= ipnum <= 3459460863:    # CoreSite - Any2 Denver  does have ip prefix 206.51.46.0/24
			ixp['peeringdbid'] = 254
			ixp['city']        = "Denver"
			ixp['name']        = "CoreSite - Any2 Denver "
			ixp['name_long']   = "CoreSite - Any2 Denver / Formerly RMIX"
			return ixp
		elif 3459450624 <= ipnum <= 3459450751:    # KCIX Kansas City does have ip prefix 206.51.7.0/25
			ixp['peeringdbid'] = 249
			ixp['city']        = "Kansas City"
			ixp['name']        = "KCIX Kansas City"
			ixp['name_long']   = "Kansas City Internet eXchange"
			return ixp
		elif 3459615488 <= ipnum <= 3459615743:    # midwest-ix does have ip prefix 206.53.139.0/24
			ixp['peeringdbid'] = 986
			ixp['city']        = "Indianapolis, Indiana"
			ixp['name']        = "midwest-ix"
			ixp['name_long']   = "Midwest Internet Exchange"
			return ixp
		elif 3459761152 <= ipnum <= 3459761663:    # LINX NoVA does have ip prefix 206.55.196.0/23
			ixp['peeringdbid'] = 777
			ixp['city']        = "Northern Virginia"
			ixp['name']        = "LINX NoVA"
			ixp['name_long']   = "LINX Northern Virginia"
			return ixp
		elif 3460878336 <= ipnum <= 3460878591:    # MBIX does have ip prefix 206.72.208.0/24
			ixp['peeringdbid'] = 703
			ixp['city']        = "Winnipeg, Manitoba"
			ixp['name']        = "MBIX"
			ixp['name_long']   = "Manitoba Internet Echange"
			return ixp
		elif 3460878848 <= ipnum <= 3460879359:    # CoreSite - Any2 California does have ip prefix 206.72.210.0/23
			ixp['peeringdbid'] = 142
			ixp['city']        = "Los Angeles and Silicon Valley"
			ixp['name']        = "CoreSite - Any2 California"
			ixp['name_long']   = "CoreSite - Any2 California"
			return ixp
		elif 3461435392 <= ipnum <= 3461435903:    # SIX does have ip prefix 206.81.80.0/23
			ixp['peeringdbid'] = 13
			ixp['city']        = "Seattle"
			ixp['name']        = "SIX"
			ixp['name_long']   = "Seattle Internet Exchange"
			return ixp
		elif 3488084224 <= ipnum <= 3488084479:    # PacificWave does have ip prefix 207.231.241.0/24
			ixp['peeringdbid'] = 82
			ixp['city']        = "West Coast"
			ixp['name']        = "PacificWave"
			ixp['name_long']   = "Pacific Wave Exchange in Los Angeles and Seattle"
			return ixp
		elif 3500005888 <= ipnum <= 3500006143:    # Phoenix IX does have ip prefix 208.157.218.0/24
			ixp['peeringdbid'] = 662
			ixp['city']        = "Phoenix"
			ixp['name']        = "Phoenix IX"
			ixp['name_long']   = "Phoenix IX"
			return ixp
		elif 3492986880 <= ipnum <= 3492987135:    # IXNM does have ip prefix 208.50.192.0/24
			ixp['peeringdbid'] = 153
			ixp['city']        = "New Mexico"
			ixp['name']        = "IXNM"
			ixp['name_long']   = "Internet Exchange New Mexico"
			return ixp
		elif 3514577920 <= ipnum <= 3514578431:    # DET-IX does have ip prefix 209.124.52.0/23
			ixp['peeringdbid'] = 1006
			ixp['city']        = "Detroit"
			ixp['name']        = "DET-IX"
			ixp['name_long']   = "Detroit Internet Exchange"
			return ixp
		elif 3508652464 <= ipnum <= 3508652479:    # SUPRnet does have ip prefix 209.33.201.176/28
			ixp['peeringdbid'] = 363
			ixp['city']        = "Saint George"
			ixp['name']        = "SUPRnet"
			ixp['name_long']   = "Southern Utah Peering Regional Network"
			return ixp
		elif 3529769728 <= ipnum <= 3529769983:    # PIPE Networks Adelaide does have ip prefix 210.100.3.0/24
			ixp['peeringdbid'] = 112
			ixp['city']        = "Adelaide"
			ixp['name']        = "PIPE Networks Adelaide"
			ixp['name_long']   = "PIPE Networks Adelaide"
			return ixp
		elif 3534479360 <= ipnum <= 3534479615:    # JPIX does have ip prefix 210.171.224.0/24
			ixp['peeringdbid'] = 30
			ixp['city']        = "Tokyo"
			ixp['name']        = "JPIX"
			ixp['name_long']   = "Japan Internet Exchange"
			return ixp
		elif 3535306496 <= ipnum <= 3535306751:    # iAIX does have ip prefix 210.184.127.0/24
			ixp['peeringdbid'] = 88
			ixp['city']        = "Hong Kong"
			ixp['name']        = "iAIX"
			ixp['name_long']   = "iAdvantage Internet Exchange"
			return ixp
		elif 3527343872 <= ipnum <= 3527344127:    # TWIX does have ip prefix 210.62.255.0/24
			ixp['peeringdbid'] = 43
			ixp['city']        = "Taipei"
			ixp['name']        = "TWIX"
			ixp['name_long']   = "Taiwan Internet Exchange"
			return ixp
		elif 3564707840 <= ipnum <= 3564716031:    # Edge-IX does have ip prefix 212.121.32.0/19
			ixp['peeringdbid'] = 57
			ixp['city']        = "UK"
			ixp['name']        = "Edge-IX"
		elif 3562733568 <= ipnum <= 3562734591:    # Thinx does have ip prefix 212.91.0.0/22
			ixp['peeringdbid'] = 481
			ixp['city']        = "Warsaw"
			ixp['name']        = "Thinx"
			ixp['name_long']   = "Thinx Poland"
			return ixp
		elif 3652099328 <= ipnum <= 3652099583:    # B-IX does have ip prefix 217.174.157.0/24
			ixp['peeringdbid'] = 326
			ixp['city']        = "Sofia"
			ixp['name']        = "B-IX"
			ixp['name_long']   = "Balkan Internet Exchange"
			return ixp
		elif 3642573312 <= ipnum <= 3642573823:    # MIX-IT does have ip prefix 217.29.66.0/23
			ixp['peeringdbid'] = 35
			ixp['city']        = "Milan"
			ixp['name']        = "MIX-IT"
			ixp['name_long']   = "Milano Internet eXchange"
			return ixp
		elif 3642573824 <= ipnum <= 3642574335:    # MIX-IT does have ip prefix 217.29.68.0/23
			ixp['peeringdbid'] = 35
			ixp['city']        = "Milan"
			ixp['name']        = "MIX-IT"
			ixp['name_long']   = "Milano Internet eXchange"
			return ixp
		elif 3645874176 <= ipnum <= 3645874687:    # XchangePoint does have ip prefix 217.79.160.0/23
			ixp['peeringdbid'] = 51
			ixp['city']        = "London"
			ixp['name']        = "XchangePoint"
			ixp['name_long']   = "XchangePoint Europe"
			return ixp
		elif 3645874176 <= ipnum <= 3645874687:    # XchangePoint London does have ip prefix 217.79.160.0/23
			ixp['peeringdbid'] = 139
			ixp['city']        = "London"
			ixp['name']        = "XchangePoint London"
			ixp['name_long']   = "XchangePoint Europe"
			return ixp
		elif 3663986688 <= ipnum <= 3663986943:    # PIPE Networks Brisbane does have ip prefix 218.100.0.0/24
			ixp['peeringdbid'] = 110
			ixp['city']        = "BRISBANE"
			ixp['name']        = "PIPE Networks Brisbane"
			ixp['name_long']   = "PIPE Networks Brisbane"
			return ixp
		elif 3663989760 <= ipnum <= 3663990015:    # PIPE Networks Hobart does have ip prefix 218.100.12.0/24
			ixp['peeringdbid'] = 114
			ixp['city']        = "HOBART"
			ixp['name']        = "PIPE Networks Hobart"
			ixp['name_long']   = "PIPE Networks Hobart"
			return ixp
		elif 3663990016 <= ipnum <= 3663990271:    # PIPE Networks Melbourne does have ip prefix 218.100.13.0/24
			ixp['peeringdbid'] = 111
			ixp['city']        = "MELBOURNE"
			ixp['name']        = "PIPE Networks Melbourne"
			ixp['name_long']   = "PIPE Networks Melbourne"
			return ixp
		elif 3663991552 <= ipnum <= 3663991807:    # PIPE Networks Canberra does have ip prefix 218.100.19.0/24
			ixp['peeringdbid'] = 113
			ixp['city']        = "CANBERRA"
			ixp['name']        = "PIPE Networks Canberra"
			ixp['name_long']   = "PIPE Networks Canberra"
			return ixp
		elif 3663987200 <= ipnum <= 3663987455:    # PIPE Networks Sydney does have ip prefix 218.100.2.0/24
			ixp['peeringdbid'] = 105
			ixp['city']        = "Sydney, NSW"
			ixp['name']        = "PIPE Networks Sydney"
			ixp['name_long']   = "Pipe Networks MLPA Sydney"
			return ixp
		elif 3663992064 <= ipnum <= 3663992319:    # PNIX does have ip prefix 218.100.21.0/24
			ixp['peeringdbid'] = 566
			ixp['city']        = "Palmerston North"
			ixp['name']        = "PNIX"
			ixp['name_long']   = "Palmerston North Internet Exchange"
			return ixp
		elif 3663992832 <= ipnum <= 3663993087:    # CHIX-NZ does have ip prefix 218.100.24.0/24
			ixp['peeringdbid'] = 349
			ixp['city']        = "Christchurch"
			ixp['name']        = "CHIX-NZ"
			ixp['name_long']   = "Christchurch Internet Exchange"
			return ixp
		elif 3663993600 <= ipnum <= 3663993855:    # OpenIXP / NiCE does have ip prefix 218.100.27.0/24
			ixp['peeringdbid'] = 375
			ixp['city']        = "Indonesia"
			ixp['name']        = "OpenIXP / NiCE"
			ixp['name_long']   = "National Inter Connection Exchange (NiCE)"
			return ixp
		elif 3663997184 <= ipnum <= 3663997439:    # BIXc does have ip prefix 218.100.41.0/24
			ixp['peeringdbid'] = 452
			ixp['city']        = "Jakarta"
			ixp['name']        = "BIXc"
			ixp['name_long']   = "Biznet Internet Exchange"
			return ixp
		elif 3663997952 <= ipnum <= 3663998207:    # MyIX does have ip prefix 218.100.44.0/24
			ixp['peeringdbid'] = 250
			ixp['city']        = "Kuala Lumpur"
			ixp['name']        = "MyIX"
			ixp['name_long']   = "Malaysia Internet Exchange"
			return ixp
		elif 3664000000 <= ipnum <= 3664000255:    # IX Australia NSW does have ip prefix 218.100.52.0/24
			ixp['peeringdbid'] = 716
			ixp['city']        = "Sydney/NSW"
			ixp['name']        = "IX Australia NSW"
			ixp['name_long']   = "New South Wales Internet Exchange (NSW-IX)"
			return ixp
		elif 3664000512 <= ipnum <= 3664000639:    # IX Australia SA does have ip prefix 218.100.54.0/25
			ixp['peeringdbid'] = 691
			ixp['city']        = "Adelaide/SA"
			ixp['name']        = "IX Australia SA"
			ixp['name_long']   = "South Australian Internet Exchange (SA-IX)"
			return ixp
		elif 3664000640 <= ipnum <= 3664000767:    # IX Australia ACT does have ip prefix 218.100.54.128/25
			ixp['peeringdbid'] = 976
			ixp['city']        = "Canberra/ACT"
			ixp['name']        = "IX Australia ACT"
			ixp['name_long']   = "Australian Capital Territory"
			return ixp
		elif 3664001792 <= ipnum <= 3664002047:    # ACTIX does have ip prefix 218.100.59.0/24
			ixp['peeringdbid'] = 288
			ixp['city']        = "Canberra, ACT"
			ixp['name']        = "ACTIX"
			ixp['name_long']   = "ACT Internet Exchange"
			return ixp
		elif 3663988224 <= ipnum <= 3663988479:    # BBIX Tokyo does have ip prefix 218.100.6.0/24
			ixp['peeringdbid'] = 126
			ixp['city']        = "Tokyo"
			ixp['name']        = "BBIX Tokyo"
			ixp['name_long']   = "BroadBand Internet eXchange Tokyo"
			return ixp
		elif 3664006656 <= ipnum <= 3664006911:    # IX Australia VIC does have ip prefix 218.100.78.0/24
			ixp['peeringdbid'] = 513
			ixp['city']        = "Melbourne/Victoria"
			ixp['name']        = "IX Australia VIC"
			ixp['name_long']   = "Victorian Internet Exchange (VIC-IX)"
			return ixp
		elif 3664008192 <= ipnum <= 3664008447:    # MIX does have ip prefix 218.100.84.0/24
			ixp['peeringdbid'] = 572
			ixp['city']        = "Ulaanbaatar"
			ixp['name']        = "MIX"
			ixp['name_long']   = "Mongolian Internet Exchange"
			return ixp
		elif 624027648 <= ipnum <= 624027711:    # France-IX Marseille does have ip prefix 37.49.232.0/26
			ixp['peeringdbid'] = 880
			ixp['city']        = "Marseille"
			ixp['name']        = "France-IX Marseille"
			ixp['name_long']   = "France-IX Marseille"
			return ixp
		elif 624028672 <= ipnum <= 624029183:    # France-IX does have ip prefix 37.49.236.0/23
			ixp['peeringdbid'] = 359
			ixp['city']        = "Paris"
			ixp['name']        = "France-IX"
			ixp['name_long']   = "FranceIX"
			return ixp
		elif 737350912 <= ipnum <= 737351167:    # AKL-IX does have ip prefix 43.243.21.0/24
			ixp['peeringdbid'] = 977
			ixp['city']        = "Auckland/NZ"
			ixp['name']        = "AKL-IX"
			ixp['name_long']   = "Auckland Internet Exchange "
			return ixp
		elif 737351168 <= ipnum <= 737351679:    # Megaport IX Auckland does have ip prefix 43.243.22.0/23
			ixp['peeringdbid'] = 984
			ixp['city']        = "Auckland"
			ixp['name']        = "Megaport IX Auckland"
		elif 87642112 <= ipnum <= 87643135:    # LONAP does have ip prefix 5.57.80.0/22
			ixp['peeringdbid'] = 53
			ixp['city']        = "London"
			ixp['name']        = "LONAP"
			ixp['name_long']   = "London Network Access Point"
			return ixp
		elif 1044352512 <= ipnum <= 1044352767:    # LIX-LV does have ip prefix 62.63.142.0/24
			ixp['peeringdbid'] = 383
			ixp['city']        = "Riga"
			ixp['name']        = "LIX-LV"
			ixp['name_long']   = "Latvian Internet Exchange"
			return ixp
		elif 1044746752 <= ipnum <= 1044747263:    # ECIX-FRA does have ip prefix 62.69.146.0/23
			ixp['peeringdbid'] = 676
			ixp['city']        = "Frankfurt"
			ixp['name']        = "ECIX-FRA"
			ixp['name_long']   = "European Commercial Internet Exchange Frankfurt"
			return ixp
		elif 1298089728 <= ipnum <= 1298089983:    # Lyonix does have ip prefix 77.95.71.0/24
			ixp['peeringdbid'] = 69
			ixp['city']        = "Lyon"
			ixp['name']        = "Lyonix"
			ixp['name_long']   = "Lyonix, the Lyon IX"
			return ixp
		elif 1311358336 <= ipnum <= 1311358399:    # PhibIX does have ip prefix 78.41.189.128/26
			ixp['peeringdbid'] = 206
			ixp['city']        = "Saint-Etienne"
			ixp['name']        = "PhibIX"
			ixp['name_long']   = "PhibIX Gix & Nap"
			return ixp
		elif 1358548992 <= ipnum <= 1358551039:    # AMS-IX does have ip prefix 80.249.208.0/21
			ixp['peeringdbid'] = 26
			ixp['city']        = "Amsterdam"
			ixp['name']        = "AMS-IX"
			ixp['name_long']   = "Amsterdam Internet Exchange"
			return ixp
		elif 1346609920 <= ipnum <= 1346610175:    # GEIX does have ip prefix 80.67.163.0/24
			ixp['peeringdbid'] = 147
			ixp['city']        = "Paris, London, Amsterdam, Frankfort"
			ixp['name']        = "GEIX"
			ixp['name_long']   = "Gigabit European Internet Exchange"
			return ixp
		elif 1346612992 <= ipnum <= 1346613055:    # Pouix does have ip prefix 80.67.175.0/26
			ixp['peeringdbid'] = 67
			ixp['city']        = "Paris"
			ixp['name']        = "Pouix"
			ixp['name_long']   = "Paris Operators for Universal Internet eXchange"
			return ixp
		elif 1347534848 <= ipnum <= 1347535871:    # DE-CIX Frankfurt does have ip prefix 80.81.192.0/22
			ixp['peeringdbid'] = 31
			ixp['city']        = "Frankfurt"
			ixp['name']        = "DE-CIX Frankfurt"
			ixp['name_long']   = "DE-CIX, the global Internet Exchange"
			return ixp
		elif 1347536640 <= ipnum <= 1347536895:    # DE-CIX Frankfurt does have ip prefix 80.81.199.0/24
			ixp['peeringdbid'] = 31
			ixp['city']        = "Frankfurt"
			ixp['name']        = "DE-CIX Frankfurt"
			ixp['name_long']   = "DE-CIX, the global Internet Exchange"
			return ixp
		elif 1347537408 <= ipnum <= 1347537663:    # DE-CIX Munich does have ip prefix 80.81.202.0/24
			ixp['peeringdbid'] = 248
			ixp['city']        = "Munich"
			ixp['name']        = "DE-CIX Munich"
			ixp['name_long']   = "DE-CIX, the Munich Internet Exchange"
			return ixp
		elif 1347537664 <= ipnum <= 1347537919:    # DE-CIX Hamburg does have ip prefix 80.81.203.0/24
			ixp['peeringdbid'] = 74
			ixp['city']        = "Hamburg"
			ixp['name']        = "DE-CIX Hamburg"
			ixp['name_long']   = "DE-CIX, the Hamburg Internet Exchange"
			return ixp
		elif 1360355328 <= ipnum <= 1360355583:    # CAIX does have ip prefix 81.21.96.0/24
			ixp['peeringdbid'] = 274
			ixp['city']        = "Cairo"
			ixp['name']        = "CAIX"
			ixp['name_long']   = "Cairo Internet eXchange"
			return ixp
		elif 1406404608 <= ipnum <= 1406404863:    # GR-IX does have ip prefix 83.212.8.0/24
			ixp['peeringdbid'] = 347
			ixp['city']        = "Athens"
			ixp['name']        = "GR-IX"
			ixp['name_long']   = "GReek Internet eXchange"
			return ixp
		elif 1410768640 <= ipnum <= 1410768895:    # Sibir-IX does have ip prefix 84.22.159.0/24
			ixp['peeringdbid'] = 822
			ixp['city']        = "Krasnoyarsk"
			ixp['name']        = "Sibir-IX"
			ixp['name_long']   = "Krasnoyarsk Internet Exchange"
			return ixp
		elif 1449688320 <= ipnum <= 1449688575:    # INTERLAN does have ip prefix 86.104.125.0/24
			ixp['peeringdbid'] = 270
			ixp['city']        = "Bucharest"
			ixp['name']        = "INTERLAN"
			ixp['name_long']   = "Interlan Internet Exchange"
			return ixp
		elif 1539336192 <= ipnum <= 1539336447:    # Lviv-IX does have ip prefix 91.192.104.0/24
			ixp['peeringdbid'] = 475
			ixp['city']        = "Lviv"
			ixp['name']        = "Lviv-IX"
			ixp['name_long']   = "Lviv Internet Exchange Point"
			return ixp
		elif 1539496448 <= ipnum <= 1539496703:    # R_ix does have ip prefix 91.194.218.0/24
			ixp['peeringdbid'] = 313
			ixp['city']        = "Rotterdam"
			ixp['name']        = "R_ix"
			ixp['name_long']   = "Rotterdam Internet Exchange"
			return ixp
		elif 1539747840 <= ipnum <= 1539748095:    # Fixo does have ip prefix 91.198.176.0/24
			ixp['peeringdbid'] = 453
			ixp['city']        = "Oslo"
			ixp['name']        = "Fixo"
			ixp['name_long']   = "Free Internet Exchange Oslo"
			return ixp
		elif 1540062976 <= ipnum <= 1540063231:    # YAR-IX does have ip prefix 91.203.127.0/24
			ixp['peeringdbid'] = 683
			ixp['city']        = "Yaroslavl"
			ixp['name']        = "YAR-IX"
			ixp['name_long']   = "Yaroslavl Internet Exchange"
			return ixp
		elif 1540240384 <= ipnum <= 1540240895:    # SwissIX does have ip prefix 91.206.52.0/23
			ixp['peeringdbid'] = 60
			ixp['city']        = "Zurich"
			ixp['name']        = "SwissIX"
			ixp['name_long']   = "Swiss Internet Exchange"
			return ixp
		elif 1540493312 <= ipnum <= 1540494335:    # NIX CZ does have ip prefix 91.210.16.0/22
			ixp['peeringdbid'] = 71
			ixp['city']        = "Prague"
			ixp['name']        = "NIX CZ"
			ixp['name_long']   = "Neutral Internet Exchange"
			return ixp
		elif 1540680448 <= ipnum <= 1540680703:    # OM-NIX does have ip prefix 91.212.235.0/24
			ixp['peeringdbid'] = 1056
			ixp['city']        = "Sofia"
			ixp['name']        = "OM-NIX"
		elif 1540739840 <= ipnum <= 1540740095:    # Peering.cz does have ip prefix 91.213.211.0/24
			ixp['peeringdbid'] = 713
			ixp['city']        = "Prague"
			ixp['name']        = "Peering.cz"
			ixp['name_long']   = "Peering.cz eXchange"
			return ixp
		elif 1540746240 <= ipnum <= 1540746495:    # TOUIX does have ip prefix 91.213.236.0/24
			ixp['peeringdbid'] = 336
			ixp['city']        = "Toulouse"
			ixp['name']        = "TOUIX"
			ixp['name_long']   = "Toulouse Internet eXchange"
			return ixp
		elif 1540704512 <= ipnum <= 1540704767:    # CNIX does have ip prefix 91.213.73.0/24
			ixp['peeringdbid'] = 329
			ixp['city']        = "Cork"
			ixp['name']        = "CNIX"
			ixp['name_long']   = "Cork Neutral Internet Exchange"
			return ixp
		elif 1540899584 <= ipnum <= 1540899839:    # FR-IX does have ip prefix 91.216.67.0/24
			ixp['peeringdbid'] = 410
			ixp['city']        = "Paris"
			ixp['name']        = "FR-IX"
			ixp['name_long']   = "FR-IX"
			return ixp
		elif 1541007104 <= ipnum <= 1541007359:    # IX Leeds does have ip prefix 91.217.231.0/24
			ixp['peeringdbid'] = 435
			ixp['city']        = "Leeds / Western Yorkshire"
			ixp['name']        = "IX Leeds"
			ixp['name_long']   = "Leeds Internet Exchange"
			return ixp
		elif 1541194240 <= ipnum <= 1541194495:    # SIX SI does have ip prefix 91.220.194.0/24
			ixp['peeringdbid'] = 319
			ixp['city']        = "Ljubljana"
			ixp['name']        = "SIX SI"
			ixp['name_long']   = "Slovenian Internet Exchange"
			return ixp
		elif 1541989632 <= ipnum <= 1541989887:    # Rheintal IX does have ip prefix 91.232.229.0/24
			ixp['peeringdbid'] = 543
			ixp['city']        = "LI / CH / AT"
			ixp['name']        = "Rheintal IX"
			ixp['name_long']   = "Rheintal IX Internet Exchange"
			return ixp
		elif 1570528512 <= ipnum <= 1570528767:    # TRDIX does have ip prefix 93.156.93.0/24
			ixp['peeringdbid'] = 342
			ixp['city']        = "Trondheim"
			ixp['name']        = "TRDIX"
			ixp['name_long']   = "Trondheim Internet eXchange"
			return ixp
		ixp['peeringdbid'] = 0
		return ixp
