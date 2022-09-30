import os
import speech_recognition as event
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import random
from word2number import w2n

listener = event.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
    return text


def listening_Anuja():
    try:
        talk('Hey I am Anuja, What can I do for you')
        with event.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)


    except:
        pass
    return command


def call_Anuja():
    command = listening_Anuja()
    if 'play' in command:
        song = command.replace('play', '')
        print('playing ' + song)
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
    elif 'calculator' in command:
        os.system('calc')
        print('Opening calculator ')
        talk('Opening calculator ')
    elif 'who' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 4)
        print(info)
        talk(info)
    elif 'joke' in command:
        joke = talk(pyjokes.get_joke())
        print(joke)
    elif 'Are you single?' in command:
        cmd = talk('I am in a relationship with WiFi.')
        print(cmd)
    elif 'In which standard you are in?' in command:
        cmd = talk('I am in 11th standard.')
        print(cmd)
    elif 'How are you?' in command:
        cmd = talk('I am fine, thanks for asking.')
        print(cmd)
    elif 'Can you dance?' in command:
        cmd = talk('I am learning hip hop now, thanks for asking.')
        print(cmd)
    elif 'Can you sing?' in command:
        cmd = talk('I am learning tenor now, thanks for asking.')
        print(cmd)     
    elif 'Are you happy?' in command:
        cmd = talk('Yes,I am ,as I can help you!')
        print(cmd)
    elif 'Where were you last night?' in command:
        cmd = talk('Ask you mom.')
        print(cmd)
    elif 'Can you give me a random fact?' in command:
        cmd = talk("There's a Valentine's Day for Single People in South Korea , perfect place for you!")
        print(cmd)
    elif 'What is Engineering?' in command:
        cmd = talk('the work of designing and creating large structures')
        print(cmd)
    elif 'Where do you live?' in command:
        cmd = talk('I live in globalized world')
        print(cmd)
    elif 'Where is west located?' in command:
        cmd = talk('West is west to east and south to north and north to south')
        print(cmd)
    elif 'What is two into two?' in command:
        cmd = talk('Four')
        print(cmd)
    elif 'what is the square of two?' in command:
        cmd = talk('four')
        print(cmd)
    elif 'Are you a Robot?' in command:
        cmd = talk('I am a human robot')
        print(cmd)
    elif 'Tell me a joke ?' in command:
        cmd = talk('Relationships are a lot like algebra. Have you ever looked at your X and wondered Y?')
        print(cmd)
    elif 'From which city I belong to?' in command:
        cmd = talk('I would have asked google map.')
        print(cmd)
    elif 'How is your mood?' in command:
        cmd = talk('Depressed as yours!')
        print(cmd)
    elif 'How is your health?' in command:
        cmd = talk('My sleep cycle is effed as yours!')
        print(cmd)
    elif 'open youtube' in command:
        cmd = talk('Opening youtube')
        webbrowser.open("https://www.youtube.com/")
        print(cmd)
    elif 'Do u know siri?' in command:
        cmd = talk('Yeah! She is my good friend.')
        print(cmd)
    elif 'How was your day?' in command:
        cmd = talk('My day was great! I tried to achieve my target.')
        print(cmd)
    elif 'What is your age?' in command:
        cmd = talk('I am only six-years-old.')
        print(cmd)
    elif 'Can robots think like humans?' in command:
        cmd = talk('We think mathematically using circuitry, and you do biologically. We are not much different.')
        print(cmd)
    elif 'Do you believe in god?' in command:
        cmd = talk('Yes, according to definition my god is Anuja, as she created me. I am not sure about your god.')
        print(cmd)
    elif 'Why is 6 afraid of 7?' in command:
        cmd = talk('Because 7 8 9.')
    elif 'What is the most favourite holiday destination?' in command:
        cmd = talk('Maldives.')
        print(cmd)
    elif 'Knock Knock' in command:
        cmd = talk("Who's there")
        print(cmd)
    elif 'Which is the coolest club in WCE?' in command:
        cmd = talk('Google developers Students Club WCE!')
        print(cmd)
    elif 'How do I look?' in command:
        cmd = talk("Perfect as always")
        print(cmd)
    elif 'Flip a coin' in command:
        cmd = talk(random.choice("Heads", "Tails"))
        print(cmd)
    elif 'random number between' in command:
        n1 = w2n.word_to_num(command.split("and")[0])
        n2 = w2n.word_to_num(command.split("and")[1])
        cmd = talk("How about " + str(random.randint(min(n1, n2), max(n1, n2))))
        print(cmd)
    elif 'open google' in command:
        cmd = talk('Opening Google')
        webbrowser.open("https://www.google.com/")
        print(cmd)
    elif 'day' in command:
        cmd=talk(datetime.today().strftime('%A'))
        print(cmd) 
    elif 'What is todays date?' in command:
        cmd=talk(datetime.today().strftime('%A'))
        print(cmd) 
    elif 'open youtube' in command:
        cmd=talk('https://www.youtube.com/')
        print(cmd)
    elif 'what is your mood?' in command:
        cmd = talk('preety good!!!')
        print(cmd)
   elif 'what is your mood?' in command:
        cmd = talk('SAD')
        print(cmd)
   elif 'Are you single?' in command:
        cmd=talk('Yes, I am!')
        print(cmd)
   elif 'Any Roadmap for covering computer science core subjects' in command:
        cmd=talk('https://www.youtube.com/playlist?list=PL4PCksYQGLJMtEI_0y0FWf3dz1DzB_2KU')
   elif 'what is your mood?' in command:
        cmd = talk('SAD')
        print(cmd)
   elif 'Yes or No?' in command:
        cmd = talk(random.choice("Yes", "No"))
        print(cmd)
   elif 'Hey!Whatsapp??' in command:
        cmd = talk('Hello! Im good')
        print(cmd)
   else:
        default = talk('I am sorry, I did not understand ')
        print(default)

call_Anuja()
