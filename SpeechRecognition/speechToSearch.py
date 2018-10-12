import speech_recognition as sr
import webbrowser

r3 = sr.Recognizer()
r2 = sr.Recognizer()
r = sr.Recognizer()
with sr.Microphone() as source:
    # Adapt the noise
    r.adjust_for_ambient_noise(source)
    print("Options:\n [Search Web] | [Search Music]")
    print("Please which one you would like to search:")
    audio= r.listen(source)

if "web" in r2.recognize_google(audio):
    #Obtain Audio when the word 'web' is heard
    r2 =sr.Recognizer()
    url = 'https://en.wikipedia.org/wiki/'
    with sr.Microphone() as source:
        print("Please say what you would like to search ")
        audio = r.listen(source)

        try:
            get = r2.recognize_google(audio)
            print("Google thinks you said: \n " + get)
            webbrowser.open_new(url+get)
        except sr.UnknownValueError:
            print("Sorry could not understand Audio ")
        except sr.RequestError as e:
            print("Failed to retrive results",format(e))

if "music" in r3.recognize_google(audio):
    # Obtain Audio when the word muic is heard
    url2 = 'https://www.youtube.com/results?search_query='
    r3 = sr.Recognizer()
    with sr.Microphone() as source:
        print("Search for Music Video \n Please state the name of music:")
        audio = r.listen(source)

        try:
            text = r3.recognize_google(audio)
            print("Google thinks you said:\n" + text)
            webbrowser.open_new(url2+text)
        except sr.UnknownValueError:
            print("Sorry could not understand Audio")
        except sr.RequestError as e:
            print("Faild to retrive results",format(e))
