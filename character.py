"""
Code copied from the class and modified
"""
import random
def character(): #function for character
  ai1 = [{"Amount":100,"Text":"I will die if I give you that much elixr. Be reasonable"},{"Amount":50,"Text":"You want to kill me, Come on!"},{"Amount":25,"Text":"Still going to kill me, but I will allow it"},{"Amount":10,"Text":"It was a good deal"},{"Amount":0,"Text":"Pleasure doing business with you!"},{"Amount":-10,"Text":"That’s really cheap, nice bargain!"},{"Amount":-50,"Text":"Its practically a steal!"}]
  
  cost = random.randint(1,500) #cost of elixer is random number between 1 and 500
  print(f"The amount of elixr needed is {cost}")
  
  print("The witcher would like to give you elixr for some information")
  
  while True:
      choice = int(input("How much do you want to sell the information for? "))
  
      #building some sorting logic to find out when the computer should sell
      if choice > ai1[0]["Amount"] + cost:
          print(ai1[0]["Text"])
      elif choice > ai1[1]["Amount"] + cost:
          print(ai1[1]["Text"])
      elif choice > ai1[4]["Amount"]  + cost or choice > ai1[5]["Amount"] + cost:
          print(ai1[4]["Text"])
          #this is where the trade and story happens with the computer character
          break          
