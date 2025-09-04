
from dotenv import load_dotenv
from tools import calculate,get_planet_mass
import json
from tools import tools_registry
load_dotenv()


class CreateReactAgent:
    def __init__(self,client,system_prompt,tools,tools_registry,max_iterations):
        self.client = client
        self.messages= []
        self.tools_registry = tools_registry
        self.max_iterations = max_iterations
        self.tools=tools
        self.system_prompt = system_prompt
        if self.system_prompt is not None:
            self.messages.append({"role":"system","content":self.system_prompt})

    def __call__(self,message=""):
        if message:
            self.messages.append({"role":"user","content":message})
            
        i=0
        while i<self.max_iterations:
            i+=1
            result = self.execute()
                       
            for item in result:
                
                if getattr(item, "content", None):
                    for content in item.content:
                        if "Answer" in content.text:
                            return content.text
                        self.messages.append({"role":"assistant","content":content.text})
                if item.type == "function_call":
                    self.messages.append({"type":"function_call","name":item.name,"arguments":item.arguments,"call_id":item.call_id})
                    if item.name not in self.tools_registry:
                        self.messages.append({"role":"system","content":f"the Function '{item.name}' was requested but is not available"})
                        continue
                    name = item.name
                    args = json.loads(item.arguments)
                    observation = self.call_function(name,args)
                    self.messages.append({"type":"function_call_output","call_id":item.call_id,"output":json.dumps(observation)})           
                                
        
        return "failed to capture the answer"
            
        

    def execute(self):
        response = self.client.responses.create(
            model="gpt-5",
            tools=self.tools,
            input=self.messages
        )
        return response.output
    
    def call_function(self,name,args):
        func = self.tools_registry[name]
        return func(**args)

    
