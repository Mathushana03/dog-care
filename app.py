#app.py

import gradio as gr
import sys
import os
import logging
from pathlib import Path
import torch
import warnings
from transformers import logging as transformers_logging

# Torch workaround
torch.classes.__path__ = []

# Suppress warnings
warnings.filterwarnings("ignore")
transformers_logging.set_verbosity_error()
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set project root
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# Import chatbot logic
from src.chatbot.chatbot import handle_input

logger.info("Starting Dog Care Chatbot app with Gradio")

def chat_fn(message, history):
    response = handle_input(message)
    return response

# Launch Gradio Chat Interface
demo = gr.ChatInterface(
    fn=chat_fn,
    title="🐶 Dog Care Chatbot",
    description="Ask me anything about dog diseases or symptoms",
    submit_btn="Send"
)

if __name__ == "__main__":
    demo.launch()
