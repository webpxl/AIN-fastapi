from sqlalchemy.orm import Session
from sqlmodel import SQLModel

import models
from database import engine


def seed() -> None:
    SQLModel.metadata.create_all(engine)

    with Session(engine) as db:
        # Create your planets and bounties here
        pass


if __name__ == "__main__":
    seed()
    print("Seed complete.")
