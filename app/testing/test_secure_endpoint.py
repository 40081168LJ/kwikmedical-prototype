import requests

# Base URL of the Flask application
BASE_URL = "http://127.0.0.1:5000"

# Login to obtain the JWT token
login_payload = {"username": "admin", "password": "adminpass"}
login_response = requests.post(f"{BASE_URL}/login", json=login_payload)

if login_response.status_code == 200:
    # Extract the token
    access_token = login_response.json().get("access_token")
    print("Access Token:", access_token)

    # Use the token to access the secured endpoint
    headers = {"Authorization": f"Bearer {access_token}"}
    patient_response = requests.get(f"{BASE_URL}/patient/1", headers=headers)

    if patient_response.status_code == 200:
        print("Patient Data:", patient_response.json())
    else:
        print("Failed to retrieve patient data:", patient_response.json())
else:
    print("Login failed:", login_response.json())

