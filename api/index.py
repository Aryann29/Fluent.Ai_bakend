from flask import Flask, request, jsonify
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import json

app = Flask(__name__)
load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", #or gemini-1.5-pro
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
        
        Format your response as valid JSON with these keys:
        {{
            "response": "your conversational response",
            "corrections": "any grammar corrections",
            "suggestions": ["alternative word or expression suggestions"]
        }}
        """,
        expected_output="A JSON response with conversation, corrections, and suggestions.",
        agent=fluent_ai
    )
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'No message provided'}), 400

        user_input = data['message']

        crew = Crew(
            agents=[fluent_ai],
            tasks=[create_conversation_task(user_input)],
            process=Process.sequential
        )

        response = crew.kickoff()

     
        if isinstance(response, str):
            clean_response = response.split("```json")[-1].split("```")[0].strip()
            try:    
                response_data = json.loads(clean_response)
            except json.JSONDecodeError:
                return jsonify({'status': 'error', 'message': 'Failed to parse response JSON.'}), 500
        elif isinstance(response, dict):
            response_data = response 
            return jsonify({'status': 'error', 'message': 'Unexpected response format.'}), 500

        return jsonify({'status': 'success', 'data': response_data})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'ok',
        'message': 'FluentAI is running'
    })

if __name__ == '__main__':
    app.run()