import json

# data = {
#   "timestamp": "2018-11-13T03:09:07.716718+0530",
#   "flow_id": 1695390875711035,
#   "in_iface": "eth1",
#   "event_type": "alert",
#   "src_ip": "10.71.9.157",
#   "src_port": 55100,
#   "dest_ip": "10.71.17.101",
#   "dest_port": 161,
#   "proto": "UDP",
#   "alert": {
#     "action": "allowed",
#     "gid": 1,
#     "signature_id": 2101411,
#     "rev": 12,
#     "signature": "GPL SNMP public access udp",
#     "category": "Attempted Information Leak",
#     "severity": 2
#   },
#   "payload": "ME0CAQAEBnB1YmxpY6BAAgMA75sCAQACAQAwMzAPBgsrBgECARkDAgEFAQUAMA8GCysGAQIBGQMFAQEBBQAwDwYLKwYBAgEZAwUBAgEFAA==",
#   "payload_printable": "0M.....public.@...........030...+............0...+............0...+............",
#   "stream": 0,
#   "packet": "AAAMB6zRAB4LNzz7CABFAABrU80AAIARtyUKRwmdCkcRZdc8AKEAV/zYME0CAQAEBnB1YmxpY6BAAgMA75sCAQACAQAwMzAPBgsrBgECARkDAgEFAQUAMA8GCysGAQIBGQMFAQEBBQAwDwYLKwYBAgEZAwUBAgEFAA==",
#   "packet_info": {
#     "linktype": 1
#   },
#   "host": "Pune-01"
# }

# with open("data_file.json", "w") as write_file:
#     json.dump(data, write_file)

# write a data(preferably dictionaries) to a file 

# with open("data_file.json", "r") as r:
# 	data = json.load(r)

# print(data, type(data), sep = "\n")