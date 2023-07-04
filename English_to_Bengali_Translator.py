import requests

def translate_text(text, target_language):
    api_key = "YOUR_API_KEY"  # Replace with your own Google Translate API key
    url = "https://translation.googleapis.com/language/translate/v2"
    
    params = {
        "key": api_key,
        "q": text,
        "target": target_language
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        translated_text = response.json()["data"]["translations"][0]["translatedText"]
        return translated_text
    else:
        print("Translation failed.")
        return None

# Example usage
english_text = input("Enter the English text to translate: ")
bengali_text = translate_text(english_text, "bn")
print("Translated text: ", bengali_text)
