import pyttsx3
import wikipedia
import webbrowser
import datetime
import speech_recognition as sr
import smtplib
import os


engine = pyttsx3.init('sapi5') #for using the inbuilt voice
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def takeCommand():
    # takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising..")
        query = r.recognize_google(audio)
        print("User said: ", query)    

    except Exception as e:
        print(e)


        print("SAY THAT AGAIN PLEASE..")
        return "None"   
        
    return query   

def sendEmail(to, content):
    server = smtplib.SMTP('64.233.184.108') #587 is the port
    server.ehlo()
    server.starttls()
    server.login('aayushi100199@gmail.com', 'enter_password')
    server.sendmail('aayushi100199@gmail.com', to, content)
    server.close()




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good AFternoon")

    else:
        speak("Good Evening")

    speak("I'm Zira here, Mam,  How may I help you")                

if __name__ == "__main__":
    wishMe()  
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query   :
            speak('Opening in Youtube...')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in  query:
            webbrowser.open("stackoverflow.com")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to aayushi' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "username@gmail.com" 
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry,email can't be sent")       

        elif 'open teams' in query:
            speak("opening teams app.....") 
            os.startfile("C:\\Users\\admin\\AppData\\Local\\Microsoft\\Teams")     

        elif 'quit' in query:
            speak("signing off, Anneyeong")
            break
           

                


