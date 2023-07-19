# LUNA (Logical User-friendly Navigation Assistant) by Srikar Veluvali
# A virtual Assistant which makes Navigation easy.

# Modules Imported
# Microsoft Text to Speech
import pyttsx3
# For date and Time
import datetime
# For Speech Recognition
import speech_recognition as sr
# For wikipedia
import wikipedia
# For Web-browser functions
import webbrowser
# For Spotify API
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# For GPT-3 API
import openai
# For General Opening of files
import os
# For Sleep()
import time
# For weather API
import requests
# For SpeedTest
import speedtest
# For Movies
import imdb

# API Setups
# Microsoft Text To Speech API
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# Spotify Client for Music
client_credentials_manager = SpotifyClientCredentials(client_id='371d72b411c146f8b6f02a24a152cada', client_secret='8bb70d2587564f7b96a3ead85d000b55')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# OpenAI API for General Chat
openai.api_key = "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"

# Weather API for Weather
w_api_key = '30d4741c779ba94c470ca1f63045390a'

# Movies DataBase
moviesDB=imdb.IMDb()

# Functions
# Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish Function (At the begining of the application.)
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    else:
        print("Good Evening!")
        speak("Good Evening!")
    print("I am LUNA (v1.5). Logical User-friendly Navigation Assistant. How may I help you today?")
    speak("I am LUNA . Logical User-friendly Navigation Assistant. How may I help you today?")

#Recognise the command given through microphone using Microsoft Text to Speech
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1 # Pause time
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said : {query.title()}")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

# The Main Function
if __name__=="__main__":
    # Make LUNA Wish you.
    wishMe()
    # Start the conversation with LUNA
    while True:
        # Start Speaking.
        query = takeCommand().lower()
        # Search Wikipedia for topics. Returns summary of the topic in 5 lines.
        if 'wikipedia' in query:
            print('Searching Wikipedia...')
            speak('Searching Wikipedia...')

            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=5)

            print(f"According to wikipedia, {results}")
            speak(f"According to wikipedia, {results} ")

        # Opens YouTube in your default browser
        elif 'luna help' in query:
            print("Opening LUNA Documentation...")
            speak("Opening LUNA Documentation...")
            os.startfile("LUNA AI DOCUMENTATION.txt")
            time.sleep(5)

        # Opens YouTube in your default browser
        elif 'open youtube' in query:
            print("Opening YouTube...")
            speak("Opening YouTube...")
            webbrowser.open('youtube.com')
            time.sleep(5)

        # Opens Google in your default browser
        elif 'open google' in query:
            print("Opening Google...")
            speak("Opening Google...")
            if 'search' in query:
                webbrowser.open("https://www.google.com/search?q={}".format(query.replace("open google and search","")))
            else:
                webbrowser.open('google.com')
            time.sleep(5)

        # Opens ChatGPT in your default browser
        elif 'open chat gpt' in query:
            print("Opening ChatGPT...")
            speak("Opening ChatGPT...")
            webbrowser.open('chat.openai.com')
            time.sleep(5)

        # Opens BardAI in your default browser
        elif 'open bird' in query:
            print("Opening Google Bard...")
            speak("Opening Google Bard...")
            webbrowser.open('bard.google.com')
            time.sleep(5)

        # Opens LeetCode
        elif 'open leetcode' in query:
            print("Opening Leet Code...")
            speak("Opening Leet Code")
            webbrowser.open("https://leetcode.com/problemset/all/?difficulty=EASY&page=1")
            time.sleep(5)

        # Plays music from Spotify.
        elif 'play music' in query:
            track_results = sp.search(q=query.replace("play music",""), type='track')
            track_uri = track_results['tracks']['items'][0]['uri']
            webbrowser.open(track_uri)
            time.sleep(5)

        # Shows the current date.
        elif 'date today' in query or 'day today' in query:
            dte=str(datetime.date.today())
            match datetime.date.today().weekday():
                case 0:
                    dte="Monday " + dte
                case 1:
                    dte="Tuesday " + dte
                case 2:
                    dte="Wednesday " + dte
                case 3:
                    dte="Thursday " + dte
                case 4:
                    dte="Friday " + dte
                case 5:
                    dte="Saturday " + dte
                case 6:
                    dte="Sunday " + dte
            print(f"The day and date today is : {dte}")
            speak(f"The day and date today is : {dte}")


        # Shows the current time.
        elif 'time now' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time now is {strTime}")
            speak(f"The time now is {strTime}")
            time.sleep(5)

        # Movie Review
        elif 'movie review' in query:
            u_i=query.replace("movie review","")
            try:
                movies=moviesDB.search_movie(f"{u_i}")
                id=movies[0].getID()
                movie=moviesDB.get_movie(id)
                title=movie['title']
                year=movie['year']
                rating=movie['rating']
                results = wikipedia.summary(title,sentences=4)
                print(f"\n\nTitle : {title}\nYear : {year}\nIMDB Rating {rating}/10\n\nAbout : {results}")
                speak(f"Title : {title}\nYear : {year}\nIMDB Rating {rating} out of 10\nAbout : {results}")
            except:
                print("This movie / series isn't released yet. Or It wasn't found in IMDB Movie Database.")
                speak("This movie or series isn't released yet. Or It wasn't found in IMDB Movie Database.")

        # Uses OpenAI API to Chat with the bot using GPT-3
        elif 'ask luna' in query:
            ask = query.replace('ask luna','')
            if len(ask)!=0:
                response = openai.Completion.create(
                model="text-davinci-003",
                prompt=ask,
                temperature=0.9,
                max_tokens=250,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]
                )
                text = response['choices'][0]['text']
                print(text)
                speak(text)
                time.sleep(5)

        # Displays the weather in "Hyderabad" only.
        elif 'weather today' in query:
            weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q=Hyderabad&units=imperial&APPID={w_api_key}")

            if weather_data.json()['cod'] == '404':
                print("No City Found")
            else:
                weather = weather_data.json()['weather'][0]['main']
                temp = round(weather_data.json()['main']['temp'])
                celsius = (temp - 32)/1.8
                print(f"The weather in Hyderabad is: {weather}")
                print(f"The temperature in Hyderabad is: {round(celsius,2)}ºC")
                speak(f"The weather in Hyderabad is: {weather}")
                speak(f"The temperature in Hyderabad is: {round(celsius,2)}ºCelcius")
            time.sleep(5)

        # Opens VS Code
        elif 'open vs code' in query:
            print("Opening VS Code...")
            speak("Opening VS Code")
            os.startfile("C:\\Users\\srika\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            time.sleep(5)

        # Opens Games Folder
        elif 'open games' in query:
            print("Opening Games...")
            speak("Opening Games")
            os.startfile("C:\\Users\\srika\\OneDrive\\Desktop\\Srikar's Folders\\Games")
            time.sleep(5)

        # Opens Command Prompt
        elif 'open command prompt' in query:
            print("Opening Command Prompt")
            speak("Opening Command Prompt")
            os.startfile('cmd.exe')
            time.sleep(5)
        
        # Opens Calculator
        elif 'open calculator' in query:
            print("Opening Calculator")
            speak("Opening Calculator")
            os.startfile('calc.exe')
            time.sleep(5)
        
        # Opens Notepad
        elif 'open notepad' in query:
            print("Opening Notepad")
            speak("Opening Notepad")
            os.startfile('notepad.exe')
            time.sleep(5)

        # Remember Function
        elif "remember that" in query:
            rememberMessage = query.replace("remember that","").replace("luna","")
            print("You told me to remember that "+rememberMessage)
            speak("You told me to remember that "+rememberMessage)
            with open("Remember.txt","w") as remember:
                remember.write(rememberMessage)
        elif "what do you remember" in query:
            remember = open("Remember.txt","r")
            remembered=remember.read()
            if len(remembered)!=0:
                print(f"You told me to remember that {remembered}")
                speak(f"You told me to remember that {remembered}")
            else:
                print("I dont remember anything...")
                speak("I dont remember anything")
        elif "forget what you remember" in query:
            with open("Remember.txt", 'w') as file:
                file.truncate(0)
            print("I have successfully wiped my memory.")
            speak("I have successfully wiped my memory.")

        # Internet Speed
        elif "internet speed" in query:
            wifi  = speedtest.Speedtest()
            upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
            download_net = wifi.download()/1048576
            print("Internet Upload Speed is", round(upload_net,2))
            print("Internet Download speed is ",round(download_net,2))
            speak(f"Internet Upload speed is {int(upload_net)}")
            speak(f"Internet Download speed is {int(download_net)}")
            time.sleep(5)

        #Pauses LUNA AI
        elif 'pause' in query:
            print("PAUSED LUNA FOR 30 SECONDS.")
            speak("PAUSED LUNA FOR 30 SECONDS.")
            time.sleep(30)
            print("RESUMING LUNA.")
            speak("RESUMING LUNA.")
            time.sleep(2)

        # Exits the LUNA AI
        elif 'exit' in query or "quit" in query:
            print("Thanks for using LUNA! LUNA hopes to see you again.")
            speak("Thanks for using LUNA! LUNA hopes to see you again.")
            break

        # If Commands are not recognised.
        else:
            if "none" not in query:
                print("Sorry. Luna can't recognise this command.")
                speak("Sorry. Luna can't recognise this command.")
                time.sleep(1)
        os.system("cls")