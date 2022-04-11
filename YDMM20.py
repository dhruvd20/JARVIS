import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import smtplib
import webbrowser
import pyautogui
import os
import math

list_fine_or_not = ()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200) # we can use 170 or 150(when jarvis is asked to read a book)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon")   

    else:
        speak("Good Evening!")
        print("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")  

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query



def sendEmail(to, content):
    user_email = ("downifty@gmail.com")  #value = will et inserted in places where it is called
    user_password = ("1234")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(user_email, user_password)
    server.sendmail(user_email, to, content)
    server.close()

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
           speak('Searching Wikipedia...')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           print(results)
           speak(results)

        elif 'youtube search' in query:
           speak('this is what I have found for your search.')
           query = query.replace("jarvis","")
           query = query.replace("youtube search","")
           web = 'https:/www.youtube.com/results?search_query=' + query
           webbrowser.open(web)
      


        elif 'Google search' in query or 'google' in query:
            speak("this is what i have found according to google")
            query = query.replace("Google Search","")
            query = query.replace("Jarvis","")
            query = query.replace("google","")
            google_open = 'https://www.google.com/search?q='+query
            webbrowser.open(google_open)

        elif 'Play in spotify' in query or 'spotify' in query:
            speak("This is the most accurate search according to you needs")
            query = query.replace("Play in spotify","")
            query = query.replace("spotify","")
            spotify_play = "https://open.spotify.com/search/"+query
            webbrowser.open(spotify_play)

        elif 'open sent mail' in query or 'sent mail' in query:
            speak("DOing that right now")
            query = query.replace("Open sent mail","")
            query = query.replace("sent mail","")
            open_sent = "https://mail.google.com/mail/u/0/#sent"
            webbrowser.open(open_sent)

        elif 'open my mail box' in query or 'Open mail' in query:
            speak("Doing that right now")
            query = query.replace("jarivs","")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'open whatsapp' in query or 'whatsapp' in query:
            speak("Doing that right now")
            webbrowser.open("https://web.whatsapp.com/")

        elif 'hello Jarvis' in query or 'hi' in query or 'hello' in query or 'hai' in query:
            speak("Hi sir, how are you")
            fine_or_not = takeCommand()
            if 'fine' in fine_or_not or 'I am fine' in fine_or_not:
               speak("thats good")
               continue
            else:
                speak("Hope you have a better day")
                continue

        elif 'email to ' in query or 'I want to email someone' in query:
            try:
                speak("What should I say?")
                content = input("what should it say: ")
                to = input("who should it go to: ")    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")   

        elif 'good bye' in query or 'goodbye' in query or 'bye' in query:
            print("Goodbye sir")
            speak("Goodbye sir")
            break


        elif 'find the ' in query:
            speak("did not quite get that")

        elif 'Find the square root of ' in query or 'square root of ' in query:
            query = query.replace("Find the square root of ",'')
            query = query.replace('square root of ','')
            query = float(query)
            root =  math.sqrt(query)
            print(root)

        elif 'find the factorial of' in query or 'factorial of' in query:
            query = query.replace("Find the factorial of","")
            query = query.replace("factorial of","")
            query = query.replace("factorial","")
            fact_num = int(query)
            fact = math.factorial(fact_num)
            speak(fact)

        else:
            speak("I did not quite get that")
