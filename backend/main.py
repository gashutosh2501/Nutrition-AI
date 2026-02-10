from fastapi import FastAPI
from fastapi import APIRouter
from backend.api.routes import router as routes
from fastapi.middleware.cors import CORSMiddleware
from backend.agents.nutrition_agent import NutritionAgent


from dotenv import load_dotenv
load_dotenv()

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=[
        "http://localhost:5173",
        "https://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_methods=["*"],
    allow_headers=["*"]
)
main_router=APIRouter()

main_router.include_router(routes)

app.include_router(main_router)

@app.get("/")
def check():
    return {"status":"ok","message":"API is running"}

@app.get("/test_agent")
def test_agent():
    agent = NutritionAgent()
    return agent.run()


