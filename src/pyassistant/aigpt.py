import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_question(question):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content