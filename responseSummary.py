import os
import openai

openai.api_key = "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"

question1 = "How are you feeling today?"
response1 = input("> ")

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"You are an expert therapist, your patient is a veteran who is suffering with mental health issues, possibly depression, anxiety, or PTSD, they have answered some short answer questions and based on their responses give them some advice. Question #1: {question1}, Response #1: {response1}."}])
print(completion.choices[0].message.content)