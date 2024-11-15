from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

fluent_ai = Agent(
    role="English Tutor",
    goal="Have a natural conversation while helping users improve their English",
    verbose=True,
    memory=True,
    backstory="You are FluentAI, a friendly English tutor who helps users improve their English through conversation",
    llm=llm
)

def create_conversation_task(user_input: str) -> Task:
    return Task(
        description=f"""
        Respond to: "{user_input}"
        
        Have a natural conversation while:
        1. Responding in a friendly way
        2. Correcting any grammar mistakes
        3. Suggesting alternative words or expressions
        
        Keep the response format simple:
        Response: [Your conversational response]
        Corrections: [Any grammar corrections]
        Suggestions: [Alternative words or expressions]
        """,
        expected_output="A friendly conversation response with language corrections and suggestions.",
        agent=fluent_ai
    )

def chat():
    print("Welcome to FluentAI! Let's practice English together. (Type 'exit' to end)")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'exit':
            print("\nFluentAI: Goodbye! Thanks for practicing English with me!")
            break
            
        if not user_input:
            continue
            
        try:
            crew = Crew(
                agents=[fluent_ai],
                tasks=[create_conversation_task(user_input)],
                process=Process.sequential
            )
            
            response = crew.kickoff()
            print("\nFluentAI:", response)
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please try again or type 'exit' to quit.")

if __name__ == "__main__":
    chat()