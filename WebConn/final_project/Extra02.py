import requests

url = "http://google.com"
response = requests.get(url)
response.raise_for_status()

print(len(response.text)) 
print(response.text)

with open("google.html", "w", encoding="utf8") as google: 
	google.write(response.text)