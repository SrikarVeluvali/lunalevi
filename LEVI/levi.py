# LEVI (Language Enabled Virtual Assistant) by Srikar Veluvali
# A virtual Assistant which makes Navigation easy.

# Modules Imported
# Microsoft Text to Speech
import pyttsx3
# For date and Time
import datetime
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
engine.setProperty('voice',voices[0].id)

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
        speak("Good Morning")
    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon")
    else:
        print("Good Evening!")
        speak("Good Evening")
    print("I am LEVI (v1.5). Language Enabled Virtual Intelligence. How may I help you today?")
    speak("I am LEVI . Language Enabled Virtual Intelligence. How may I help you today?")

# The Main Function
if __name__=="__main__":
    # Make LUNA Wish you.
    wishMe()
    # Start the conversation with LUNA
    while True:
        # Start Speaking.
        query = input("Enter your query : ").lower()
        # Search Wikipedia for topics. Returns summary of the topic in 5 lines.
        if 'wikipedia' in query:
            speak("Enter the number of sentences : ")
            try:
                s=int(input("Enter the number of sentences : "))
            except:
                print("Invalid Input! Please enter again.")
                speak("Invalid Input! Please enter again.")
                s=int(input("Enter the number of sentences : "))
            print('Searching Wikipedia...')
            speak('Searching Wikipedia...')

            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=s)

            print(f"According to wikipedia,{results}")
            speak(f"According to wikipedia,{results}")
            

        # Opens LEVI AI Documentation
        elif 'levi help' in query:
            print("Opening LEVI Documentation...")
            speak("Opening LEVI Documentation...")
            os.startfile("LEVI AI DOCUMENTATION.txt")
        
        # Open any site
        elif 'open site' in query:
            print("Enter the address of the site : ",end="")
            speak("Enter the address of the site")
            site=input()
            print(f"Opening {site}...")
            speak(f"Opening {site}...")
            webbrowser.open(f'{site}')

        # Opens YouTube in your default browser
        elif 'open youtube' in query:
            print("Opening YouTube...")
            speak("Opening YouTube...")
            webbrowser.open('youtube.com')

        # Opens Google in your default browser
        elif 'open google' in query:
            print("Opening Google...")
            speak("Opening Google...")
            if 'search' in query:
                webbrowser.open("https://www.google.com/search?q={}".format(query.replace("open google and search","")))
            else:
                webbrowser.open('google.com')

        # Opens ChatGPT in your default browser
        elif 'open chat gpt' in query:
            print("Opening ChatGPT...")
            speak("Opening ChatGPT...")
            webbrowser.open('chat.openai.com')
        

        # Opens BardAI in your default browser
        elif 'open bard' in query:
            print("Opening Google Bard...")
            speak("Opening Google Bard...")
            webbrowser.open('bard.google.com')

        # Opens LeetCode
        elif 'open leetcode' in query:
            print("Opening Leet Code...")
            speak("Opening Leet Code")
            webbrowser.open("https://leetcode.com/problemset/all/?difficulty=EASY&page=1")

        # Plays music from Spotify.
        elif 'play music' in query:
            track_results = sp.search(q=query.replace("play music",""), type='track')
            track_uri = track_results['tracks']['items'][0]['uri']
            webbrowser.open(track_uri)

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
                    dte+=" Sunday"
            print(f"The day and date today is : {dte}")
            speak(f"The day and date today is : {dte}")

        # Shows the current time.
        elif 'time now' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time now is {strTime}")
            speak(f"The time now is {strTime}")

        # Movie Review
        elif 'movie review' in query:
            print("Enter the title of the movie/series: ",end="")
            speak("Enter the title of the movie or series: ")
            u_i=input()
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
        elif 'ask levi' in query:
            ask = query.replace('ask levi','')
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

        # Displays the weather in given city.
        elif 'weather today' in query:
            print("Enter the city you want to check weather in : ",end="")
            speak("Enter the city you want to check weather in")
            city=input()
            weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={w_api_key}")

            if weather_data.json()['cod'] == '404':
                print("No City Found")
                speak("No City Found")
            else:
                weather = weather_data.json()['weather'][0]['main']
                temp = round(weather_data.json()['main']['temp'])
                celsius = (temp - 32)/1.8
                print(f"The weather in {city.title()} is: {weather}")
                print(f"The temperature in {city.title()} is: {round(celsius,2)}ºC")
                speak(f"The weather in {city.title()} is: {weather}")
                speak(f"The temperature in {city.title()} is: {round(celsius,2)}ºCelcius")

        # Opens VS Code
        elif 'open vs code' in query:
            print("Opening VS Code...")
            speak("Opening VS Code")
            os.startfile("C:\\Users\\srika\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        # Opens Games Folder
        elif 'open games' in query:
            print("Opening Games...")
            speak("Opening Games")
            os.startfile("C:\\Users\\srika\\OneDrive\\Desktop\\Srikar's Folders\\Games")

        # Opens Command Prompt
        elif 'open command prompt' in query:
            print("Opening Command Prompt")
            speak("Opening Command Prompt")
            os.startfile('cmd.exe')
        
        # Opens Calculator
        elif 'open calculator' in query:
            print("Opening Calculator")
            speak("Opening Calculator")
            os.startfile('calc.exe')
        
        # Opens Notepad
        elif 'open notepad' in query:
            print("Opening Notepad")
            speak("Opening Notepad")
            os.startfile('notepad.exe')

        # Remember Function
        elif "remember that" in query:
            rememberMessage = query.replace("remember that","").replace("luna","")
            print("You told me to remember that"+rememberMessage)
            speak("You told me to remember that"+rememberMessage)
            with open("Remember.txt","w") as remember:
                remember.write(rememberMessage)
        elif "what do you remember" in query:
            try:
                remember = open("Remember.txt","r")
                remembered=remember.read()
            except:
                remember=open("Remember.txt","x")
                remembered=""
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

        # Exits the LUNA AI
        elif 'exit' in query or 'quit' in query:
            print("Thanks for using LEVI! LEVI hopes to see you again.")
            speak("Thanks for using LEVI! LEVI hopes to see you again.")
            break

        # If Commands are not recognised.
        else:
            print("Sorry. Levi can't recognise this command.")
            speak("Sorry. Levi can't recognise this command.")
            time.sleep(1)

        os.system("cls")