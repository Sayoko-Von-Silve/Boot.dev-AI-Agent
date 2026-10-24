print("Hello from agent!")

# Loading API Key
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key or api_key == "" or api_key == None:
    raise RuntimeError("OPENROUTER_API_KEY is not available, please check your .env file.")

# Assigning Client OpenAI to API Key
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

import argparse

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()
# Now we can access `args.user_prompt`

def main():
    # Calling Response
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": args.user_prompt,
            }
        ],
    )

    if response.usage is None:
        raise RuntimeError("Prompt usage has evaluated to None, Potentially failed API Request.")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
