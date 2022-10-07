import urllib.request 
import json
import item
import random
from character import character
import time
import login
from clear_screen import clear
from termcolor import colored, cprint
from replit import audio
import sys
from weather import weather

with open("current_player.json", "r") as game:
    data = json.load(game)

#print(data)

username = data["username"] #username from login file
avatar = data["avatar"] 


print(f"{username.title()} Welcome to the adventure to save the reality of this universe")
print(f"You started at {round((time.time() - data['start_time']) / 60,2)} minutes ago")


source = audio.play_file('audio.mp3') #audio file to play
source.volume -= .50
url= "https://raw.githubusercontent.com/starlordishere/DoctorStrangeGame/main/csvjson.json"
request = urllib.request.urlopen(url) #fetching url
response = json.loads(request.read())

#print(response)
room = 0

while True:
    clear()
    cprint(f"Your location: {response[room]['name']}, your health status is {data['health']} and you have currently {data['items']} items with you.", "green")
    chance = random.randint(1,3) 
    if chance == 1:
      if response[room]["dark_magic"] == 1:
          cprint("You see a witch who perform Dark Magic","yellow")
          character()
    if chance == 2:
      if response[room]["weather"] == 1:
        cprint("Big cloud of acid rain is over you.","yellow")
        cprint("Be alert about the weather","yellow")
        print("The temperature is ")
        weather()
      if chance == 3:
        if response[room]["item"]== 1:
          cprint("Ancient one is here to provide you some advice. Take the advice seriously.","yellow")
          item()
    
    
    cprint(response[room]["story"],"blue")
    
    if response[room]["win"] == 1:
        print("Congratulations, You completeted the task. You won!")
        sys.exit("Thanks for playing!")
    elif response[room]["lose"] == 1:
        print("You failed to complete the task. You lose.")
        sys.exit("Thanks for playing!")
    
    print(response[room]["nav"])
    cprint("America Chavez has opened the portal:","red")

    choice = input(f"Please select one of the portal to go:\n")

    if choice == '1':
        room = response[room]["c1"] - 1
    elif choice == '2':
        room = response[room]["c2"] - 1
    elif choice == '3':
        room = response[room]["c3"] - 1
    else:
        print("You didnot select the right portal, try again")

   