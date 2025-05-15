# llama_inference.py

import os
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.messages import HumanMessage, SystemMessage

PROJECT_ROOT = Path(__file__).parent.parent.parent
MODEL_DIR = os.path.join(PROJECT_ROOT, "models", "llama-3.2-1b-instruct")

if not os.path.exists(MODEL_DIR):
    print(f"Model not found in {MODEL_DIR}. Please run scripts/download_model.py first.")
    raise FileNotFoundError(f"Model not found in {MODEL_DIR}")
else:
    model = AutoModelForCausalLM.from_pretrained(MODEL_DIR)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    return_full_text=False,               # only give the generated part
    max_new_tokens=150,                   # a bit more room for longer answers
    do_sample=True,                       # enable sampling (avoids warnings)
    temperature=0.6,                      # control randomness
    top_p=0.9,                            # nucleus sampling
    num_beams=1,                          # no beam search
    early_stopping=False,                 # avoid warning with num_beams=1
    eos_token_id=tokenizer.eos_token_id,  # ensure model knows when to stop
    pad_token_id=tokenizer.eos_token_id,  # use eos as pad to avoid warnings
    device_map="auto"                     # use GPU if available
)

messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful dog care assistant. "
            "Always respond in complete sentences and do not end mid-sentence."
        )
    }
]

def generate_llama_response(user_input: str) -> str:
    """
    Append the user_input to the history, generate a fully-formed reply, 
    and then append the assistant's reply back into the history.
    """
    # 3) Add the new user turn to the history
    messages.append({"role": "user", "content": user_input})
    
    # 4) Render the chat history into a single string
    input_text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    
    outputs = pipe(input_text)
    raw = outputs[0]["generated_text"]

    assistant_response = raw.strip()
    messages.append({"role": "assistant", "content": assistant_response})
    
    return assistant_response
