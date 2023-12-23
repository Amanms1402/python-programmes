import time
from googletrans import Translator

# Create a Translator object
translator = Translator()

# Define the text to be translated 
text_to_translate = "나는 죽을 때까지 당신과 싸울 것입니다"

# Add a delay of 5 seconds
time.sleep(5)

# Translate the text into English
translated_text = translator.translate(text_to_translate, src="ko", dest="en")

# Print the translated text
print(translated_text.text)
