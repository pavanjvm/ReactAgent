from agent import CreateReactAgent
from openai import OpenAI
from dotenv import load_dotenv
from system_prompt import system_instruction
from tools import tools,tools_registry
client = OpenAI()
load_dotenv()

agent = Agent(client= client,
              system_prompt = system_instruction,
              tools = tools,
              tools_registry = tools_registry,
              max_iterations=4)

print(agent("what is 2 times the mass of the earth"))