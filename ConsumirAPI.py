import requests

url = "https://open.er-api.com/v6/latest/USD"

requisicao = requests.get(url)

print(requisicao.status_code)

if requisicao.status_code == 200:
    print(requisicao.json()["rates"]["BRL"])
