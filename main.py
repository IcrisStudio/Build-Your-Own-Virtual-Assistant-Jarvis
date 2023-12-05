import os
import pygame
import pyautogui
import pywhatkit
import speech_recognition as sr
# from scrapper.bot_scrapper import *
from datetime import datetime
from gpt4_free import GPT
from functions.emailsender import send_email



def speak(text):
    voice = "en-US-GuyNeural"

    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "audio/output.mp3"'

    os.system(command)

    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load("audio/output.mp3")

        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)

    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')

    except Exception as e:
        print(e)
        return "-"
    return query


sleep_mode = False

speak('Hello sir, I am Jarvis and How can i help you today?')
# click_on_chat_button()
while True:
    query = take_command().lower()
    print('\n You: ' + query)

    if 'open' in query:
        app_name = query.replace('open', '')
        speak('opening ' + app_name)
        pyautogui.press('super')
        pyautogui.typewrite(app_name)
        pyautogui.sleep(1)
        pyautogui.press('enter')

    elif 'play' in query:
        song_name = query.replace('play', '')
        speak('Playing ' + song_name + ' in youtube')
        pywhatkit.playonyt(song_name)

    elif 'switch tab' in query:
        pyautogui.hotkey('ctrl', 'tab')

    elif 'close tab' in query:
        pyautogui.hotkey('ctrl', 'w')

    elif 'close' in query:
        pyautogui.hotkey('alt', 'f4')
        speak('done sir')

    elif 'time' in query:
        current_time = datetime.now().strftime('%H:%M %p')
        speak('Current time is ' + current_time)

    elif 'sleep' in query:
        speak('Ok sir. I am going to sleep but you can call me any time just say wake up and i will be there for you.')
        sleep_mode = True

    elif 'write an email' in query or 'compose an email' in query or 'send an email' in query:
        speak('Sure sir, Can you provide me the name of the user to whom you want to send email below: ')
        recever = input('Enter his/her email address: ')
        speak('What should be the subject of the email')
        subject = take_command()
        speak('What should be the content. Just provide me some prompt')
        email_prompt = take_command()
        content = GPT('write a email for' + email_prompt)
        send_email(recever, subject, content)
        speak(f'Done sir. Email sent succesfully to {recever}')
        
    else:
        res = GPT(query)
        speak(res)

    while sleep_mode:
        query = take_command().lower()
        print(query)
        if 'wake up' in query:
            speak('I am awake now. How can i help  you sir.')
            sleep_mode = False
