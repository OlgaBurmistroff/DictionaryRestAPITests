import requests

url = 'http://127.0.0.1:8080/eng_to_ua'

item = {"apple": 'яблуко'}

response = requests.get(url)
print(response.text)

response = requests.put(url)
print(response.text)

response = requests.post(url, data=item)
print(response.text)

response = requests.delete(url)
print(response.text)
