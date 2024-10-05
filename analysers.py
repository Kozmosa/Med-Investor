from openai import OpenAI
from config import *

class Analyser:
    def __init__(self) -> None:
        self.client = OpenAI(
            api_key=MedInvestorConfig.api_key,
            base_url="https://open.bigmodel.cn/api/paas/v4/"
        )
        self.prompts = MedInvestorConfig.prompts
    
    def general(self, prompt="", req=""):
        completion = self.client.chat.completions.create(
            model="glm-4",  
            messages=[    
                {"role": "system", "content": prompt},    
                {"role": "user", "content": req} 
            ],
            top_p=0.7,
            temperature=0.9
        ) 
        return completion.choices[0].message.content
    
    def ctd_analyser(self, req=""):
        return self.general(prompt=self.prompts['ctd_analyser'], req=req)