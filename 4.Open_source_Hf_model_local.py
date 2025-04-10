# We don't need API keys in this we are running it locally
# For First time it can take 10 mins 
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

model_name = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=model_name)
result = model.invoke("What is the capital of India?")
print(result.content)
