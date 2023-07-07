from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr

analyzer = SentimentIntensityAnalyzer()
recognizer = sr.Recognizer()

def clear_background_noise():
    with sr.Microphone() as source:
        print('Clearing background noise...')
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print('Background noise cleared.')

def listen_for_message():
    with sr.Microphone() as source:
        print('Waiting for your message...')
        recorded_audio = recognizer.listen(source)
        print('Done recording.')

    try:
        print('Printing the message..')
        text = recognizer.recognize_google(recorded_audio, language='en-US')
        print('Your message: {}'.format(text))
        return text
    except Exception as ex:
        print(ex)
        return None

def analyze_sentiment(text):
    if text:
        sentence = [text]
        for i in sentence:
            sentiment_scores = analyzer.polarity_scores(i)
            print(sentiment_scores)

# Main program
clear_background_noise()
message = listen_for_message()
analyze_sentiment(message)
