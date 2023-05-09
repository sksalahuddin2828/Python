import pyttsx3
import webbrowser

# Initialize the text-to-speech engine
search = pyttsx3.init("sapi5")

# Set the voice to a female voice
voices = search.getProperty("voices")
search.setProperty("voice", voices[1].id)

while True:
    # Get user input
    user_input = input("Enter your text: ").lower()

    # Open YouTube if the user wants to go to YouTube
    if "youtube" in user_input:
        search.say("Opening YouTube, just wait a while")
        search.runAndWait()
        webbrowser.open("https://www.youtube.com/")

    # Search Google if the user wants to search for something
    elif "search" in user_input:
        search.say("What do you want to search from Google?")
        search.runAndWait()
        search_items = input("Give your search keyword: ").lower()
        search.say("Opening your search items, just wait a while")
        search.runAndWait()
        webbrowser.open(f"https://www.google.com/search?q={search_items}")

    # If the user input doesn't match any of the above, ask them to try again
    else:
        search.say("Oops! Please try again.")
        search.runAndWait()
