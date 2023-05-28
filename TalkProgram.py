import pyttsx3
import datetime
import speech_recognition as sr
from googletrans import Translator
engine = pyttsx3.init()
def get_command(query):
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 0.7
        audio = rec.listen(source)
        try:
            print("Recognizing...")
            query = rec.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return "None"
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return "None"

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query
def fun_talk(audio):
    engine.say(audio)
    engine.runAndWait()
def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        fun_talk("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        fun_talk("Good Afternoon Sir")
    else:
        fun_talk("Good Evening Sir")
        
    fun_talk('Test')
