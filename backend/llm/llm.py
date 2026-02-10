from openai import OpenAI
import os

def call_llm(prompt:str):
    llm=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response=llm.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role":"system",
                "content":"You are a helpful nutrition agent who is capable of suggesting scientifically the nutrition summary and ways to improve health when you are given sufficent data about the meals taken in whole day."
            },
            {
                "role":"user",
                "content":prompt
            }
        ]
    )
    return response.choices[0].message.content

