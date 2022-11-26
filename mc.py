import requests
import json

headers = {
        "Authorization": "Bearer 2I4JRY5F5mXkb0MKJoxTHA9V1O0_7ghKThA5rUQiG3SUaaLWr",
        "Ngrok-Version": "2"
        }

r = requests.get('https://api.ngrok.com/tunnels',headers=headers)
r = json.loads(r.text)
url = r["tunnels"][0]["public_url"][6:]
print(url)
id = url[0]
print(id)
port = url[-5:]
print(port)
headers = {
            'Authorization': 'Bearer 3UcIPhPXL2bas5tlS1q0Y2zB5omxMCQ7hrCBvD08',
            'Content-Type': 'application/json'
        }
r = requests.get('https://api.cloudflare.com/client/v4/zones/755157d403761b93bd8412a593dfff6a/dns_records?type=SRV',headers=headers)
r = json.loads(r.text)
idd = r["result"][0]["id"]
print(idd)
r = requests.delete('https://api.cloudflare.com/client/v4/zones/755157d403761b93bd8412a593dfff6a/dns_records/'+idd,headers=headers)
data = {
            "type":"SRV",
            "data":{
                "name":"mc.leee.eu.org",
                "port": port,
                "priority":1,
                "proto":"_tcp",
                "service":"_minecraft",
                "target": id+".tcp.ngrok.io",
                "weight":1,
                "ttl":1,
            }
        }
a = requests.post('https://api.cloudflare.com/client/v4/zones/755157d403761b93bd8412a593dfff6a/dns_records',headers = headers,data = json.dumps(data))
print(a.text)
