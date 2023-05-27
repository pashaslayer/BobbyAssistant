import os, webbrowser, sys, requests, subprocess, pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)


def speaker(text):
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[2].id)
    engine.say(text)
    engine.runAndWait()


def browser():
    webbrowser.open('https://github.com/', new=2)
    print("starting browser")


def offpc():
    # os.system('shutdown /s')
    print("turning off your pc master")


def weather():
    print("weather")


def startPycharm():
    print("starting pycharm")


def offBot():
    sys.exit()


def passive():
    pass
