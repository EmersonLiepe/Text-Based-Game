# intro.py

import win32com.client as wc
speak = wc.Dispatch("Sapi.SpVoice")

say = speak.speak
from playsound import playsound

import os
def testing():
    say("testing...")
    say("so far so good!")


def start():
    say(" Choose a door to begin! (1, 2 or 3)")

    doors = """
____________________
|     DANGER       |
|                  |
|     door 1       |
| O                |    
|                  |
|                  |     
|__________________|

____________________
|      DANGER      |
|                  |
|     door 2       |
|   o              |
|                  |
|                  |     
|__________________|

____________________
|     DANGER       |
|                  |
|     door 3       |
| O                |
|                  |
|                  |     
|__________________|
"""
    print(doors)
    door = input("door: ")

    if door == "1":
        say("Great, door 1 it is!")
        say("There is a lion that is so hungry. he hasent eaten in 1000 years. would you like to turn back or keep going?")
        dire = input("b\\f | ")
        import os


        if dire == ("b"):
            say("ok, choose a door! 2 or 3.")
            door = input("door: ")

        if dire == ("f"):
            
            say("Good choice! the lion hassent eaten in 1000 years. he's dead!... you walk safeley accross.")
            os.system("python main.py")
            import os
            os.system("cd D:\\Maze")
            os.system("python main.py")
            quit()


    if door == "2":
        say("Nothing in here but two doors... but just as you touch the other door nob, you hear the sound of two locks clicking.") 
        playsound("Lockclick.mp3")
        say("your trapped.")
        say("game over")
        quit()



    if door == "3":
        playsound("Jammed.wav")
        say("Door 3 is jammed shut, try again")
        #say("ok, choose a door! 1 or 2.")
        door = input("door: ")

        if door == "2":
            say("Nothing in here but two doors... but just as you touch the other door nob, you hear the sound of two locks clicking.")
            playsound("Lockclick.mp3")
            say("your trapped, you lose the game.")

            quit()

        if door == ("1"):
#<<<<<<< HEAD
            say("Good choice! the lion hassent eaten in 1000 years. he's dead!... you walk safeley accross.")
            import os
            os.system("cd D:\\Maze")
            os.system("python main.py")
            quit()
                
                
#=======
                
                
#>>>>>>> b7351258d08760ce6f6148f5d1ef0f8be7c6ce33
                

        else:
            playsound("Thud.wav")
            say("You ran into a wall, rerun the program")

    else:
        playsound("Thud.wav")
        say("You ran into a wall, rerun the program")



start()

#this is for testing:
#For testing
