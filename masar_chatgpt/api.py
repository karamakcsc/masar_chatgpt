# # Import required modules at the beginning of your script
import frappe
# import openai

# # Set your OpenAI API key
# openai.api_key = "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"

# @frappe.whitelist()
# def get_chat_response(user_input):
#     try:
#         # Use a valid model name, check OpenAI documentation for the latest models
#         model_name = "text-embedding-3-small"  # Replace with the model name you want to use

#         # Create a chat completion using OpenAI Python client
#         assistant_response = openai.Completion.create(
#             engine=model_name,
#             prompt=user_input,
#             temperature=0.7,  # Adjust as needed
#             max_tokens=150,  # Adjust as needed
#         ).choices[0].text.strip()

#         # Save the user input and AI response to the Frappe DocType
#         chat_entry = frappe.new_doc("ChatGPTIntegration")
#         chat_entry.user_input = user_input
#         chat_entry.assistant_response = assistant_response
#         chat_entry.save()

#         return assistant_response

#     except openai.error.OpenAIError as e:
#         return f"OpenAI API Error: {e}"

# Import required modules at the beginning of your script
# import frappe
# import openai

# # Set your OpenAI API key
# openai.api_key = "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"

# Import required modules at the beginning of your script
# Import required modules at the beginning of your script





############################################### Check from where ???
# import frappe
# import openai

# # Set your OpenAI API key
# openai.api_key = "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"

# @frappe.whitelist()
# def get_chat_response(user_input):
#     try:
#         # Use the GPT-3 model for text completion
#         model_name = "gpt-3.5-turbo-1106"

#         # Create a chat completion using OpenAI Python client
#         assistant_response = openai.Completion.create(
#             model=model_name,
#             prompt=user_input,
#             temperature=0.5,  # Adjust as needed
#             max_tokens=100,  # Adjust as needed
#         ).choices[0].text.strip()

#         # Save the user input and AI response to the Frappe DocType
#         chat_entry = frappe.new_doc("ChatGPTIntegration")
#         chat_entry.user_input = user_input
#         chat_entry.assistant_response = assistant_response
#         chat_entry.save()

#         return assistant_response

#     except openai.error.OpenAIError as e:
#         return f"OpenAI API Error: {e}"
