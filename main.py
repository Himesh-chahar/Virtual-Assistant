# Jarvis virtual assisstant

import webbrowser
import os
import speech_recognition as sr
import pyttsx3
import musiclibrary
import sys
from gtts import gTTS
import pygame

recognizer = sr.Recognizer()
recognizer.energy_threshold = 400
recognizer.dynamic_energy_threshold = True
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak_old(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open ac" in c.lower():
        webbrowser.open("https://www.apnacollege.in/home-post-login")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://openai.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "open himesh" in c.lower():
        # os.O_DIRECTORY("E:\Himesh")
        pass
    elif "exit" in c.lower():
        speak("Goodbye!")
        print("Goodbye!")
        sys.exit(0)



if __name__ == "__main__":
    speak("Initializing jarvis...")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yeah baby!")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))




