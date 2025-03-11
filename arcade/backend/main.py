from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Don't touch this
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"])

class Highscore(BaseModel):
    player: str
    score: int

highscores = [
    Highscore(player="ALC", score=100),
    Highscore(player="BOB", score=200),
    Highscore(player="CLY", score=300)
]

@app.post("/scores/", summary="Add a new score")
async def add_score(highscore:Highscore):
    highscores.append(highscore)
    return highscore

@app.get("/scores/", response_model=List[dict], summary="Get all scores") # response_model = optional
async def get_scores():
    return [{"player": s.player, "score": s.score} for s in highscores]

@app.delete("/scores/{name}", summary="Delete a score")
async def delete_score(name: str):
    global highscores
    valid_name = [s.player for s in highscores if s.player == name]
    if not valid_name:
        raise HTTPException(status_code=404, detail="Player not found")
    highscores = [s for s in highscores if s.player != name]
    return {"message": "Highscore deleted"}

@app.get("/highscores/", summary="Get all scores, sorted")
async def get_highscores(limit: int = 10):
    sorted_scores = sorted(highscores, key=lambda s: s.score, reverse=True)
    return [{"player": s.player, "score": s.score} for s in sorted_scores[:limit]]
