#Insufficient Balance for Quota
import os
from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
llm=OpenAI(model='gpt-3.5-turbo-instruct',temperature=0,)
result=llm.invoke('Who is Prime Minister of India')
print(result)