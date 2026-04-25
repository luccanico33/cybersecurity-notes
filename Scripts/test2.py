import requests

url = "http://scanme.nmap.org/?user=admin"

r = requests.get(url)

print("Status:", r.status_code)
print("Length:", len(r.text))