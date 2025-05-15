# chatbot.py

from src.chatbot.static_responses import STATIC_RESPONSES
from src.data.database import query_disease
from src.inference.llama_inference import generate_llama_response

def detect_intent(user_input: str) -> str:
    user_input_lower = user_input.lower()
    if any(word in user_input_lower for word in ["disease", "treatment", "prevent"]):
        return "disease_query"
    elif user_input_lower in STATIC_RESPONSES:
        return "static"
    return "llama"

def handle_input(user_input: str) -> str:
    intent = detect_intent(user_input)

    if intent == "static":
        return STATIC_RESPONSES[user_input.lower()]

    elif intent == "disease_query":
        for word in user_input.split():
            result = query_disease(word.capitalize())
            if result:
                return (
                    f"Disease: {result['disease']}\n\n"
                    f"Symptoms:\n- " + "\n- ".join(result["symptoms"]) + "\n\n"
                    f"Treatment:\n- " + "\n- ".join(result["treatments"]) + "\n\n"
                    f"Prevention:\n- " + "\n- ".join(result["preventions"])
                )
        return "I couldn't find a disease with that name."

    else:
        return "This is not included in the current domain. Please ask about other diseases related to dogs."