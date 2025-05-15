# scripts/download_model.py

import os
import logging
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Get Hugging Face token from environment variable
HF_TOKEN = "your_hf_token_here"

# Get the path to the models directory relative to the project root
PROJECT_ROOT = Path(__file__).parent.parent
MODEL_DIR = os.path.join(PROJECT_ROOT, "models", "llama-3.2-1b-instruct")

def download_model():
    """Download the Llama 3.2 1B Instruct model for education chatbot."""
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR, exist_ok=True)
        
        logger.info("Downloading Llama 3.2 1B Instruct model and tokenizer...")
        logger.info("This may take several minutes depending on your internet speed.")
        
        # Check if HF_TOKEN is set
        if not(HF_TOKEN):
            logger.error("HF_TOKEN environment variable not set.")
            logger.error("Please set the environment variable with your Hugging Face access token:")
            logger.error("export HF_TOKEN=your_token_here")
            return
        
        try:
            # Download the model and tokenizer from Hugging Face
            model = AutoModelForCausalLM.from_pretrained(
                "meta-llama/Llama-3.2-1B-Instruct",
                token=HF_TOKEN
            )
            tokenizer = AutoTokenizer.from_pretrained(
                "meta-llama/Llama-3.2-1B-Instruct",
                token=HF_TOKEN
            )
            
            # Configure tokenizer to use eos_token as pad_token to avoid warnings
            if tokenizer.pad_token is None:
                tokenizer.pad_token = tokenizer.eos_token
            
            # Save them to the project directory
            model.save_pretrained(MODEL_DIR)
            tokenizer.save_pretrained(MODEL_DIR)
            
            logger.info(f"Model and tokenizer successfully downloaded to {MODEL_DIR}")
        except Exception as e:
            logger.error(f"Error downloading model: {str(e)}")
    else:
        logger.info(f"Model already exists at {MODEL_DIR}")
        logger.info("To re-download, delete the directory first.")

if __name__ == "__main__":
    download_model()
