import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json = login_payload)
login_response_data = login_response.json()

print("Login response: ",login_response.json())
print("Status Code", login_response.status_code)

accessToken = login_response.json()["token"]["accessToken"]

headers = {"Authorization": f"Bearer {accessToken}" }

get_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print(get_response.json())
print(get_response.status_code)