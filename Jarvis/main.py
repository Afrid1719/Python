import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as browser


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Adjusting from background noise...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        print('Listening... ')
        audio = r.listen(source)

    while True:
        try:
            print('Recognizing... ')
            query = r.recognize_google(audio, language='en-in')
            print(f"Your command: {query}")
            print(query.find('Jarvis go to sleep'))
            if query.find('Jarvis go to sleep') != -1:
                break
            
            exec_command(query)
        except Exception as e:
            print(e)
            speak("Pardon, can you please repeat")
            print("Pardon, can you please repeat")

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

def exec_command(query):
    if query.find('open the browser') != -1:
        browser.open('https://www.google.com')

if __name__ == '__main__':
    wishMe()
    q = takeCommand()