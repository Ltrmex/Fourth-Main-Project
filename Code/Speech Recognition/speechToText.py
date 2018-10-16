import speech_recognition as sr

 # Obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
     r.adjust_for_ambient_noise(source)
     print("Please say something to me!")
     audio = r.listen(source)

 # Recognize speech using Google 
try:
     print("You said: " + r.recognize_google(audio))
except Exception as e:
     print(e)
