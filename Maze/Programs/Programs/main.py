from playsound import playsound
import win32com.client as wc
import time
import pygame
import os
pygame.mixer.init()

pygame.mixer.music.load('Current.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

speak = wc.Dispatch("Sapi.SpVoice")

say = speak.speak
say("Next you come accross 2 buttons")
say("Witch would you like to press first (1 or 2)")
button = input("1\\2 | ")

if button == "1":
    say("press Enter to press the button")
    input("")
    playsound("Button.wav")
    say("you wait and you wait.. everythings fine until")
    #pause()
    playsound("Swoosh.wav")
    say("Arows start shooting at you.... but you can still get to the other button")
    say("but... wait???")

    playsound("Grind.wav")

    say("the other butten is sealed. then you see a key.")
    say("it's ???just??? out of your reach!")
    say("so you go get the key")
    say("you run past the arrows unlocking the door... it opens!!!")
    playsound("Grind.wav")
    os.system('cd maze')
    os.system('pythonwalklong.py')
    quit()



    

      
