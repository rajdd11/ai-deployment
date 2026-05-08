from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

question = input("Ask something: ")

# The model string has been updated to a supported version
response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents=question
)

print("\nAI Response:\n")
print(response.text)