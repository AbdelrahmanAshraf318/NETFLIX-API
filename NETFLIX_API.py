import requests

url = "https://unogs-unogs-v1.p.rapidapi.com/search/deleted"

headers = {
    'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
    'x-rapidapi-key': "1d88541f30msh8c38ae0f0c4461ap175eddjsn69833d430b89"
    }


response = requests.request("GET", url, headers=headers)

print(response.text)