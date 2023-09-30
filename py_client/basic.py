import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"


endpoint = "http://localhost:8008/api/"

get_response = requests.get(endpoint, params={"abc":123}, json={"query": "Hello this is an api project"})
print(get_response.json())

# print(get_response.json())
print(get_response.status_code)