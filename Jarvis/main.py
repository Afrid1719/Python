import pyttsx3
import datetime
import speech_recognition as sr


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening... ')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing... ')
        query = r.recognize_google(audio, language='en-in')
        print(f"Jarvis thinks you said: {query}")
        speak(query)
    except Exception as e:
        print(e)
        speak("Pardon, can you please repeat")
        print("Pardon, can you please repeat")
        return "None"
    return query

def speak(speech):
    engine.say(speech)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak('Good Morning Sir')
    elif hour >= 12 and hour < 16:
        speak('Good Afternoon Sir')
    elif hour >= 16 and hour < 20:
        speak('Good Evening Sir')
    else:
        speak('Good Night Sir')
        speak('I am always awake for you, sir')
        return
    
    speak('What can I do for you, sir?')

if __name__ == '__main__':
    wishMe()
    q = takeCommand()