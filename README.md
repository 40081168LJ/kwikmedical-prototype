---

# KwikMedical System

KwikMedical is a distributed, service-oriented system designed to manage emergency medical calls and ambulance dispatches. The system integrates with a central patient database, processes ambulance requests, and sends patient medical records to ambulances and hospitals. The project also implements role-based authentication using JSON Web Tokens (JWT) to secure sensitive medical data.

## Table of Contents

- [KwikMedical System](#kwikmedical-system)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
    - [Authentication](#authentication)
    - [Patient Records](#patient-records)
    - [Emergency Calls](#emergency-calls)
    - [Ambulance Dispatch](#ambulance-dispatch)
  - [Error Handling](#error-handling)
  - [Real-Time Updates](#real-time-updates)
  - [Future Enhancements](#future-enhancements)

## Features

- **Service-Oriented Architecture**: Modular services for emergency calls, patient records, ambulance dispatch, and medical record updates.
- **JWT-Based Authentication**: Secures endpoints with role-based access (admin/operator roles).
- **RESTful APIs**: Each service exposes its own REST API for data exchange.
- **SQLite Database Integration**: Stores and retrieves patient medical records.
- **Asynchronous Messaging**: Uses RabbitMQ (or another message broker) to handle ambulance dispatch asynchronously.
- **WebSocket Integration**: (Future enhancement) Real-time updates for ambulance location and status.

## Technologies Used

- **Flask**: Web framework for building REST APIs.
- **Flask-JWT-Extended**: JWT-based authentication for securing endpoints.
- **SQLite**: Database for storing patient medical records.
- **RabbitMQ**: (Optional) Message broker for asynchronous communication between services.
- **HTML/CSS/JavaScript**: Front-end interface for entering emergency calls and dispatching ambulances.
- **WebSockets**: (Future) Real-time communication for ambulance tracking.

## Project Structure

```bash
kwikmedical-prototype/
├── app/
│   ├── __init__.py                    # Main app initialization
│   ├── emergency_call_service.py       # Emergency call management
│   ├── patient_records_service.py      # Patient database interactions
│   ├── ambulance_dispatch_service.py   # Ambulance dispatch logic
│   ├── auth_service.py                 # User authentication with JWT
│   ├── static/
│   │   ├── css/                        # Front-end styles
│   │   ├── js/                         # Front-end logic (JavaScript)
│   │   └── img/                        # Images including favicon
│   └── templates/
│       └── index.html                  # Front-end template for emergency call input
├── data/
│   └── patients.db                     # SQLite database for patient records
├── run.py                              # Main script to start the application
├── create_db.py                        # Script to create and populate the database
├── requirements.txt                    # Project dependencies
└── README.md                           # Project README
```

## Installation

### Prerequisites

- **Python 3.7+**
- **SQLite** (optional, SQLite is bundled with Python)
- **RabbitMQ** (optional, for asynchronous messaging)

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/kwikmedical.git
   cd kwikmedical
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Create the database**:

   Run the `create_db.py` script to create the SQLite database and populate it with sample data:

   ```bash
   python create_db.py
   ```

## Running the Application

1. **Start the Flask application**:

   ```bash
   python run.py
   ```

2. Open your browser and navigate to:

   ```
   http://127.0.0.1:5000
   ```

3. Use Postman or a similar tool to interact with the API, or use the front-end form to submit emergency calls.

## API Endpoints

### Authentication

- **POST `/login`**: Authenticate users and retrieve a JWT.

  Example Request Body:

  ```json
  {
    "username": "admin",
    "password": "adminpass"
  }
  ```

  Example Response:

  ```json
  {
    "access_token": "your_jwt_token_here"
  }
  ```

### Patient Records

- **GET `/patient/<int:patient_id>`**: Retrieve patient medical history.

  Example:

  ```
  GET /patient/1
  ```

  Response:

  ```json
  {
    "id": 1,
    "name": "John Doe",
    "nhs_number": "NHS12345",
    "medical_history": "Hypertension, Diabetes"
  }
  ```

### Emergency Calls

- **POST `/emergency-call`**: Submit details for an emergency call.

  Example Request Body:

  ```json
  {
    "patient_id": 1,
    "condition": "Cardiac Arrest",
    "location": "123 Main Street"
  }
  ```

  Example Response:

  ```json
  {
    "message": "Ambulance dispatched successfully!",
    "dispatch_details": {
      "status": "Success",
      "message": "Ambulance dispatched to 123 Main Street for John Doe"
    }
  }
  ```

### Ambulance Dispatch

- **POST `/dispatch-ambulance`**: Dispatch an ambulance to the patient location.

  Example Request Body:

  ```json
  {
    "patient_id": 1,
    "name": "John Doe",
    "condition": "Cardiac Arrest",
    "location": "123 Main Street"
  }
  ```

  Example Response:

  ```json
  {
    "status": "Success",
    "message": "Ambulance dispatched to 123 Main Street for John Doe"
  }
  ```

## Error Handling

The system handles errors gracefully, returning appropriate error messages:

- **400 Bad Request**: When input data is invalid.
- **401 Unauthorized**: When an invalid JWT or no token is provided for protected routes.
- **404 Not Found**: When a resource (such as a patient) is not found.

Example Error Response:

```json
{
  "msg": "Bad username or password"
}
```

## Real-Time Updates

A future enhancement includes implementing **WebSockets** to provide real-time updates on ambulance locations and status during an emergency. This will ensure that hospital staff and emergency call centers are continuously updated on the ambulance's location and estimated time of arrival.

## Future Enhancements

- **WebSocket Integration**: Real-time ambulance location updates.
- **Advanced Role-Based Access Control**: More granular roles and permissions.
- **GPS Integration**: For dispatching ambulances based on the nearest available unit.
- **Database Migration**: Expand the SQLite database to PostgreSQL for enhanced scalability.
- **Monitoring and Logging**: Implement monitoring to track system performance and usage.

---

Feel free to clone the repository, contribute, or raise issues if you encounter any problems. We appreciate feedback and welcome collaboration!

---
