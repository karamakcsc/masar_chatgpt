import frappe
from frappe.model.document import Document
import requests
import json

class ChatGPTIntegration(Document):   
    pass

# separate into functions
    
@frappe.whitelist()
def integration(user_input,model,file):
    
    api_key = str(frappe.db.get_single_value('ChatGPT Settings', 'secret_key'))
    endpoint = str(frappe.db.get_single_value('ChatGPT Settings', 'model'))
        
    if model == "gpt-4" or model == "gpt-4-32k" or model == "gpt-3.5-turbo":
        #endpoint = "https://api.openai.com/v1/chat/completions"
        data = {
        "messages":  [{
            "role": "user",
            "content": user_input
            }],
        "model": model
        }
    elif model == "gpt-3.5-turbo-instruct":
        #endpoint = "https://api.openai.com/v1/completions"
        data = {
            "prompt": user_input,
            "model": model,
            "temperature": 1,
            "max_tokens": 256,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }
    elif model == "dall-e-3":
        #endpoint = "https://api.openai.com/v1/chat/completions"
        data = {
            "model": "dall-e-3",
            "prompt": "a white siamese cat",
            "size": "1024x1024",
            "quality":"standard",
            "n": 1
        }
    # elif model == "tts-1":
    #     #endpoint = "https://api.openai.com/v1/chat/completions"
    #     data = {
    #         "model": "tts-1",
    #         "voice": "alloy",
    #         "input":user_input
    #     }
    else:
        #endpoint = "https://api.openai.com/v1/files"
        data = {
        "id": "file-abc123",
        "object": file,
        "bytes": 175,
        "created_at": 1613677385,
        "filename": "salesOverview.pdf",
        "purpose": "assistants"
        }
            

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(endpoint, headers=headers, json=data)

    if response.status_code == 200:
        result = json.loads(response.text)
        return result['choices'][0]['text']
    elif model == "dall-e-3":
        result = json.loads(response.text)
        return result['data'][0].url
    else:
        return response.text


# # gpt-4 & gpt-4-32k & gpt-3.5-turbo
# def GPTModels():
    
# # gpt-3.5-turbo
# def GPT3Instruct():

# # dall-e-3
# def PhotoGeneration():

# # tts
# def TextToSpeech():