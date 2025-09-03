from openai import OpenAI
from agent import Agent
from system_prompt import system_instruction
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

new_agent=Agent(client,system_instruction)

print(new_agent("hi"))
print(new_agent.messages)