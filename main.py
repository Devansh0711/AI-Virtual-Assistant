import requests
from datetime import datetime
import pyttsx3
import speech_recognition as sr
from random import choice
from decouple import config
from pprint import pprint
from utils import opening_text
from functions.online_ops import (
    find_my_ip, get_latest_news, get_random_advice, 
    get_random_joke, get_trending_movies, get_weather_report, 
    play_on_youtube, search_on_google, search_on_wikipedia, 
    send_email, send_whatsapp_message
)
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord

# Load configurations
USER = config('USER')
BOT_NAME = config('BOTNAME')

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)  # Set speech rate
engine.setProperty('volume', 1.0)  # Set volume level
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Set voice to female

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greet the user based on the current time."""
    current_hour = datetime.now().hour
    if 6 <= current_hour < 12:
        speak(f"Good Morning {USER}")
    elif 12 <= current_hour < 16:
        speak(f"Good Afternoon {USER}")
    elif 16 <= current_hour < 19:
        speak(f"Good Evening {USER}")
    speak(f"I am {BOT_NAME}. How can I assist you today?")

def get_user_input():
    """Capture and process user input through the microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    
    try:
        print('Recognizing...')
        query = recognizer.recognize_google(audio, language='en-in')
        if 'exit' in query or 'stop' in query:
            current_hour = datetime.now().hour
            if 21 <= current_hour < 6:
                speak("Good night, take care!")
            else:
                speak("Have a great day!")
            exit()
        else:
            speak(choice(opening_text))
    except Exception as e:
        speak('Sorry, I did not catch that. Could you please repeat?')
        query = 'None'
    return query.lower()

if __name__ == '__main__':
    greet_user()
    while True:
        command = get_user_input()
        
        if 'open notepad' in command:
            open_notepad()

        elif 'open discord' in command:
            open_discord()

        elif 'open command prompt' in command or 'open cmd' in command:
            open_cmd()

        elif 'open camera' in command:
            open_camera()

        elif 'open calculator' in command:
            open_calculator()

        elif 'ip address' in command:
            ip = find_my_ip()
            speak(f'Your IP Address is {ip}. I am displaying it on the screen for you.')
            print(f'Your IP Address is {ip}')

        elif 'wikipedia' in command:
            speak('What would you like to search for on Wikipedia?')
            search_term = get_user_input()
            result = search_on_wikipedia(search_term)
            speak(f"According to Wikipedia, {result}")
            speak("I am displaying the result on the screen for you.")
            print(result)

        elif 'youtube' in command:
            speak('What would you like to play on YouTube?')
            video_query = get_user_input()
            play_on_youtube(video_query)

        elif 'search on google' in command:
            speak('What would you like to search on Google?')
            google_query = get_user_input()
            search_on_google(google_query)

        elif "send whatsapp message" in command:
            speak('Please enter the phone number:')
            phone_number = input("Enter the number: ")
            speak("What is the message?")
            message = get_user_input()
            send_whatsapp_message(phone_number, message)
            speak("Message has been sent.")

        elif "send an email" in command:
            speak("Please enter the recipient's email address:")
            email_address = input("Enter email address: ")
            speak("What is the subject?")
            subject = get_user_input()
            speak("What is the message?")
            email_message = get_user_input()
            if send_email(email_address, subject, email_message):
                speak("Email has been sent.")
            else:
                speak("There was an issue sending the email. Please check the error logs.")

        elif 'joke' in command:
            joke = get_random_joke()
            speak(f"Here's a joke for you: {joke}")
            speak("I am displaying it on the screen for you.")
            pprint(joke)

        elif "advice" in command:
            advice = get_random_advice()
            speak(f"Here's some advice: {advice}")
            speak("I am displaying it on the screen for you.")
            pprint(advice)

        elif "trending movies" in command:
            trending_movies = get_trending_movies()
            speak(f"The current trending movies are: {', '.join(trending_movies)}")
            speak("I am displaying them on the screen for you.")
            print(*trending_movies, sep='\n')

        elif 'news' in command:
            latest_news = get_latest_news()
            speak(f"Here are the latest news headlines: {latest_news}")
            speak("I am displaying them on the screen for you.")
            print(*latest_news, sep='\n')

        elif 'weather' in command:
            ip = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip}/city/").text
            speak(f"Fetching weather report for {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}°C, but it feels like {feels_like}°C.")
            speak(f"Weather condition: {weather}")
            speak("I am displaying the details on the screen for you.")
            print(f"Description: {weather}\nTemperature: {temperature}°C\nFeels like: {feels_like}°C")
