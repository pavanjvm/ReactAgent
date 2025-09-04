from agent import Agent
from openai import OpenAI
from dotenv import load_dotenv
from system_prompt import system_instruction
from tools import tools
client = OpenAI()
load_dotenv()

agent = Agent(client,system_instruction,tools)