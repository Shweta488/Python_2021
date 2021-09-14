import pyttsx3
import time

voice = pyttsx3.init()

try:
    voice.say("Press u for going up and d for going down")
    voice.runAndWait()
    direction = input("Press u for going up and d for going down")


    #print("Elevator Door Opens")
    voice.say("Elevator Door Opens")
    voice.runAndWait()


    #print("W e l c o m e  T o  E l e v a t o r")
    voice.say("Welcome  To  Elevator")
    voice.runAndWait()


    #print("Elevator Door Closes")
    voice.say("Elevator Door Closes")
    voice.runAndWait()


    voice.say("Which floor you are at?")
    voice.runAndWait()
    floor = int(input("Which floor you are at?"))


    voice.say("Which floor you want to go at?")
    voice.runAndWait()
    dest = int(input("Which floor you want to go at?"))


except:
    #print("please enter an integer")
    voice.say("please enter an integer")
    voice.runAndWait()


finally:
    max = 10
    total = 0
    if direction == 'u' and dest < 11 and (floor and dest) > 0:
        total = dest - floor
        if total > 0:
            while floor < dest:
                print(floor)
                time.sleep(1)
                floor += 1
            print(f"Reached  at  floor  {dest}")
            voice.say(f"Reached  at  floor  {dest}")
            voice.runAndWait()

            print("Door Opens")
            voice.say("Door Opens")
            voice.runAndWait()

        else:
            #print("Please enter a higher floor number")
            voice.say("Please enter a higher floor number")
            voice.runAndWait()

    elif direction == 'd'and dest < 11 and (floor and dest) > 0:
        total = floor - dest
        if total > 0:
            while floor > dest:
                print(floor)
                time.sleep(1)
                floor -= 1
            print(f"Reached at floor {dest}")
            voice.say(f"Reached at floor {dest}")
            voice.runAndWait()

        else:
            #print("Please enter a lower floor number")
            voice.say("Please enter a lower floor number")
            voice.runAndWait()
    else:
        #print("Not a floor number")
        voice.say("Not a floor number")
        voice.runAndWait()
    voice.stop()
