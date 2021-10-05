import pyttsx3
import datetime
import requests
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import pywhatkit
import psutil
import pyjokes
import os
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    _time = datetime.datetime.now().strftime("%I:%M")
    speak("The current time is "+_time)

def date_():
    year = datetime.datetime.now().year
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    if month == 1:
        speak("Today's date is "+ str(day)+'Jan'+str(year))
    elif month == 2:
        speak("Today's date is "+ str(day)+'Feb'+str(year))
    elif month == 3:
        speak("Today's date is "+ str(day)+'March'+str(year))
    elif month == 4:
        speak("Today's date is "+ str(day)+'April'+str(year))
    elif month == 5:
        speak("Today's date is "+ str(day)+'May'+str(year))
    elif month == 6:
        speak("Today's date is "+ str(day)+'June'+str(year))
    elif month == 7:
        speak("Today's date is "+ str(day)+'July'+str(year))
    elif month == 8:
        speak("Today's date is "+ str(day)+'August'+str(year))
    elif month == 9:
        speak("Today's date is "+ str(day)+'September'+str(year))
    elif month == 10:
        speak("Today's date is "+ str(day)+'October'+str(year))
    elif month == 11:
        speak("Today's date is "+ str(day)+'November'+str(year))
    else:
        speak("Today's date is "+ str(day)+'December'+str(year))
    
def tell_weather():
    api_key = "1f0b96148a292aa9cf581c3aba5da199"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + "Karimganj"
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        celsius = float(current_temperature)- 273.15
        temperature = round(celsius)
    speak("Current temperature in Karimganj is "+str(temperature)+"degree celsius")

def begin():
    hour = datetime.datetime.now().hour
    if hour>=6 and hour <12:
        speak("Good morning Tanisha")
    elif hour>=12 and hour<18:
        speak("Good afternoon Tanisha")
    elif hour>=18 and hour<24:
        speak("Good evening Tanisha")
    else:
        speak("Good night, wow you are still awake")
    speak("Good to see you back")
    speak("I will update you about today's temperature, date and time")
    date_()
    time_()
    tell_weather()
    speak("Now tell me bro,what can I do for you!!")


def takecommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Started listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language = 'en-US')
        #speak("hello")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please....")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('26tanishabanik@gmail.com','goal')
    server.sendmail('26tanishabanik@gmail.com',to,content)
    server.close()

def CPUAndBattery():
    pass

def tellJokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    #begin()
    while True:
        query = takecommands().lower()
        if 'bye' in query:
            speak('bye')
            quit()
        elif 'wiki' in query:
            speak("Wait, I am searching")
            query = query.replace('wiki','')
            result = wikipedia.summary(query,sentences=3)
            speak("According to the Wikipedia, ")
            print(result)
            speak(result)
        elif 'send a mail' in query:
            try:
                speak("What do you wanna send?")
                content = takecommands()
                speak('Whom do you want to send the mail?')
                receiver = input("Enter receiver's mail address: ")
                to = receiver
                sendEmail(to,content)
                speak(content)
                speak('Your email has been sent.')
            except Exception as e:
                print(e)
                speak("Can't send mail")
        elif 'search' in query:
            speak("What do you want to search?")
            #chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            search = takecommands().lower()
            url = "https://google.com/search?q=" + search
            wb.get().open(url)
        elif "play a song" in query:
            speak("Which song you wanna listen to?")
            song = input("Enter song name: ")
            #wb.open('https://www.youtube.com/results?search_query=' + str(song))
            pywhatkit.playonyt(song)
            speak("Getting your song, relax and sit down")
            #pywhatkit.playonyt(url)
        elif "open my github" in query:
            speak('Opening your github account.....')
            wb.open("https://github.com/26tanishabanik/")
        elif "joke" in query or "jokes" in query:
            tellJokes()
        elif "open app" in query:
            speak("Which app you wanna open?")
            app = input("Enter app name: ")
            if app == 'notes':
                os.system('Notepad')
            
        

