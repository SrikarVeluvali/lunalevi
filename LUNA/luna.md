# LUNA (Logical User-friendly Navigation Assistant) Documentation

**Author:** Srikar Veluvali

## Description

LUNA (Logical User-friendly Navigation Assistant) is a virtual assistant designed to simplify navigation and provide a range of functionalities, including text-to-speech, Wikipedia information retrieval, web browsing, music playback, weather forecasts, chat using GPT-3 API, news headlines, system commands, and more.

## Modules Used

- `pyttsx3`: Microsoft Text-to-Speech engine.
- `datetime`: Date and time functions.
- `wikipedia`: Query Wikipedia articles.
- `webbrowser`: Open web pages in a browser.
- `spotipy`: Access the Spotify API for music playback.
- `openai`: Interact with the GPT-3 API.
- `os`: General file and system operations.
- `time`: Time-related functions.
- `requests`: Make HTTP requests.
- `speedtest`: Test internet speed.
- `imdb`: Query movie and series information.
- `json`: Work with JSON data.
- `subprocess`: Execute system commands.

## API Setups

- **Microsoft Text To Speech API:** Initialize the text-to-speech engine.
- **Spotify Client:** Set up Spotify API credentials for music playback.
- **OpenAI API:** Set the API key for GPT-3 interaction.
- **Weather API:** Configure the API key for weather forecasts.
- **Movies Database:** Set up IMDb API for movie and series information.
- **News API:** Configure the API key and base URL for news headlines.

## Functions

- `speak(audio)`: Convert text to speech and audibly communicate.
- `wishMe()`: Greet the user based on the time of day.
- `feedback(name, stars, feed)`: Collect and store user feedback.
- `detect_darkmode_in_windows()`: Check if dark mode is enabled on Windows.
- `news()`: Retrieve and display top news headlines.
- *Main Function*: The central loop for user interaction and action execution.

## Usage

1. LUNA offers a command-line interface for user queries.
2. Users can instruct LUNA to perform tasks such as Wikipedia searches, music playback, weather forecasts, GPT-3 chat, website openings, and more.
3. LUNA responds with both text and speech outputs.

## Note

- The code may require appropriate API keys and permissions.
- Install the required libraries before running the code.
- Some features, like GPT-3 chat, rely on external APIs and may need additional setup.

For further details and updates, refer to the official project documentation.

---

## LUNA (Logical User-friendly Navigation Assistant) Commands

Here's a list of LUNA commands along with brief descriptions of their functionalities.

### General Commands

- `exit` or `quit`: Terminate the LUNA assistant.

### Information Retrieval

- `wikipedia [topic]`: Search Wikipedia for a topic and provide a summary.

### Feedback

- `feedback`: Provide feedback about the assistant's performance.

### Documentation

- `luna help`: Open the LUNA AI documentation.

### Web Browsing

- `open site [URL]`: Open a specified website in the default web browser.
- `open youtube`: Open YouTube in the default web browser.
- `open google [search_query]`: Open Google homepage or perform a search.
- `open chat gpt`: Open ChatGPT website.
- `open bird`: Open Google Bard website.
- `open leetcode`: Open LeetCode problems page.

### Music Playback

- `play music [song_name]`: Search and play music on Spotify.

### Date and Time

- `date today` or `day today`: Display the current date and day.
- `time now`: Display the current time.

### Movie Review

- `movie review [movie_title]`: Display information and summary of a movie or series.

### Chat with GPT-3

- `ask luna [question]`: Engage in a conversation with the GPT-3 chatbot.

### Weather Forecast

- `weather today [city_name]`: Display the weather forecast for a specified city.

### News Headlines

- `news`: Display the top trending news headlines.

### System Commands

- `switch theme`: Switch between light and dark mode.
- `open vs code`: Open Visual Studio Code.
- `open games`: Open the games folder.
- `open command prompt`: Open Command Prompt.
- `open calculator`: Open Calculator.
- `open notepad`: Open Notepad.
- `internet speed`: Test and display internet speed.

### Remember and Forget

- `remember that [message]`: Store a message for later recall.
- `what do you remember`: Recall the stored message.
- `forget what you remember`: Clear the stored message.

Please note that LUNA's functionality relies on API integrations and external services, and some commands may require additional setup or permissions.