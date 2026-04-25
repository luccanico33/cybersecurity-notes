import requests

r = requests.get("http://scanme.nmap.org")
print("Status:", r.status_code)
print("Length:", len(r.text))