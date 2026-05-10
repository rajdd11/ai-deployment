from google import genai
from google.genai import errors # Added to catch specific API errors
from dotenv import load_dotenv
import os
import time # Added to handle the delay

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)

print("=" * 50)
print("Enterprise IT Troubleshooting Assistant")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    issue = input("\nDescribe the issue:\n")

    if issue.lower() == "exit":
        print("\nClosing assistant...")
        break

    prompt = f"""
    You are an experienced enterprise IT support engineer.

    Analyze the following issue carefully.
    Try to keep response short whenever you can, dont give leanthy explanations
    Provide:
    1. Possible root causes
    2. Troubleshooting steps
    3. Severity level
    4. Escalation recommendation if needed

    Keep the response professional and structured.

    Issue:
    {issue}
    """

    # --- Throttling & Retry Logic Starts Here ---
    while True:
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=prompt
            )

            print("\nAI Troubleshooting Report:\n")
            print(response.text)
            
            # Break out of the retry loop once successful
            break 

        except errors.ClientError as e:
            # Catch the specific 429 Rate Limit error
            if e.code == 429:
                print("\n[!] Rate limit exceeded. Throttling for 48 seconds to reset quota...")
                time.sleep(48)
                print("Retrying request now...")
                continue # Loops back to the try block to attempt the call again
            else:
                # Handle other API errors (like 404, 500)
                print("\n[!] API Error occurred:")
                print(e)
                break 

        except Exception as e:
            # Handle standard Python errors (network drops, etc.)
            print("\n[!] Unexpected Error occurred:")
            print(e)
            break