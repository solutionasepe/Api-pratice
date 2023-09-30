import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"


endpoint = "http://localhost:8000/api/product/"

data = {
    "title":"This is the new content",
    "price":12.23
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())

# print(get_response.json())
print(get_response.status_code)