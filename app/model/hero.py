from typing import Optional

import sqlmodel as sm


from .team import Team, TeamRead


class HeroBase(sm.SQLModel):
    name: str
    secret_name: str
    age: Optional[int] = None

    team_id: Optional[int] = sm.Field(default=None, foreign_key="team.id")


class Hero(HeroBase, table=True):
    id: Optional[int] = sm.Field(default=None, primary_key=True)

    team: Optional[Team] = sm.Relationship(back_populates="heroes")


class HeroRead(HeroBase):
    id: int


class HeroCreate(HeroBase):
    pass


class HeroUpdate(sm.SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
    team_id: Optional[int] = None


class HeroReadWithTeam(HeroRead):
    team: Optional[TeamRead] = None
