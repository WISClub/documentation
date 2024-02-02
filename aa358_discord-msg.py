import requests


url = "insert request URL"

payload = {
    "content" : "insert text to be posted"
}

headers = {
    "Authorization" : "insert authorization token"
}

res = requests.post(url, payload, headers=headers)
