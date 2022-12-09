import concurrent.futures as concurrent
import requests
import time


def post(request):
    url = 'https://order.com.br/v1/order'
    cer = 'certificate.cer'
    headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }
    sequence, body = request # desempacotamento
    response = requests.post(url=url, headers=headers, json=body, verify=cer, timeout=None)

took = time.perf_counter()
file = open('input.txt')
lines = file.readlines()

requests = []
for i in range(10):
    body = {'id':'{0}','value':'{1}','item':[1,2,3]}
    body['id'] = i
    body['value'] = 120
    requests.append(body)


with concurrent.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(post, enumerate(requests))
    executor.shutdown()


print('time elapsed: {}', time.perf_counter() - took)