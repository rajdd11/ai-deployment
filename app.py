from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

print("AI Assistant Started")
print("Type 'exit' to quit\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    try:  
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            You are a professional IT support assistant.
            and you are man of few words
    
            User question:
            {question}
            """
        )
    
        print("\nAI:")
        print(response.text)
        print("\n")

    except Exception as e:
        print("\nError:",e)
        print(e)
        print("\n")