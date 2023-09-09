import os
import openai
messages_input = []
model_to_use = 'gpt-3.5-turbo'
openai.api_key = os.getenv("OPENAI_API_KEY")
def send_message(message_to_send):
    message = {"role":"user","content": message_to_send}
    messages_input.append(message)
    chat_completion = openai.ChatCompletion.create(model=model_to_use, messages=messages_input)
    #extract choices
    choices = chat_completion['choices']
    print(chat_completion)
    index = 0
    for choice in choices:
        chatgpt_response = choice['message']
        content = chatgpt_response['content']
        txt1 = "Message for index {idx}, is {msg}".format(idx = index, msg = content)
        print(txt1)
        index = index+1 

message_to_send = input("Enter message to send:")
print("message: " + message_to_send)
# Load your API key from an environment variable or secret management service
send_message(message_to_send)

