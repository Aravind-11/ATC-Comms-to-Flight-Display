## Transcribing and Interpreting Air-Traffic-Controller Communications to the pilot's display

### Setup 

Use python 3.7 and above

- Install Whisper

```pip install -U openai-whisper```
- Support tool
  
```brew install ffmpeg```

- Install Replicate

  ```pip install replicate```

- A replicate token from the replicate website can be retrieved and used here

  ```export REPLICATE_API_TOKEN=<paste-your-token-here>```

### Install Instructions

#### Backend
- Change directory: `cd backend`
- Create a virtual env: `python -m venv hackenv`
- Activate it: `source hackenv/bin/activate`
- Install libraries: `pip install -r requirements.txt`
- Run the server: `uvicorn main:app --reload`

#### Frontend
- Change directory: `cd frontend`
- Run the server: `python3 -m http.server 8000`
