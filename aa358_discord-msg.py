import requests


url = "insert request URL"

payload = {
    "content" : "IS 421"
}

headers = {
    "Authorization" : "insert authorization token"
}

res = requests.post(url, payload, headers=headers)
