from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Planet(SQLModel, table=True):
    __tablename__ = "planets"

    # id, name, sector
    # bounties: one-to-many relationship to Bounty (with cascade delete)


class Bounty(SQLModel, table=True):
    __tablename__ = "bounties"

    # id, target_name, reward_amount, status
    # planet_id: foreign key to planets.id
    # planet: relationship back to Planet
