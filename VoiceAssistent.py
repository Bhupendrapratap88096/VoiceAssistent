import os
import webbrowser
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Initialize the engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query

def open_application(query):
    if 'open' in query:
        app_name = query.split('open')[-1].strip()
        if os.path.exists(app_name):
            os.startfile(app_name)
        else:
            speak(f"Sorry, I can't find {app_name}")

def search_on_web(query):
    if 'search' in query:
        search_term = query.split('search')[-1].strip()
        url = f"https://www.google.com/search?q={search_term}"
        webbrowser.open(url)

def main():
    while True:
        query = listen().lower()
        if 'exit' in query:
            speak("Goodbye!")
            break
        elif 'open' in query:
            open_application(query)
        elif 'search' in query:
            search_on_web(query)
        else:
            speak("Sorry, I can't understand that command.")

if __name__ == "__main__":
    main()
