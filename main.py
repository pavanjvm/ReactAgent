from openai import OpenAI

import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

class Agent:
    def __init__(self,client,system_prompt):
        self.client = client
        self.messages= []
        self.system_prompt = system_prompt
        if self.system_prompt is not None:
            self.messages.append({"role":"system","content":self.system_prompt})

    def __call__(self,message):
        if message:
            self.messages.append({"role":"user","content":message})
        result = self.execute()
        self.messages.append({"role":"system","content":result})
        return result
    
    def execute(self):
        response = client.responses.create(
            model="gpt-5",
            input=self.messages
        )
        return response.output_text


new_agent=Agent(client,"you are a chat assistant")



print(new_agent("hi"))
print(new_agent.messages)