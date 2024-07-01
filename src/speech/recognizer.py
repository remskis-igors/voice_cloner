from TTS.api import TTS
import soundfile as sf

class SpeechSynthesizer:
    def __init__(self):
        self.tts = TTS(model_name="tts_models/ru/v3_1", progress_bar=True)

    def synthesize_speech(self, text, output_filename):
        try:
            print(f"Synthesizing speech for '{text}'...")
            wav = self.tts.tts(text)
            print("Speech synthesized successfully.")
            sf.write(output_filename, wav, self.tts.synthesizer.output_sample_rate)
            print(f"Speech saved to {output_filename}")
        except Exception as e:
            print(f"Error occurred during speech synthesis: {e}")

