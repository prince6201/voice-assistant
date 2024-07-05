import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voice')
#print(voice[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am spandy Mam, Please tell me how may I help you")

def takecommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()   
    with sr.Microphone()as source:
        print("Listening...")
        r.paush_threshold = 1
        audio = r.listen(source)

    try:
        print ("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"USer said: {query}\n")

    except Exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    return query

if __name__== "__main__":
    wishMe()

    while True:
        query = takecommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open youtube' in query:
           webbrowser.open("google.com")


        elif 'play music' in query:
            music_dir = "c:\\Users\\naren\\Music\\playlists"
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir,song[0]))


        elif 'the time'in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Man, the time is {strTime}")

        elif 'open code' in query:
            codepath = "c:\\Users\\naren\\AppData\\local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

                             



