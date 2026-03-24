from fastapi import FastAPI
from app.service import search_service as ss

app=FastAPI()

@app.get('/search-match')
def getSimilarMatch(query:str):
    try:
        matches = ss.getMatches(query)
        return {"status": "SUCCESS", "result": matches}
    except Exception as e:
        print("ERROR:", str(e))
        return {"status": "ERROR", "message": str(e)}