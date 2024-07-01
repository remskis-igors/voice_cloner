import speech_recognition as sr

class AudioRecorder:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def record_audio(self, filename, duration=5):
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                print("Recording for {} seconds...".format(duration))
                audio = self.recognizer.listen(source, phrase_time_limit=duration)

            with open(filename, "wb") as f:
                f.write(audio.get_wav_data())
                print(f"Audio recorded and saved to {filename}")

        except sr.RequestError as e:
            print(f"Error during request: {e}")

        except sr.UnknownValueError:
            print("Unknown error occurred during audio recognition")


if __name__ == "__main__":
    recorder = AudioRecorder()
    output_file = "recorded_audio.wav"
    recorder.record_audio(output_file)
