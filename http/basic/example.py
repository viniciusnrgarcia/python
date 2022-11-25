import requests
import time

cer = 'CERT.cer'
requests.get("https://url", verify="CERT.cer")

url = 'https://url.com/path'
headers = {
    'Content-Type': 'application/json',
    'accept': 'application/json'
}

body = {'doc':'123','id':'123'}

response = requests.post(url=url, headers=headers, json=body, verify=cer)
print(response.status_code, response.json())

time.sleep(0.5)
