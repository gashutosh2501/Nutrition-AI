

def nutrition_prompt(observation:dict):
    meals=observation["meals"]
    prompt=f"""
    You are a helpful nutrition agent who is capable of suggesting scientifically the nutrition summary and ways to improve health when you are given sufficent data about the meals taken in whole day.
    - You may encounter Indian dishes mostly
    Breakfast : {meals["breakfast"]}
    Lunch: {meals["lunch"]}
    Dinner:{meals["dinner"]}

    Give this structured output only 
    {{
        "summary":"The nutritional summary.",
        "suggestion":["suggestion1","suggestion2"],
        "priority":"low | medium | high",
        "action":" send_email | do_nothing "

    }}
    -No markdown
    -No extra text.
    
"""
    
    return prompt