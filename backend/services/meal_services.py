from backend.tools.db_tool import fetch_db_data
from backend.agents.nutrition_agent import NutritionAgent
from database.database import engine
from sqlalchemy import text
from backend.schemas.diet import Entry


def agent_email_task(payload:Entry):

    with engine.connect() as conn:
        query=text(""" 
                INSERT INTO meals(name,meal_type,sabji)
                   VALUEs (:name,:time,:ate)
        """)
        
        conn.execute(query,{
            "name":payload.name,
            "time":payload.time,
            "ate":payload.ate
        })

        conn.commit()
    
    if payload.time=="dinner":
        agent=NutritionAgent(name=payload.name)
        agent.run()
    
    
