import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"


endpoint = "http://localhost:8000/api/product/1/update"

data = {
    "title":"trying",
    "price":12.67
}
get_response = requests.put(endpoint, json=data)
print(get_response.json())

# print(get_response.json())
print(get_response.status_code)