## Install Instructions

### Backend
- Change directory: `cd backend`
- Create a virtual env: `python -m venv hackenv`
- Activate it: `source hackenv/bin/activate`
- Install libraries: `pip install -r requirements.txt`
- Run the server: `uvicorn main:app --reload`

### Frontend
- Change directory: `cd frontend`
- Run the server: `python3 -m http.server 8000`
