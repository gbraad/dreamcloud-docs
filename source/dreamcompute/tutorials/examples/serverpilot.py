# step-1
import requests
import shade
import json

client_id = 'CLIENT ID GOES HERE'
api_key = 'API KEY GOES HERE'

server_info = json.loads('{"name": "serverpilot"}')
server_endpoint = 'https://api.serverpilot.io/v1/servers'

session = requests.Session()
session.auth = (client_id, api_key)
session.headers = {'Content-Type': 'application/json'}
response_raw = session.post(server_endpoint, json.dumps(server_info))
print(response_raw.content)
response_json = json.loads(response_raw.content)

# step-2
cloud_init='''#!/bin/bash
sudo apt-get update && sudo apt-get -y install wget ca-certificates && \
sudo wget -nv -O serverpilot-installer \
https://download.serverpilot.io/serverpilot-installer && \
sudo sh serverpilot-installer \
--server-id={serverid} \
--server-apikey={serverapikey}
'''.format(serverid=response_json['data']['id'], serverapikey=response_json['data']['apikey'])

conn = shade.OpenStackCloud(cloud='iad2')

image = conn.get_image('Ubuntu-16.04')
flavor_id = '100'
key_name = 'KEY NAME GOES HERE'
conn.create_server(image=image, flavor=flavor_id
        name=server_info['name'], network='public', userdata=cloud_init,
        key_name=key_name)
