from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

# 1. Define a list of callable tools for the model
from tools import tools

# Create a running input list we will add to over time
input_list = [
    {"role": "user", "content": "mass of planet earth"}
]

# 2. Prompt the model with tools defined
response = client.responses.create(
    model="gpt-5",
    tools=tools,
    input=input_list,
)

# Save function call outputs for subsequent requests
input_list += response.output
print(response.output)
print(input_list)