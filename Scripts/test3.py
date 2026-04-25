import requests

urls = [
    "http://scanme.nmap.org",
    "http://scanme.nmap.org/admin",
    "http://scanme.nmap.org/test"
]

for url in urls:
    r = requests.get(url)
    print(url, "->", r.status_code)
