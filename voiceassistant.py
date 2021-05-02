#Importing the libraries
import speech_recognition as sr
import pyttsx3
import pywhatkit as kit

listener = sr.Recognizer()    #Creating the recognizer object
speaker = pyttsx3.init()      #Creating the text to speach object

voices = speaker.getProperty('voices')   #Getting the system voices
speaker.setProperty('voice', voices[1].id)   #Setting our assistant for female voice

def speak(command):
    speaker.say(command)          #Assistant will speak the message passed by the used
    speaker.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:    #Using the microphone for the command
            print("Please speak, I'm listening.....")
            voice = listener.listen(source)  #Calling our library to recognize the source
            command = listener.recognize_google(voice)  #Using google-api to recognize the command
            command = command.lower()
            if 'youtube' in command:
                #speak(command)
                command = command.replace('youtube', '')      #We don't want assistant to speak youtube. Removing it from the command 
                print(command)    

    except:
        pass
    return command

def run_assistant():
    command = listen()     #Calling the listen function to take the command from user
    print(command)
    if 'play' in command:
        song = command.replace('play', '')           #We don't want assistant to speak play. Removing it from the command 
        speak('Playing' + song)
        kit.playonyt(song)
    else:
        speak('Please come again')

while True:
    run_assistant()