import torchaudio
import numpy as np
from resemblyzer import VoiceEncoder, preprocess_wav
from scipy.io.wavfile import write
import pyttsx3
from pathlib import Path

# Инициализация голосового энкодера
encoder = VoiceEncoder()

# Путь к файлу input.wav
input_wav_path = Path("input.wav")

# Загрузите и предобработайте аудио файл
wav, sr = torchaudio.load(input_wav_path)
wav = wav.numpy().squeeze()
wav = preprocess_wav(wav, source_sr=sr)

# Создание голосового отпечатка (speaker embedding)
speaker_embedding = encoder.embed_utterance(wav)

# Текст для синтеза
text = "Hello, this is a test of voice cloning."

# Инициализация синтезатора речи
engine = pyttsx3.init()

# Настройка параметров синтезатора (можно подстроить для вашего случая)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Синтез текста в аудио
engine.save_to_file(text, "temp_output.wav")
engine.runAndWait()

# Проверка существования файла "temp_output.wav"
file_path = "temp_output.wav"
if Path(file_path).exists():
    print(f"File '{file_path}' exists.")
else:
    print(f"File '{file_path}' does not exist.")

# Загрузите синтезированный аудио файл
synth_wav, sr = torchaudio.load(file_path)
synth_wav = synth_wav.numpy().squeeze()

# Применение голосового отпечатка к синтезированному аудио (это демонстрационный шаг, обычно требуются сложные методы для переноса стиля речи)
# В реальных применениях потребуется более сложная модель для корректного переноса стиля
output_wav = synth_wav  # Здесь просто сохраняем синтезированное аудио без изменений

# Сохранение результата
output_wav_path = "output.wav"
write(output_wav_path, sr, output_wav.astype(np.float32))

print(f"Synthesized speech saved to {output_wav_path}")
