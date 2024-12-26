from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    surname: str
    team: str
    position: str
