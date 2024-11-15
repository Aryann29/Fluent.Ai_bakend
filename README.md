# FluentAI - Interactive English Tutor

FluentAI is an AI-powered English language tutor that helps users improve their English through natural conversations. It provides real-time grammar corrections, suggests alternative expressions, and helps enhance overall language fluency.

## Features

- Interactive conversation practice
- Real-time grammar corrections
- Alternative expression suggestions
- Vocabulary enhancement
- Natural language processing for accurate feedback

## Prerequisites

- Python 3.8 or higher
- Google API key for Gemini

## Installation

1. **Clone the Repository**
```bash
git clone https://github.com/Aryann29/fluentAI_backend.git
cd fluentAI_backend
```

2. **Set Up Virtual Environment**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Environment Variables**
- Rename `.env.addkey` to `.env`
- Add your Google API key to the `.env` file:
```plaintext
GOOGLE_API_KEY=your_gemini_api_key_here
```

## Usage

1. **Start the Application**
```bash
python fluent_ai.py
```

2. **Begin Conversation**
Once running, you can start chatting with FluentAI. The application will provide corrections and suggestions to help improve your English.

### Example Interaction:
```
User: "i am very happy for meet you today"

FluentAI: {
    "response": "I'm very happy to meet you today as well! How are you doing?",
    "corrections": "I am very happy to meet you today (not 'for meet').",
    "suggestions": [
        "Instead of 'very happy', you could use 'delighted', 'pleased', or 'thrilled'."
    ]
}
```

To end the conversation, simply type `exit`.

## Contributing

Please feel free to submit a Pull Request.


This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please open an issue in the GitHub repository.
