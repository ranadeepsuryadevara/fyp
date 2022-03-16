import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import socket
import subprocess
#import selenium
from PIL import Image #pip install pillow
from playsound import playsound
engine = pyttsx3.init('sapi5')
#engine1 = pyttsx3.init('sapi5')
#voices = engine1.getProperty('voices')
#engine1.setProperty('voice',voices[0].id)
voices = engine.getProperty('voices')


print(voices[1].id)


engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def IP():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("Ok sir . Here's your Internet Protocol Address")    
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)    
    speak(IPAddr)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")
        speak("Have a great day Tell me how can i help you")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!") 

    elif hour in range(5,6):
        speak("Wake up sir. it's time for your workout")  

    else:
        speak("Good Evening sir. Hope you had a wonderful day.")  
	
           

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        if 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak('Opening google')
            webbrowser.open("google.com")
        elif 'intro' in query:
            speak("I am Jarvis . An artificial intelligence program developed by Ranadeep Suryadevara to asist him in his daily tasks . Now  I am in a development stage . In the near future I would be useful to automate his needs , install an uninstall programs, do complex taskts etc...")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'what are you doing'  in query:
            speak("Waiting for your commands sir") 
        elif 'open command prompt' in query:
            speak('Opening command prompt sir')
            codePath = "%windir%\system32\cmd.exe"
            os.startfile(codePath)
        elif 'close terminal' in query:
            speak('closing command prompt sir')
            os.system("TASKKILL /F /IM cmd.exe")
        elif 'jarvis'  in query:
            speak("Yes sir")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"sir, the time is {strTime}")
        elif 'status' in query:
            speak('All systems at one hundred percent . standby')
        elif 'open chrome' in query:
            speak("Opening google chrome")
            codePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)
        elif 'close google chrome' in query:
            speak("Closing google chrome ")
            os.system("TASKKILL /F /IM chrome.exe")
        elif 'i need some info' in query:
            speak("What's the info that you need sir?")
            content = takeCommand()
            urL = content
            webbrowser.open_new_tab(urL)
        elif 'open edge' in query:
            speak("Opening your default browser")
            codePath="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            os.startfile(codePath)
        elif 'close edge' in query:
            speak("Closing Microsoft edge ")
            codePath="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            os.system("TASKKILL /F /IM msedge.exe")
        #elif hour == 18:

        elif 'start linux' in query:
            speak("Opening virtual box")
            codePath="C:\Program Files\Oracle\VirtualBox\VirtualBox.exe"
            os.startfile(codePath)
        elif 'stop linux machine' in query:
            speak("Closing virtualbox")
            os.system("TASKKILL /F /IM VirtualBox.exe")
        elif 'my ip address' in query:
            IP()
        elif "let's pack it up" in query:
            speak("Ok sir , call me if you need anything . good bye")
            os.system("TASKKILL /F /IM Code.exe")

        elif 'reboot the system' in query:
            speak('OK sir rebooting the system')
            os.system("shutdown -r")
        elif 'kill the system' in query:
            speak("OK Boss turning off the computer and going to hibernation")
            os.system("shutdown -s")
        elif 'start virtual machines' in query:
            speak("Starting virtual machines")
            codePath="C:\Program Files\Oracle\VirtualBox\VirtualBox.exe"
            os.startfile(codePath)

        
