import speech_recognition as sr

class AudioRecorder:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def record_audio(self):
        try:
            with sr.Microphone() as source:
                print("Speak something:")
                audio = self.recognizer.listen(source)
            return audio
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occurred")

# Пример использования класса AudioRecorder
if __name__ == "__main__":
    recorder = AudioRecorder()
    audio_data = recorder.record_audio()
    if audio_data:
        print("Audio recorded successfully!")
