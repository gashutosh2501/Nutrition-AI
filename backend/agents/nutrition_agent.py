from backend.agents.base_agent import BaseAgent
from backend.tools.db_tool import fetch_db_data
from backend.tools.email_tool import send_email
from backend.llm.llm import call_llm
from backend.llm.prompts import nutrition_prompt
import json
from backend.tools.email_tool import send_email

class NutritionAgent(BaseAgent):

    def __init__(self,name:str):
        self.name=name

    def observe(self):
        print("HIT OBSERVE")
        observation=fetch_db_data(name=self.name)
        return observation
    def think(self,observation):
        prompt=nutrition_prompt(observation=observation)
        raw_response=call_llm(prompt)
        decision=json.loads(raw_response)
        return decision
    
    def act(self,decision):
        print("HIT ACT")
    
        send_email(
                to="g.ashutosh2502@gmail.com",
                subject="Daily Nutrition Guidance",
                body=decision["summary"]
            )

        return{"status":"email sent"}
    

