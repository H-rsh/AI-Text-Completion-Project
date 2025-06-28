# Capstone Project: AI-Powered Text Completion
# By: Harsh Chavva

# Part 1: Text Completion App Using Cohere
# Make sure to have run the command in the VS Code terminal: 
    #  pip install cohere
import cohere
from typing import Text
# Make sure to have run the command in the VS Code terminal: 
    # pip3 install python-dotenv
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

configure()

# Load API key securely
api_key = os.getenv("api_key")  # Get the api key from env
if not api_key:
    raise ValueError("Your Cohere API key was not found. Try checking your api_key environment variable.")

co = cohere.Client(api_key)

def genText(input):
    response = co.chat(model = 'command-r-plus',
                       message = input,
                       temperature = 0.8, # How creative the AI's reply is (between 0.0 - 1.0)
                       max_tokens = 150) # How long the AI's reply is
    
    return response.text

def run_genapp():
    print("Welcome to the Cohere Text Generator!")
    
    while True:
        prompt = input("\nPlease enter your prompt (or type 'q' to quit): ").strip()
        
        if prompt.lower() == 'q':
            print("Good bye")
            break
        if not prompt:
            print("You didn't type anything, please enter a something to give a prompt to the AI.")
            continue

        try:
            gText = genText(prompt)
            print("\nThe AI Replied:")
            print(gText.strip())
        except Exception as e:
            print(f"Error: {e}")

run_genapp()