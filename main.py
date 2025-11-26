import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import asyncio

def speak(text, language="en"):
  engine = pyttsx3.init()
  engine.setProperty("rate", 150)
  voices = engine.getProperty('voices')
  if language == "en":
    engine.setProperty('voice', voices[0].id)
  else:
    engine.setProperty('voice', voices[1].id)
  engine.say(text)
  engine.runAndWait()
def speech_to_text():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("please speak now in english")
    audio = recognizer.listen(source)
  try:
    print("recognising speech now")
    text = recognizer.recognize_google(audio, language="en-US")
    print("you said: ", text)
    return text
  except sr.UnknownValueError:
       print("sorry could not recognise your voice")
  except sr.RequestError as e:
      print("could not request results; {0}".format(e))
  return ""
async def translate_text(text, dest_language):
    translator = Translator()
    translation = await translator.translate(text, dest=dest_language)
    print(translation)
    return translation.text
def display_language_options():
    print("choose a language to translate to:")
    print("1. Spanish (sp)")
    print("2. French (fr)")
    print("3. German (ge)")
    print("4. Italian (it)")
    print("5. Dutch (du)")
    choice = input("please select the target language number (1-5): ")
    language_dict = {
        "1": "sp",
        "2": "fr",
        "3": "ge",
        "4": "it",
        "5": "du"

    }
    return language_dict.get(choice, "es")
async def main():
  target_language = display_language_options()
  orignal_text = speech_to_text()
  if orignal_text:
    translated_text = await translate_text(orignal_text, target_language)
    speak(translated_text, language="en")
    print("translated text: ", translated_text)
if __name__ == "__main__":
  asyncio.run(main())
  
  