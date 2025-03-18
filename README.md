# Event Booking System

## Overview
The **Event Booking System** is a web-based application that allows users to browse events, book tickets, and manage their reservations. The system consists of a **FastAPI backend**, a **React.js frontend**, and an **auto-generated Python SDK** to interact with the API.

## Project Structure
```
event_booking_system/
├── backend/            # FastAPI backend
│   ├── main.py         # Entry point for FastAPI
│   ├── models.py       # Database models
│   ├── schemas.py      # Pydantic schemas
│   ├── crud.py         # CRUD operations
│   ├── database.py     # Database connection
│   ├── routes/         # API endpoints
│   │   ├── events.py   # Event-related APIs
│   │   ├── users.py    # User authentication APIs
│   │   ├── bookings.py # Booking APIs
│   ├── tests/          # Unit tests
│   │   ├── test_events.py
│   │   ├── test_users.py
│   │   ├── test_bookings.py
│   ├── requirements.txt # Dependencies
│   ├── openapi.json     # API specification
│
├── frontend/           # React.js frontend
│   ├── src/
│   │   ├── components/  # UI components
│   │   ├── pages/       # Page components
│   │   ├── App.js       # Main app component
│   │   ├── index.js     # React entry point
│   ├── package.json     # Frontend dependencies
│   ├── README.md        # Frontend setup guide
│
├── sdk/                # Auto-generated Python SDK
│   ├── event_sdk/
│   │   ├── events_api.py
│   │   ├── users_api.py
│   │   ├── bookings_api.py
│   ├── setup.py         # SDK installation
│
├── scripts/            # Automation scripts
│   ├── setup.sh        # Set up environment
│   ├── run.sh          # Run backend and frontend
│
└── README.md           # Project documentation
```

## Backend Setup (FastAPI)
### Prerequisites
- Python 3.8+
- FastAPI
- SQLAlchemy
- PostgreSQL or SQLite

### Installation Steps
1. Navigate to the `backend/` directory:
   ```sh
   cd backend
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Start the FastAPI server:
   ```sh
   uvicorn main:app --reload
   ```
4. Access the API documentation at:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Frontend Setup (React.js)
### Prerequisites
- Node.js (v14+)
- npm or yarn

### Installation Steps
1. Navigate to the `frontend/` directory:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the React application:
   ```sh
   npm start
   ```
4. Open the frontend in a browser at `http://localhost:3000`

## SDK Installation & Usage
1. Navigate to the `sdk/` directory:
   ```sh
   cd sdk
   ```
2. Install the SDK package:
   ```sh
   pip install .
   ```
3. Example usage of the SDK:
   ```python
   from event_sdk.events_api import get_events
   events = get_events()
   print(events)
   ```

## Running Tests
### Backend Tests
Run FastAPI backend tests using pytest:
```sh
cd backend
test -m pytest
```
### Frontend Tests
Run React tests using Jest:
```sh
cd frontend
npm test
```

## Deployment
- Backend: Can be deployed on **Heroku**, **AWS Lambda**, or **Docker**.
- Frontend: Can be deployed on **Vercel**, **Netlify**, or **GitHub Pages**.

## Contributors
- **Sudhiksha M K** - Developer


This README provides a comprehensive guide to setting up and running the **Event Booking System** project.

