from fastapi import APIRouter
from backend.services.meal_services import agent_email_task
from pydantic import BaseModel

router=APIRouter()


class Entry(BaseModel):
    name:str
    ate:str
    time:str


@router.post("/data")
def agent_email(payload:Entry):
    return agent_email_task(payload)