"""
LEVI (Language Enabled Virtual Assistant) Documentation

Author: Srikar Veluvali

Description:
LEVI (Language Enabled Virtual Assistant) is a virtual assistant designed to provide various functionalities such as text-to-speech, information retrieval from Wikipedia, web browsing, music playback, weather forecasts, chat using the GPT-3 API, news headlines, system commands, and more.

Modules Used:
- pyttsx3: Microsoft Text-to-Speech engine.
- datetime: For date and time functions.
- wikipedia: For querying Wikipedia articles.
- webbrowser: For opening web pages in a browser.
- spotipy: For accessing the Spotify API for music playback.
- openai: For interacting with the GPT-3 API.
- os: For general file and system operations.
- time: For time-related functions.
- requests: For making HTTP requests.
- speedtest: For testing internet speed.
- imdb: For querying movie and series information.
- json: For working with JSON data.
- subprocess: For executing system commands.

API Setups:
- Microsoft Text To Speech API: Initializes the text-to-speech engine.
- Spotify Client: Sets up the Spotify API credentials for music playback.
- OpenAI API: Sets the API key for interacting with the GPT-3 API.
- Weather API: Configures the API key for weather forecasts.
- Movies Database: Sets up the IMDb API for querying movie and series information.
- News API: Configures the API key and base URL for news headlines.

Functions:
- speak(audio): Converts text to speech and speaks it.
- wishMe(): Greets the user based on the time of day.
- feedback(name, stars, feed): Collects and stores user feedback.
- detect_darkmode_in_windows(): Checks if dark mode is enabled on Windows.
- news(): Retrieves and displays top news headlines.
- Main Function: The main loop that interacts with the user and performs various actions based on user input.

Usage:
1. LEVI provides a command-line interface where users can input queries.
2. Users can ask LEVI to perform actions like searching Wikipedia, playing music, getting weather forecasts, chatting using GPT-3, opening websites, and more.
3. LEVI responds with both text and speech output.

Note:
- The code may require appropriate API keys and permissions to work correctly.
- Make sure to install the required libraries before running the code.
- Some features, like the GPT-3 chat, require access to external APIs and may need additional setup.

For more information and updates, please refer to the project's official documentation.

"""

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
# For Json
import json
# For Settings
import subprocess


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
# NewsAPI
API_KEY = 'e3135ebe96f24e92a0115a650856f339'
BASE_URL = 'https://newsapi.org/v2/top-headlines'

# Parameters for the request
params = {
    'country': 'in',  # You can change this to your desired country code
    'apiKey': API_KEY
}


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

# Feedback Function
def feedback(name, stars, feed):
    feedback_data = {'name': name, 'stars': stars, 'Feedback': feed}
    with open('feedback.json', 'a') as file:
        json.dump(feedback_data, file)
        file.write('\n')

    print("Thankyou", name, "!", "Your feedback is valuable to us...")
    speak("Thankyou "+ name+ "!"+" Your feedback is valuable to us...")
    time.sleep(6)
    os.system('cls')

# Detect Darkmode
def detect_darkmode_in_windows(): 
    try:
        import winreg
    except ImportError:
        return False
    registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    reg_keypath = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize'
    try:
        reg_key = winreg.OpenKey(registry, reg_keypath)
    except FileNotFoundError:
        return False

    for i in range(1024):
        try:
            value_name, value, _ = winreg.EnumValue(reg_key, i)
            if value_name == 'AppsUseLightTheme':
                return value == 0
        except OSError:
            break
    return False

# For News
def news():
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            articles = data['articles']
            top_headlines = []

            for idx, article in enumerate(articles[:10], start=1):
                title = str(article['title'])
                source = article['source']['name']
                print(f"{idx}. {title}")
                speak(f"{title}")
        else:
            print("Error:", data['message'])
    except Exception as e:
        print("An error occurred:", e)

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
            
        elif 'feedback' in query:
            print("Enter your name :",end="")
            speak("Enter your name")
            name=input()
            print("Please enter your rating out of 10")
            speak("Please enter your rating out of 10")
            try:
                star=int(input())
            except ValueError:
                print("Invalid Input! Please enter again!")
            print("Please tell if you want any other improvements :")
            speak("Please tell if you want any other improvements :")
            feed=input()
            feedback(name,star,feed)            

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
        
        # Displays the top 5 headlines
        elif 'news' in query:
            print("Sure! Here's the top 5 trending headlines")
            speak("Sure! Here's the top 5 trending headlines")
            news()
            time.sleep(10)

        # Switches the Theme
        elif 'switch theme' in query:
            if detect_darkmode_in_windows():
                print("Switching to Light Mode")
                speak("Switching to Light Mode")
                command = ['reg.exe', 'add', 'HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize', '/v', 'AppsUseLightTheme', '/t', 'REG_DWORD', '/d', '1', '/f']
            else:
                print("Switching to Dark Mode")
                speak("Switching to Dark Mode")
                command = ['reg.exe', 'add', 'HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize', '/v', 'AppsUseLightTheme', '/t', 'REG_DWORD', '/d', '0', '/f']    
            print("Theme switched successfully!")        
            speak("Theme switched successfully!")     
            time.sleep(3)   
            subprocess.run(command)

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