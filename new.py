import speech_recognition as sr
from googletrans import Translator
import pyttsx3

def a(text,language="en"):
  eng=pyttsx3.init()
  eng.setProperty("rate",150)
  eng.setProperty("volume",1)
  voices=eng.getProperty("voices")
  if language=="en":
    eng.setProperty("voice",voices[0].id)
  else:
    eng.setProperty("voice",voices[1].id)
  eng.say(text)
  eng.runAndWait()
def STT():
  recognizer=sr.Recognizer()
  with sr.Microphone() as b:
    print("speak now in english")
    audio=recognizer.listen(b)
  try:
    print("Recognizing Speech")
    text=recognizer.recognize_google(audio,language="en")
    print(f"You said: {text}")
    return text
  except sr.UnknownValueError:
    print("Couldn't understand audio")
    return ""
  except sr.RequestError as e:
    print(f"Could not request results; {e}")
    return ""
def translate(text,target_language="es"):
  translator=Translator()
  translation=translator.translate(text,dest=target_language)
  print(f"Translated text: {translation.text}")
  return translation.text
def display():
  print("Available Languages-")
  print("1.Hindi(hi)")
  print("2.Tamil(ta)")
  print("3.Telugu(te)")
  print("4.Marathi(mr)")
  print("5.Gujarati(gu)")
  print("6.French(fr)")
  print("7.Malayalam(ml)")
  print("8.Punjabi(pa)")
  print("9.Bengali(bn)")
  print("10.German(de)")
  ch=int(input("Enter your choice:"))
  d={1:"hi",2:"ta",3:"te",4:"mr",5:"gu",6:"fr",7:"ml",8:"pa",9:"bn",10:"de"}
  return d.get(ch,"es")
def main():
  target_language=display()
  while True:
    original_text=text()
    if not original_text:
      continue
    if original_text.lower() in ["exist","stop"]:
      speak("Goodbye")
      break
  translated_text=translate(original_text,target_language)
  if translated_text:
    speak(translated_text,rate=130)

main()
