from typing import List, Optional, TYPE_CHECKING

import sqlmodel as sm

if TYPE_CHECKING:
    from .hero import Hero, HeroRead


class TeamBase(sm.SQLModel):
    name: str
    headquarters: str


class Team(TeamBase, table=True):
    id: Optional[int] = sm.Field(default=None, primary_key=True)

    heroes: List["Hero"] = sm.Relationship(back_populates="team")


class TeamCreate(TeamBase):
    pass


class TeamRead(TeamBase):
    id: int


class TeamUpdate(sm.SQLModel):
    id: Optional[int] = None
    name: Optional[str] = None
    headquarters: Optional[str] = None


class TeamReadWithHeroes(TeamRead):
    heroes: List["HeroRead"] = []
