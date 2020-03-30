import pyttsx3
import webbrowser
import random
import wikipedia
import datetime
import wolframalpha
import sys
import speech_recognition as sr
import time


engine = pyttsx3.init('sapi5')
chromedir = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
client = wolframalpha.Client('UXTH2K-EGA848229T')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def say(audio):
    print('IRIS: '+audio)
    engine.say(audio)
    engine.runAndWait()

def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-US')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        say('Sorry! I didn\'t get that in this movement! Try typing the command!')
        query = str(input('Command: '))

    return query

def wish():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 5 and currentH < 12:
        say('Good Morning! I hope your day is as positive and beautiful as you are.')

    if currentH >=12 and currentH < 16:
        say('Nature looks more beautiful at this time of the day! Good Afternoon')

    if currentH >= 16 and currentH < 22:
        say('Good Evening! Dude')

    if currentH >= 22 and currentH < 5:
        say("Hey, a good night's sleep is very important! Go to bed now, I'll be here tomorrow ")


wish()


if __name__ == '__main__':
    while True:
        query = myCommand()
        query = myCommand().lower()

        if 'open youtube' in query:
            webbrowser.get(chromedir).open('www.youtube.com')
            say('Okay, I have opened Youtube')

        elif 'open google' in query:
            webbrowser.get(chromedir).open('www.google.co.in')
            say('Okay, I have opened Google')

        elif 'open gmail' in query:
            webbrowser.get(chromedir).open('www.gmail.com')
            say('Okay, I have opened Gmail')

        elif 'open reddit' in query:
            webbrowser.get(chromedir).open('www.reddit.com')
            say('Okay, I have opened Reddit')

        elif 'open facebook' in query:
            webbrowser.get(chromedir).open('www.facebook.com')
            say('Okay, I have opened Facebook')

        elif 'open instagram' in query:
            webbrowser.get(chromedir).open('www.instagram.com')
            say('Okay, I have opened insta gram')

        elif 'open twitter' in query:
            webbrowser.get(chromedir).open('www.twitter.com')
            say('Okay, I have opened Twitter')

        elif 'open quora' in query:
            webbrowser.get(chromedir).open('www.quora.com')
            say('Okay, I have opened Quora')

        elif 'open tumblr' in query:
            webbrowser.get(chromedir).open('www.tumblr.com')
            say('Okay, I have opened Tumblr')

        elif 'open wikipedia' in query:
            webbrowser.get(chromedir).open('www.wikipedia.org')
            say('Okay, I have opened Wikipedia')

        elif 'open yahoo' in query:
            webbrowser.get(chromedir).open('www.yahoo.com')
            say('Okay, I have opened Yahoo')

        elif "open dominos" in query:
            webbrowser.get(chromedir).open('www.dominos.com')
            say('Okay, I have opened Dominos')

        elif 'open amazon' in query:
            webbrowser.get(chromedir).open('www.amazon.in')
            say('Okay, I have opened Amazon')

        elif 'wassup' in query or 'watsapp' in query or 'what are you doing' in query or 'what doing' in query:
            randList2 = ['Working for you!','Getting some things ready for you!','listening songs!','Spending time for fixing some bugs in some softwares','Waiting for your commands']
            say(random.choice(randList2))

        elif 'i am bored' in query or 'say me any facts' in query or 'say facts for me' in query:
            randList3 = ['The First Computer Was Invented in the 1940s','Space Smells Like Seared Steak','The Supreme Court has its own private basketball court with an amazing nickname','The Unicorn Is the National Animal of Scotland','The Total Weight of Ants on Earth Once Equaled the Total Weight of People','“E” Is the Most Common Letter and Appears in 11 Percent of All English Words','Pringles Aren’t Actually Potato Chips','Showers Really Do Spark Creativity','Dolphins Have Been Trained to Be Used in Wars','Playing the Accordion Was Once Required for Teachers in North Korea','Water Makes Different Pouring Sounds Depending on its Temperature','Riding a Roller Coaster Could Help You Pass a Kidney Stone','Bee Hummingbirds Are So Small They Get Mistaken for Insects','Sea Lions Can Dance to a Beat']
            say('Really? then, let me say you some facts....')
            say(random.choice(randList3))
            say('Wow! that was good right!?. So then...')

        elif 'what is the time now' in query or 'say the time now' in query or 'what time' in query:
            currentH = int(datetime.datetime.now().hour)
            currentM = int(datetime.datetime.now().minute)
            currentH = str(currentH)
            currentM = str(currentM)
            say('The time now is' + currentH, ':', currentM)

        elif 'what is your name' in query:
            say('My name is IRIS')

        elif 'who created you' in query:
            say('My creator is Rishi')

        elif 'bye' in query or 'abort' in query or 'nothing' in query:
            say('bye! see you later.....')
            sys.exit()

        else:
            query = query
            say('Thinking off...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    say('Got it.')
                    say(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    say('Got it.')
                    say(results)

            except:
                say('I think there is something problem in my mouth, so I will open google for you to see results!!')
                query = query.replace(' ', '+')
                webbrowser.get(chromedir).open('https://www.google.com/search?q='+query)
        time.sleep(1)
        listmist = ['Next command please', 'Next...', 'Dude, I am bored! so please ask me more things!!']

        say(random.choice(listmist))
