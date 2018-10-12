import speech_recognition as sr

# Obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Please say something to me!")
    audio = r.listen(source)
    print("Got it! Now to recognize it ...")

#Recognize speech using Google
try:
    print("You said: " + r.recognize_google(audio))
    print("\nAudio Succesfully Recorded! Check file directory")
except Exception as e:
    print(e)

# Write audio to a Wav file
with open("microphone-result.wav", "wb") as f:
    f.write(audio.get_wav_data())

# Write audio to an AIFF file
with open("microphone-result.aiff", "wb") as f:
    f.write(audio.get_aiff_data())

# Write audio to an Flac file
with open("microphone-result.flac", "wb") as f:
    f.write(audio.get_flac_data())


