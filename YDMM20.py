import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
#engine.setProperty('rate',100)

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
    speak("I am your digital assistant. Please tell me how may i help you?")    

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try: 
            statement=r.recognize_google(audio,language='en-in')
            print(f"User said: {statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

print("Loading your AI personal assistant YDMM-20")
speak("Loading your AI personal assistant YDMM-20")
print("My name is jarvis.")
speak("My name is jarvis.")

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        statement = takeCommand().lower()

        # Logic for executing tasks based on statement
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak('youtube is open now')
          
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak('Google chrome is open now')
          
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak('Google Mail is open now')
            
        elif 'open insta' in statement or 'open instagram' in statement or 'open igm' in statement:
            webbrowser.open_new_tab("https://www.instagram.com")
            speak('Instagram is open now.')

        elif 'open fb' in statement or 'open facebook' in statement:
            webbrowser.open_new_tab("https://www.facebook.com")
            speak('Facebook is open now...')

        elif 'play music' in statement or 'play some music' in statement:
            music_dir = 'C:\\Users\\Dhruv doshi\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
                
        elif 'stop playing music' in statement or 'close this application' in statement or 'close it' in statement or 'stop it' in statement:
            os.system('TASKKILL /F /IM Music.UI.exe')

        elif 'the time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f'Sir, the time is {strTime}')

        elif 'open vs code' in statement:
            codePath = "C:\\Users\\Dhruv doshi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "good bye" in statement or "ok bye" in statement or "bye" in statement:
                speak('Your personal assistant YDMM-20 is shutting down,Good bye')
                print('Your personal assistant YDMM-20 is shutting down,Good bye')
                break

        elif 'news' in statement or 'headlines' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
                   
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am YDMM-20, version 1 point O, your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,' 
                  'get top headline news from times of india and you can ask me computational questions and I can do many more things!')
            print('I am YDMM-20 version 1 point O, your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,' 
                  'get top headline news from times of india and you can ask me computational questions and I can do many more things!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Dhruv")
            print("I was built by Dhruv")
        


        


