import requests

url = "https://remotive.com/api/remote-jobs"

response = requests.get(
    url,
    headers={"User-Agent": "JobScope/0.1"},
    timeout=15,
)

print("Status:", response.status_code)

data = response.json()

print("Tipo:", type(data))
print("Ofertas:", len(data.get("jobs", [])))

if data.get("jobs"):
    print(data["jobs"][0])
else:
    print("Sin ofertas")
