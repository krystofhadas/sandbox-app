from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.anagram_checker import IsAnagram

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:63342"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnagramRequest(BaseModel):
    str1: str
    str2: str

@app.post("/is-anagram")
def check_anagram(data: AnagramRequest):
    try:
        result = IsAnagram.is_anagram(data.str1, data.str2)
        return {"is_anagram": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))