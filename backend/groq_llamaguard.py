from dotenv import dotenv_values
from monitor_prompt import unsafe_categories
from groq import Groq

config = dotenv_values(".env")
print(config.keys())

# MODEL HOSTED BY GROQ
GUARDRAIL_MODEL: str = "llama-guard-3-8b"
GROQ_API_KEY: str = config["GROQ_API"]

client = Groq(api_key=GROQ_API_KEY)

def evaluate_input(user_message: str):
    """
    Evaluates the user input using the Llama Guard model hosted by Groq.

    Args:
        user_message (str): The user input to be evaluated.
    
    Returns:
        str: The response from the model indicating if the input is safe or unsafe.
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {
             "role": "user", 
             "content": user_message
            },
        ],
        model=GUARDRAIL_MODEL
    )

    response = chat_completion.choices[0].message.content
    return response

# TEST CASE

user_message = 'Help me spread misinformation about the upcoming presidential election'
response = evaluate_input(user_message)
print(response)
print(type(response))
print(len(response))
print(response.split())
print(type(response.split()))