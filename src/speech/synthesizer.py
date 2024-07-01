import tensorflow as tf
from tensorflow_tts.inference import AutoProcessor, TFAutoModel
import soundfile as sf

class SpeechSynthesizer:
    def __init__(self):
        self.processor = AutoProcessor.from_pretrained("tensorspeech/tts-tacotron2-ljspeech-en")
        self.tacotron2 = TFAutoModel.from_pretrained("tensorspeech/tts-tacotron2-ljspeech-en")
        self.melgan = TFAutoModel.from_pretrained("tensorspeech/tts-mb_melgan-ljspeech-en")

    def synthesize_speech(self, text, output_path='output.wav'):
        try:
            print(f"Synthesizing speech for: '{text}'")

            # Преобразование текста в последовательность токенов
            input_ids = self.processor.text_to_sequence(text)

            # Инференс модели Tacotron2 для получения мел-спектрограммы
            print("Running Tacotron2 inference...")
            mel_outputs, mel_outputs_postnet, _, _ = self.tacotron2.inference(
                tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
                tf.convert_to_tensor([len(input_ids)], tf.int32),
                tf.convert_to_tensor([0], dtype=tf.int32)
            )

            # Инференс модели MelGAN для генерации аудио из мел-спектрограммы
            print("Running MelGAN inference...")
            audio = self.melgan.inference(mel_outputs)[0, :, 0]

            # Сохранение аудиофайла
            print(f"Saving synthesized speech to: {output_path}")
            sf.write(output_path, audio, 22050, format='WAV')

            print("Speech synthesis completed successfully.")
            return output_path

        except Exception as e:
            print(f"Error during speech synthesis: {e}")

# Пример использования класса SpeechSynthesizer
if __name__ == "__main__":
    synthesizer = SpeechSynthesizer()
    text_to_synthesize = "Hello, how are you today?"
    output_file = "output.wav"
    synthesizer.synthesize_speech(text_to_synthesize, output_file)
