from collections import defaultdict
from typing import Dict, List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session, joinedload
from sqlmodel import SQLModel

import models
import schemas
from database import engine, get_db

SQLModel.metadata.create_all(engine)

app = FastAPI(title="Galactic Bounty Board API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def healthcheck():
    return {"message": "Galactic Bounty Board API online"}


# --- Planets ---

@app.post("/planets", response_model=schemas.PlanetOut, status_code=201)
def create_planet(payload: schemas.PlanetCreate, db: Session = Depends(get_db)):
    pass


@app.get("/planets", response_model=List[schemas.PlanetOut])
def list_planets(db: Session = Depends(get_db)):
    pass


@app.get("/planets/{planet_id}", response_model=schemas.PlanetOut)
def get_planet(planet_id: int, db: Session = Depends(get_db)):
    pass


@app.put("/planets/{planet_id}", response_model=schemas.PlanetOut)
def update_planet(planet_id: int, payload: schemas.PlanetUpdate, db: Session = Depends(get_db)):
    pass


@app.delete("/planets/{planet_id}", status_code=204)
def delete_planet(planet_id: int, db: Session = Depends(get_db)):
    pass


# --- Bounties ---

@app.post("/bounties", response_model=schemas.BountyOut, status_code=201)
def create_bounty(payload: schemas.BountyCreate, db: Session = Depends(get_db)):
    pass


@app.get("/bounties", response_model=List[schemas.BountyOut])
def list_bounties(db: Session = Depends(get_db)):
    pass


@app.get("/bounties/{bounty_id}", response_model=schemas.BountyOut)
def get_bounty(bounty_id: int, db: Session = Depends(get_db)):
    pass


@app.put("/bounties/{bounty_id}", response_model=schemas.BountyOut)
def update_bounty(bounty_id: int, payload: schemas.BountyUpdate, db: Session = Depends(get_db)):
    pass


@app.delete("/bounties/{bounty_id}", status_code=204)
def delete_bounty(bounty_id: int, db: Session = Depends(get_db)):
    pass


# --- Reports ---

@app.get("/reports/sector-intel", response_model=List[schemas.SectorIntelGroup])
def sector_intel(db: Session = Depends(get_db)):
    pass
