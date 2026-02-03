from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()

API_KEY = "test123"

class VoiceRequest(BaseModel):
   {
  "language": "English",
  "audio_format": "mp3",
  "audio_base64": "dummy"
}


@app.post("/detect")
def detect_voice(data: VoiceRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    {
  "language": "english",
  "audio_format": "mp3",
  "audio_base64": "dummy"
}


    return {
        "classification": "AI Generated",
        "confidence": 0.85,
        "explanation": "Voice characteristics indicate synthetic patterns"
    }


