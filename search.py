import os
from ai import audio,speak
import openai
openai.api_key = 'KEY'
messages = [ {"role": "system", "content": "You are an intelligent assistant." } ]
def info():

    message=audio().replace(" ","")

    messages.append(
        {"role": "user", "content": message},
    )

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message

    print("Assistant: ", reply.content)
    speak(reply.content)

    messages.append(reply)
