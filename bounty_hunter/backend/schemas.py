from __future__ import annotations

from typing import List, Literal

from pydantic import BaseModel, ConfigDict


class PlanetBase(BaseModel):
    name: str
    sector: str


class PlanetCreate(PlanetBase):
    pass


class PlanetUpdate(PlanetBase):
    pass


class PlanetOut(PlanetBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class BountyBase(BaseModel):
    target_name: str
    reward_amount: int
    status: Literal["Active", "Captured"] = "Active"
    planet_id: int


class BountyCreate(BountyBase):
    pass


class BountyUpdate(BountyBase):
    pass


class BountyOut(BountyBase):
    id: int
    planet: PlanetOut

    model_config = ConfigDict(from_attributes=True)


class SectorIntelGroup(BaseModel):
    sector: str
    bounties: List[BountyOut]
