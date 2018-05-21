#!/usr/bin/env python

import consul
import json

c=consul.Consul(host="172.28.128.5",port=8500)

(idx,endpoints)=c.kv.get("network/docker/network/v1.0/endpoint/",recurse=True)
print(endpoints)
epdata=[ ep['Value'] for ep in endpoints if ep['Value'] is not None]

for data in epdata:
    jsondata=json.loads(data.decode("utf-8"))
    print("Endpoint Name: %s" % jsondata["name"])
    print("Interface: %s" % jsondata["ep_iface"])
    # print("IP address: %s" % jsondata["ep_iface"]["addr"])
    # print("MAC address: %s" % jsondata["ep_iface"]["mac"])
    print("Locator: %s\n" % jsondata["locator"])
