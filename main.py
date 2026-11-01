print("Hello from agent!")

# Loading API Key
import os, json
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
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`

from config import system_prompt
from functions.call_function import available_functions, call_function

def main():
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    # Calling Response
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions, # type: ignore
        temperature=0,
    )

    if response.usage is None:
        raise RuntimeError("Prompt usage has evaluated to None, Potentially failed API Request.")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    message = response.choices[0].message
    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, verbose=args.verbose)
            if not result_message.get("content"):
                raise Exception(f"Empty function response for {tool_call.function.name}")
            if args.verbose:
                print(f"-> {result_message['content']}")
    else:
        print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
