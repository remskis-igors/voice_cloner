import logging
import json
import torchaudio
from pathlib import Path
from resemblyzer import VoiceEncoder, preprocess_wav

class Recognizer:
    def __init__(self, config_dir):
        self.config_dir = config_dir
        self.load_configuration()

        # Initialize voice encoder
        self.encoder = VoiceEncoder()

    def load_configuration(self):
        # Load recognizer configuration
        recognizer_config_path = Path(self.config_dir) / "recognizer_config.json"
        with open(recognizer_config_path, 'r') as f:
            recognizer_config = json.load(f)

        self.sample_rate = recognizer_config.get('sample_rate', 16000)
        self.max_length = recognizer_config.get('max_length', 10)
        self.batch_size = recognizer_config.get('batch_size', 1)

        logging.info("Recognizer configuration loaded")

    def process_audio(self, file_path):
        wav, sr = torchaudio.load(file_path)
        wav = wav.numpy().squeeze()
        wav = preprocess_wav(wav, source_sr=sr)
        return wav

    def get_speaker_embedding(self, wav):
        return self.encoder.embed_utterance(wav)
