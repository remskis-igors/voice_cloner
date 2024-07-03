import logging
import json
import pyaudio
import wave
from pathlib import Path

class Recorder:
    def __init__(self, config_dir):
        self.config_dir = config_dir
        self.load_configuration()

    def load_configuration(self):
        # Load recorder configuration
        recorder_config_path = Path(self.config_dir) / "recorder_config.json"
        with open(recorder_config_path, 'r') as f:
            recorder_config = json.load(f)

        self.duration = recorder_config.get('duration', 5)
        self.sr = recorder_config.get('sample_rate', 16000)
        self.channels = recorder_config.get('channels', 1)
        self.chunk = recorder_config.get('chunk', 1024)
        self.format = recorder_config.get('format', pyaudio.paInt16)

        logging.info("Recorder configuration loaded")

    def record_audio(self, output_path):
        p = pyaudio.PyAudio()
        stream = p.open(format=self.format,
                        channels=self.channels,
                        rate=self.sr,
                        input=True,
                        frames_per_buffer=self.chunk)

        frames = []

        logging.info("Recording...")
        for _ in range(0, int(self.sr / self.chunk * self.duration)):
            data = stream.read(self.chunk)
            frames.append(data)
        logging.info("Finished recording.")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(output_path, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(p.get_sample_size(self.format))
        wf.setframerate(self.sr)
        wf.writeframes(b''.join(frames))
        wf.close()

        logging.info(f"Audio saved to {output_path}")
