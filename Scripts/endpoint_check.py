import requests

urls = [
    "http://scanme.nmap.org",
    "http://scanme.nmap.org/admin",
    "http://scanme.nmap.org/test"
]

for url in urls:
    try:
        r = requests.get(url, timeout=3)
        print(f"{url} -> {r.status_code}")
    except:
        print(f"{url} -> error")
