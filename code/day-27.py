import os, time, random

race_dict = {1:'Human', 2:'Elf', 3:'Wizard', 4:'Orc'}
def roll_dice(sides):
  return(random.randint(1,sides))
  
def health_stat():
  health = int(round((roll_dice(6) * roll_dice(12))/2,0) + 10)
  return(health)

def strength_stat():
  strength = int(round((roll_dice(6) * roll_dice(12))/2,0) + 12)
  return(strength)

while True:
  os.system('clear')
  print("Character Builder")
  print("")
  time.sleep(1)

  # Choose character name
  name = input("Name your character: ")
  print("")
  time.sleep(1)
  # Choose character race
  while True:
    try:
      race = int(input("Chose your character race:\n1 - Human\n2 - Elf\n3 - Wizard\n4 - Orc\n..."))
      if race in race_dict:
        break
      else:
        print("Please choose a valid race.")
        continue
    except:
      print("Please choose a valid race.")
      continue
  # Create Health and Strength stat
  health = health_stat()
  strength = strength_stat()
  # Printing out result
  print(name+"\n")
  print(f"Race: {race_dict[race]}")
  print(f"Health :{health}")
  print(f"STRENGTH :{strength}")
  print("")
  time.sleep(1)
  print("May your name go down in Legend...")

  # Loop the game again
  again = input("Would you like to create another character? (y/n) ")
  if again.lower() == 'y':
    continue
  else:
    exit()
  
  
    
