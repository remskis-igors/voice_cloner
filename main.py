import json
import logging
from pathlib import Path
from src.speech.synthesizer import Synthesizer

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def load_general_config():
    # Load general configuration
    config_dir = Path(__file__).resolve().parent / "resources"
    config_path = config_dir / "general_config.json"

    with open(config_path, 'r') as f:
        general_config = json.load(f)

    output_directory = general_config['output_directory']
    logging_level = general_config['logging_level']

    logging.basicConfig(level=logging_level, format='%(asctime)s - %(levelname)s - %(message)s')

    return output_directory

def main():
    output_directory = load_general_config()

    # Initialize the Synthesizer
    config_dir = Path(__file__).resolve().parent / "resources"
    synthesizer = Synthesizer(config_dir)

    # Example usage of the Synthesizer
    sample_text = "Hello, this is a test."
    sample_embedding = None  # Replace with actual speaker embedding if required
    output_path = str(output_directory / "output.wav")

    synthesizer.synthesize(sample_text, sample_embedding, output_path)

if __name__ == "__main__":
    main()
