from database.database import engine
from sqlalchemy import text


def fetch_db_data(name:str):
    with engine.connect() as conn:

        query=text("""
            SELECT meal_type,sabji
            FROM meals
            WHERE name=:name
            AND meal_type IN ('breakfast','lunch','dinner')
            ORDER BY created_at DESC
            """)
        rows=conn.execute(query,{"name":name}).fetchall()

        meals={}

        for row in rows:
            meals[row.meal_type]=row.sabji

        return {
            "meals":{
                "breakfast":meals["breakfast"],
                "lunch":meals["lunch"],
                "dinner":meals["dinner"]
            }
        }

    
    