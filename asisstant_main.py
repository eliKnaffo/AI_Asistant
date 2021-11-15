import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import keyboard
import pywhatkit
import pyautogui as pg



webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))

engine = pyttsx3.init('sapi5')


voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


#SPEAK FUNCTION#

def speak(audio):
    engine.say(audio)
    engine.runAndWait() #makes the speach "audioable"



#time of day fun#
def wishme():
    hour = int(datetime.datetime.now().hour)    

    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        print("Good Afternoon!")
    else:
        speak("Good Night!")
        print("Good Night!")

    speak("Hello sir,how can i help you today")


#speech recog func#
#takes mic input and converts it to string
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.    
    except Exception as e:
        # print(e)  use only if you want to print the error!
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


#MAIN#
if __name__ == '__main__' :
    wishme()
    while True:
        query = takeCommand().lower()

        if 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.get('chrome').open_new_tab("youtube.com")

        elif 'open google' in query:
            speak("Opening google")
            webbrowser.get('chrome').open_new_tab("google.com")
        #OPEN SPOTIFY WILL BE HERE NEXT!!#
        elif 'what do you think about other AI' in query:
            speak("who? i am the only AI")

        elif 'what is the time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        #OPEN STACK OVERFLOW WILL BE IMPLEMENTED AFTER#
        #OPEN APPLE TV WILL BE IMPLEMENTED AFTER#
        elif 'search google for ' in query:
            search_term = query[17 : query.__len__()]
            speak("searching!")

            webbrowser.get('chrome').open_new_tab("https://www.google.com/search?q="+search_term)
            print("searching for "+search_term)

        elif 'search youtube for ' in query:
            search_term = query[18:query.__len__()]
            speak("Searching!")
            webbrowser.get('chrome').open_new_tab("https://www.youtube.com/results?search_query="+search_term)

        elif 'close all' in query:
            speak("Closing all open tabs")
            keyboard.press_and_release('alt+f4') #closes all tabs#

        elif 'send message ' in query:
            speak("Sending messege")
            if(query.__len__() > 17):
                pywhatkit.sendwhatmsg_instantly('+9720502910350',query[12:query.__len__()])
            else:
                pywhatkit.sendwhatmsg_instantly('+9720502910350','מה קורה')
            pg.press("tab")
            pg.press("tab")
            pg.press("tab")
            pg.press("tab")
            pg.press("tab")
            pg.press("tab")
            pg.press("tab")
            pg.press("tab")
            pg.press("tab")
            pg.press("enter")

        elif 'exit' in query:
            speak('okay boss, please call me when you need me')
            quit()
