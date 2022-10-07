"""
Code from the class
"""

import json
import os
import random
import time

path = 'players' #player data in this folder
if not os.path.exists(path):
    os.makedirs(path)


def login(): #login function
    question = input("Do you have an account? y/n ")
    if question.lower() == 'n':
        signup()
    elif question.lower() == "y":
        print("Please enter your account information")
        username = input("Username: ")
        password = input("Password: ")

        try:
            with open(os.path.join(path, username + ".json"), "r") as game:
                info = json.load(game)

            if info["username"] == username and info["password"] == password:
                print("Welcome to your game account", username.title() + "!")

                #saves current file
                with open("current_player.json", "w") as file:
                    json.dump(info, file)
            else:
                print("Incorrect username or password")
                login()

        except FileNotFoundError:
            print("We can not find that account\n Please try again")
            login()        
        
def signup():
    print("Welcome to the game! Sign up for an account!")
    username = input("Please select a username ")
    password = input("Please choose a password ")
    avatar = input("What avatar would you like to play as? ")
    location = input("Where in the world are you? ")

    data = {}
    data["username"] = username
    data["password"] = password
    data["avatar"] = avatar 
    data["progress"] = 0
    data["health"] = 100
    data["items"] = []
    data["credit"]= 0
    data["location"] = location
    data["start_time"] = time.time()
    data["last_login"] = time.time() # we can overwrite this later

    #first check if this name exists, if not, create the acount 
    
    with open(os.path.join(path, username + ".json"), "w") as infile:
        data = json.dump(data, infile)

    login()

login()