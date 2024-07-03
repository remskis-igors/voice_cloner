import logging
import json
from pathlib import Path
from TTS.utils.synthesizer import Synthesizer as TTS_Synthesizer
from TTS.utils.manage import ModelManager

class Synthesizer:
    def __init__(self, config_dir):
        self.config_dir = config_dir
        self.load_configuration()

        # Initialize the TTS synthesizer
        self.synthesizer = TTS_Synthesizer(
            model_path=self.model_path,
            config=self.config
        )
        logging.info("TTS Synthesizer initialized")

    def load_configuration(self):
        # Load TTS model configuration
        model_config_path = Path(self.config_dir) / "model_config.json"
        with open(model_config_path, 'r') as f:
            model_config = json.load(f)

        self.model_path = model_config.get('model_path', None)
        self.config = model_config.get('config', {})

        if not self.model_path:
            raise ValueError("Model path is not specified in the configuration")

        logging.info("Model configuration loaded")

    def synthesize(self, text, speaker_embedding, output_path):
        # Synthesize text into speech using the TTS synthesizer
        logging.info(f"Synthesizing text: {text}")
        wav = self.synthesizer.synthesize(text, speaker_embedding)

        # Save synthesized speech to the output path
        logging.info(f"Saving synthesized speech to: {output_path}")
        self.synthesizer.save_wav(wav, output_path)

        # Print message indicating where the synthesized speech is saved
        logging.info(f"Synthesized speech saved to {output_path}")
