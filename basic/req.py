import requests

r = requests.get("http://google.com")
ct = r.headers['content-type']
print(r.status_code, ct)
# print(r.text)

