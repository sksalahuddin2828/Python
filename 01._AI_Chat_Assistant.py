import pyttsx3
import webbrowser
import datetime
import pywhatkit
import requests

# Initialize the text-to-speech engine
search = pyttsx3.init("sapi5")

print("Sk. Salahuddin - Morning 01 Batch")

# Set the voice to a female voice
voices = search.getProperty("voices")
search.setProperty("voice", voices[-1].id)

def speak(text):
    search.say(text)
    search.runAndWait()

def esshan():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour < 19:
        speak("Good evening")
    else:
        speak("Good night!")

# Opening Welcome or you can set greetings in here:
speak("Welcome. Sheikh Salahuddin, how may I help you?")
esshan()

def get_weather(city):
    # API URL with your API key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=API_KEY&units=metric'

    # Send an HTTP GET request to the API and get the response
    response = requests.get(url)

    # Check if the API call was successful
    if response.status_code == 200:
        # Parse the JSON response to get the weather information
        weather = response.json()

        # Extract the relevant weather information from the JSON response
        temperature = weather['main']['temp']
        humidity = weather['main']['humidity']
        description = weather['weather'][0]['description']

        # Return the weather report for the city
        return f"The temperature in {city} is {temperature} Kelvin. The humidity is {humidity}% and the weather is {description}."
    else:
        # Return an error message if the API call was not successful
        return "Unable to get the weather report. Please try again later."
    
get_weather("khulna")

while True:
    # Get from input by user
    user_input = input("Enter your text: ").lower()
    
    # If you want to shut down it use this three 3 keywords : good bye / ok bye / turn off 
    if "good bye" in user_input or "ok bye" in user_input or "turn off" in user_input:
        speak('Take care, and see you later, Bye!')
        break

    # AI talks or say it everytime when user gives input
    speak("Please wait for a few seconds, I'm opening now")

    # Check if the user wants the weather report
    if 'weather' in user_input:
        # Ask for the city name
        search.say("Sure, which city?")
        search.runAndWait()

        # Get the city name from the user
        city = input("Enter the city name: ")

        # Get the weather report for the city
        weather_report = get_weather(city)

        # Speak the weather report
        speak(weather_report)

    # Open YouTube if the user wants to go to YouTube
    if "youtube" in user_input:
        search.say("OK, What do you want to search from YouTube?")
        search.runAndWait()
        search_youtube = input("Enter:--> Open YouTube / Search on YouTube / Play on YouTube: ")

        # Open YouTube if the user wants to go to YouTube
        if "open youtube" in search_youtube:
            search.say("Opning YouTube, Please wait for a while!")
            search.runAndWait()
            webbrowser.open("https://www.youtube.com/")

        # Open YouTube search if the user wants search on YouTube
        elif "search youtube" in search_youtube:
            search.say("What do you want to search from YouTube?")
            search.runAndWait()
            search_youtube_items = input("Give your search keyword: ").lower()
            search.say("Opening your search items from YouTube, just wait for a while")
            search.runAndWait()
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_youtube_items}")

        # Play on YouTube if the user wants to go to play anything from YouTube
        elif "play" in search_youtube:
            search.say("What do you want to Playing on YouTube?")
            search.runAndWait()
            song = input("Enter search :")
            search.say("You want to listen from YouTube " + song)
            search.runAndWait()
            pywhatkit.playonyt(song)

    # From the user is asked to know your local time and date together
    elif 'time' in user_input:
        now = datetime.datetime.now()
        date = now.strftime('%Y-%m-%d')
        clock = now.strftime('%I:%M %p')
        speak(f"Today's date is {date} and the current time is {clock}")

#--------------------Single Date and Single Time area Start-----------------------

# কমেন্ট করা আছে কমেন্ট টি মুছে ব্যবহার করুন - যদি শুধু তারিখ (Date) অথবা সময় (Time) ব্যবহার করতে চান
# Commented Use Delete Comment - If you want to use only Date or Time

    # From the user is asked to know your only local time
    # শুধু সময় (Only Time)
    # elif 'time' in user_input:
    #     clock = datetime.datetime.now().strftime('%I:%M %p')
    #     speak(f"Your local time is {clock}")

    # From the user is asked to know your only local date
    # শুধু তারিখ (Only Date)
    # elif 'date' in user_input:
    #     date = datetime.datetime.now().strftime('%Y-%m-%d')
    #     speak(f"Your local time is {date}")

#---------------------Single Date and Single Time area END------------------------

    # From the user is asked if he wants to open Facebook
    elif "facebook" in user_input:
        search.say("What do you want to search from Facebook?")
        search.runAndWait()
        search_from_facebook = input("Enter:--> Open Facebook / Facebook Profile / Facebook Settings / Facebook Reel / Facebook Messenger / Facebook Video / Facebook Notification: ").lower()

        # Open Facebook if the user wants to go to Facebook
        if "open facebook" in search_from_facebook:
            search.say("Opning Facebook, Please wait for a while!")
            search.runAndWait()
            webbrowser.open("https://www.facebook.com/")

        # Open Facebook profile if the user wants to go to Facebook profile
        elif "facebook profile" in search_from_facebook: 
            search.say("Opening Facebook profile")
            search.runAndWait()   
            webbrowser.open(f"https://www.facebook.com/profile.php?=facebook%20{search_from_facebook}")

        # Open Facebook settings if the user wants to go to Facebook settings
        elif "facebook settings" in search_from_facebook: 
            search.say("Opning Facebook settings")
            search.runAndWait() 
            webbrowser.open(f"https://www.facebook.com/settings/?tab=account{search_from_facebook}")

        # Open Facebook Reel if the user wants to go to Facebook Reel
        elif "facebook reel" in search_from_facebook: 
            search.say("Opning Facebook Reel")
            search.runAndWait() 
            webbrowser.open(f"https://www.facebook.com/reel/?s=ifu{search_from_facebook}")
        
        # Open Facebook Messenger if the user wants to go to Facebook Messenger
        elif "facebook messenger" in search_from_facebook: 
            search.say("Opning Facebook Messenger")
            search.runAndWait() 
            webbrowser.open(f"https://www.facebook.com/messages/t/{search_from_facebook}")

        # Open Facebook Video if the user wants to go to Facebook Video
        elif "facebook video" in search_from_facebook: 
            search.say("Opning Facebook Video")
            search.runAndWait() 
            webbrowser.open(f"https://www.facebook.com/video/")

        # Open Facebook Notifications if the user wants to go to Facebook Notifications
        elif "facebook notification" in search_from_facebook: 
            search.say("Opning Facebook Video")
            search.runAndWait() 
            webbrowser.open(f"https://www.facebook.com/notifications{search_from_facebook}")

    # Search Google Map if the user wants to search for something
    elif "map" in user_input:
        search.say("What do you want to search from Google Map?")
        search.runAndWait()
        search_from_map = input("Enter Google map / City: ").lower()

        # Search for Google map
        if "google map" in search_from_map:
            search.say("Opning Google Map, Please wait for a while!")
            search.runAndWait()
            webbrowser.open(f"https://www.google.com/maps/")

        # Search for Google map for to know city location
        elif "city" in search_from_map: 
            search.say("Give me a city name")
            search.runAndWait()
            city_name = input("Give your city name: ").lower()
            search.say("Opening your entire city, just wait for a while")
            search.runAndWait()
            webbrowser.open(f"https://www.google.com/maps/place/{city_name}")

    # Search Google if the user wants to search for something
    elif "google" in user_input:
        search.say("What do you want to search from Google?")
        search.runAndWait()
        search_items = input("Give your search keyword: ").lower()
        search.say("Opening your search items, just wait for a while")
        search.runAndWait()
        webbrowser.open(f"https://www.google.com/search?q={search_items}")  
