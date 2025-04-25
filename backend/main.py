from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.anagram_checker import IsAnagram

app = FastAPI()

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