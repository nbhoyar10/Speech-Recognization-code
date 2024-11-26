import speech_recognition as sr

r = sr.Recognizer()


while True:
    try:
        with sr.Microphone() as source:
            print("Say Something then i will convert it into text for you")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()

            print(f"here's your text : {text}")


    except:
        print("you were trying to say something")
        r = sr.Recognizer()
        continue
