import os
import openai
# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")
#you need three things to make an OPENAI API call
#1 - you need to select a model to use. Model is an agent trained for specfic purposes. 
# In this example we will use the 'gpt-3.5-turbo' model. This is the model behind chatGPT
#2 - you need the name of the API. We will use the 'ChatCompletion' API for this example
#3 - You need to provide the message 
model_to_use = 'gpt-3.5-turbo'
message_object = {"role":"user","content": "write a short story about penguins"}
chat_completion = openai.ChatCompletion.create(model=model_to_use, messages=[message_object])
print(chat_completion)

