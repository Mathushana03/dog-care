# Dog care Chatbot

A simple dog care chatbot that combines rule-based responses, database queries, and AI-powered responses using the Llama 3.2 1B Instruct model.

## 🌟 Features

- Simple chat interface built with Streamlit
- Database integration for patient records, medications, and appointments
- Llama 3.2 1B Instruct model for AI-powered responses
- Intent-based routing for different types of queries
- Modular and maintainable code structure

## 📋 Prerequisites

- Python 3.8 or higher
- Hugging Face account with access to the Llama 3.2 models
- Hugging Face access token (for downloading the model)

## 🔧 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/AbinayanRatna/dogcare_chatbot.git
   cd dogcare_chatbot
   ```

2. Create a virtual environment (recommended):

   ```bash
   # Using conda
   conda create -n dogcare_chatbot python=3.10
   conda activate dogcare_chatbot

   # Or using venv
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up Hugging Face authentication:
   ```bash
   # On Windows
   set HF_TOKEN=your_token_here

   # On macOS/Linux
   export HF_TOKEN=your_token_here
   ```

5. Download the Llama 3.2 1B model:
   ```bash
   python scripts/download_model.py
   ```

## 🚀 Running the Application

Start the application with:

```bash
python run.py
```

Or directly with Streamlit:

```bash
streamlit run app.py
```

Then open your browser and navigate to the URL shown in the terminal.



## 🤖 How It Works

The chatbot works through the following components:

1. **Static Responses**: Simple rule-based responses for common phrases.
2. **Database Queries**: SQLite database integration for querying diseases, treatments, symptoms and prevention methods.
3. **AI Inference**: Llama 3.2 1B model for handling more complex or nuanced queries.
4. **Intent Detection**: Routes user queries to the appropriate handling system based on detected intent.

## 🧠 Intent Detection Logic

The chatbot uses a simple keyword-based approach to detect user intent:

- **Disease queries**: Triggered by keywords like "disease", "treatment", "prevent".
- **Static responses**: Matched against a predefined dictionary of common phrases.
- **Others**: Will show a custom message like "Not in this domain".

## 🔍 Query Examples

- "Tell about the disease rabies?" - Medication query
- "Thank you" - Static response
- "Explain about the apple ipad?" - Will show a custom message like "Not in this domain".

## 🔄 Customization

### Adding Static Responses

Edit `src/chatbot/static_responses.py` to add more static responses:

```python
STATIC_RESPONSES = {
    "thank you": "You're welcome!",
    "thanks": "You're welcome!",
    "good morning": "Good morning!",
    "good afternoon": "Good afternoon!",
    "good evening": "Good evening!",
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! How can I help?",
    "hey": "Hey there! What can I do for you?",
    "how are you": "I'm just a bot, but I'm here to help you!",
    "what's up": "All good! How can I assist you today?",
    "who are you": "I'm your Dog Care Assistant here to help with any dog-related questions!",
    "bye": "Goodbye! Take care and give your dog a treat!",
    "see you": "See you later!",
    "goodbye": "Goodbye! I'm here whenever you need help.",
    "help": "Sure! Ask me anything about dog diseases, symptoms, or care.",
    "can you help me": "Absolutely! Let me know what you need help with.",
    "thank you very much": "You're most welcome!",
    "ok": "Alright!",
    "okay": "Got it!",
}
```

### Modifying the Database

You can modify the database schema and seed data in `src/data/database.py`.

## 🛠️ Troubleshooting

### Model Download Issues

If you encounter issues downloading the model:

1. Ensure you have a valid Hugging Face token with access to the Llama models
2. Check your internet connection
3. Verify you have sufficient disk space (model is ~2GB)

### Runtime Errors

- **ModuleNotFoundError**: Ensure you've installed all dependencies and are running from the project root
- **No module named 'src'**: Make sure you're running the application from the project root directory
