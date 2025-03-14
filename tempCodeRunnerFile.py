import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_code(prompt):
    """Generate Python code using OpenAI GPT-3.5 Turbo."""
    client = openai.OpenAI()  

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # ✅ Use GPT-3.5-Turbo instead of GPT-4
        messages=[
            {"role": "system", "content": "You are an AI coding assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content

# Test prompt
if __name__ == "__main__":
    prompt = "Write a Python function to check if a number is prime."
    generated_code = generate_code(prompt)
    print("Generated Code:\n", generated_code)
