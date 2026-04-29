from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlmodel import SQLModel

import models
from database import engine


@dataclass(frozen=True)
class PlanetSeed:
    name: str
    sector: str


@dataclass(frozen=True)
class BountySeed:
    target_name: str
    reward_amount: int
    status: str
    planet_name: str


PLANETS: list[PlanetSeed] = [
    PlanetSeed(name="Corvax Prime", sector="Outer Rim"),
    PlanetSeed(name="Nemoris", sector="Outer Rim"),
    PlanetSeed(name="Vyr-7", sector="Mid Core"),
    PlanetSeed(name="Aetheron", sector="Mid Core"),
    PlanetSeed(name="Tarsis Delta", sector="Inner Core"),
    PlanetSeed(name="Helion Reach", sector="Inner Core"),
    PlanetSeed(name="Krynn Outpost", sector="Frontier Expanse"),
    PlanetSeed(name="Zalara", sector="Frontier Expanse"),
]

BOUNTIES: list[BountySeed] = [
    BountySeed(target_name="Nyx Voss", reward_amount=18000, status="Active", planet_name="Corvax Prime"),
    BountySeed(target_name="Drax Kelm", reward_amount=12000, status="Captured", planet_name="Corvax Prime"),
    BountySeed(target_name="Iria Quell", reward_amount=14500, status="Active", planet_name="Nemoris"),
    BountySeed(target_name="Mako Rynn", reward_amount=9800, status="Active", planet_name="Nemoris"),
    BountySeed(target_name="Talos Grimm", reward_amount=26000, status="Active", planet_name="Vyr-7"),
    BountySeed(target_name="Sera Kade", reward_amount=11200, status="Captured", planet_name="Vyr-7"),
    BountySeed(target_name="Orin Vale", reward_amount=15400, status="Active", planet_name="Aetheron"),
    BountySeed(target_name="Juno Kreel", reward_amount=8700, status="Captured", planet_name="Aetheron"),
    BountySeed(target_name="Kael Thorn", reward_amount=30200, status="Active", planet_name="Tarsis Delta"),
    BountySeed(target_name="Vexa Marr", reward_amount=22100, status="Active", planet_name="Helion Reach"),
    BountySeed(target_name="Garr Vox", reward_amount=13500, status="Captured", planet_name="Helion Reach"),
    BountySeed(target_name="Rook Sentinel", reward_amount=17600, status="Active", planet_name="Krynn Outpost"),
    BountySeed(target_name="Lira Skarn", reward_amount=9400, status="Active", planet_name="Krynn Outpost"),
    BountySeed(target_name="Tarn Eclipse", reward_amount=24800, status="Active", planet_name="Zalara"),
    BountySeed(target_name="Cinder Wren", reward_amount=12600, status="Captured", planet_name="Zalara"),
]


def seed() -> None:
    SQLModel.metadata.create_all(engine)

    with Session(engine) as db:
        existing_planets = {
            planet.name: planet
            for planet in db.execute(select(models.Planet)).scalars().all()
        }

        for planet_seed in PLANETS:
            if planet_seed.name in existing_planets:
                planet = existing_planets[planet_seed.name]
                planet.sector = planet_seed.sector
            else:
                planet = models.Planet(name=planet_seed.name, sector=planet_seed.sector)
                db.add(planet)
                existing_planets[planet_seed.name] = planet

        db.flush()

        existing_bounties = {
            (bounty.target_name, bounty.planet_id): bounty
            for bounty in db.execute(select(models.Bounty)).scalars().all()
        }

        for bounty_seed in BOUNTIES:
            planet = existing_planets.get(bounty_seed.planet_name)
            if planet is None:
                continue

            key = (bounty_seed.target_name, planet.id)
            if key in existing_bounties:
                bounty = existing_bounties[key]
                bounty.reward_amount = bounty_seed.reward_amount
                bounty.status = bounty_seed.status
            else:
                db.add(
                    models.Bounty(
                        target_name=bounty_seed.target_name,
                        reward_amount=bounty_seed.reward_amount,
                        status=bounty_seed.status,
                        planet_id=planet.id,
                    )
                )

        db.commit()


if __name__ == "__main__":
    seed()
    print("Seed complete: planets and bounties are ready.")
