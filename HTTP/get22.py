import requests

server = input()
port = int(input())
a = int(input())
b = int(input())

params = {'a': a, 'b': b}
addr = f'{server}:{port}'
response = requests.get(addr, params=params)
j_resp = response.json()
print(*sorted(j_resp["result"]))
print(*sorted(j_resp['check']))