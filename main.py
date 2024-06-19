import pyttsx3
import random
import datetime
import subprocess
import urllib.request


engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)
ru_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'
en_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'

def listen():
    return (input("скажи команду :"))

def music():
    pass


def open_programm():
    pass

def message_to_say(message):
    print(message)
    engine.say(message)
    engine.runAndWait()


def comand_to_do(message):
    privetstviya = 'Привет','Здравствуй','Здравствуйте','Приветствую вас','Салют','привет','здравствуй','Здравствуйте'
    proschania = 'прощай','пока','бывай'
    message = message.lower()
    if message in privetstviya:
        message_to_say(random.choice(privetstviya))
    elif message in proschania:
        message_to_say(random.choice(proschania))
    elif "сколько время" in message:
        cur_time = str(datetime.datetime.now())[11:-7]
        print(cur_time[0:2],'часов',cur_time[3:5],' минут',cur_time[6:8],' секунд',)
    else:
        message_to_say("я вас не понимаю")
    exit()


if __name__ == '__main__':
    engine.say('Привет,я луна - ваш персональный помошник ')
    while 1:
        command = listen()
        comand_to_do(command)

engine.runAndWait()
