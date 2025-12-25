import speech_recognition as sr

class SpeechEngine:
    def __init__(self, language="en-US"):
        self.recognizer = sr.Recognizer()
        self.language = language

    def listen(self):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)
                text = self.recognizer.recognize_google(audio, language=self.language)
                return text
        except sr.UnknownValueError:
            return "‼️Sorry, I didn't catch that."
        except Exception as e:
            return f"‼️Voice Error: {str(e)}"

   