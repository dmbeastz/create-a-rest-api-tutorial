import requests

BASE = "http://127.0.0.1:5000"

data = [{"likes": 78, "name": "Joe", "views": 100000},
        {"likes": 10, "name": "How to make a REST API", "views": 80000},
        {"likes": 35, "name": "Tim", "views": 2000}]

for i, video in enumerate(data):
    response = requests.put(f"{BASE}/video/{i}", json=video)
    print(response.json())

# input("Press Enter to continue...")
# response = requests.get(f"{BASE}/video/6")
# print(response.json())

# input("Press Enter to continue...")

# response = requests.delete(f"{BASE}/video/6")
# print(response.status_code)

i = 2 # Define i with a specific value
input("Press Enter to continue...")
response = requests.patch(f"{BASE}/video/{i}", json={"name": "Updated Name", "views": 100, "likes": 50})
print(response.json())



# PUT request
# response_put = requests.put(f"{BASE}/video/1", json={"likes": 10, "name":"Tim", "views": 100000})
# print("PUT Response content:", response_put.content)  # Print the response content
# try:
#     json_data_put = response_put.json()
#     print("PUT Response JSON:", json_data_put)
# except Exception as e:
#     print("PUT Error parsing JSON:", e)

# GET request
# response_get = requests.get(f"{BASE}/video/1")
# print("GET Response content:", response_get.content)  # Print the response content
# try:
#     json_data_get = response_get.json()
#     print("GET Response JSON:", json_data_get)
# except Exception as e:
#     print("GET Error parsing JSON:", e)
