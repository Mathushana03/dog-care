# run.py

import os
import sys
import subprocess
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Get the project root directory
project_root = Path(__file__).parent

def main():
    logger.info("Starting dog disease info Chatbot")
    
    # Check if model is downloaded
    model_dir = project_root / "models" / "llama-3.2-1b-instruct"
    if not model_dir.exists() or not any(model_dir.iterdir()):
        logger.warning("Model not found. Please download it first.")
        logger.info("You can download the model with: python scripts/download_model.py")
        sys.exit(1)
    
    # Add project root to Python path
    sys.path.append(str(project_root))
    
    # Run the Streamlit app
    logger.info("Launching gradio app")
    subprocess.run(["python", "app.py"])

if __name__ == "__main__":
    main()