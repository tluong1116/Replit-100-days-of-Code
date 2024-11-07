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

def character_creation():
  # Choose character name
  name = input("Name your character: ")
  print("")
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
  return({'name':name, 'race':race_dict[race], 'health':health, 'strength':strength})

def battle_roll(player1_dict,player2_dict):
  # Rolling dice
  player1_dict['roll'] = roll_dice(6)
  player2_dict['roll'] = roll_dice(6)
  # Printing out rolls
  print(f"{player1_dict['name']} rolled a {player1_dict['roll'] }.")
  print(f"{player2_dict['name']} rolled a {player2_dict['roll']}.")
  return(player1_dict, player2_dict)

def display_health(player_dict):
  print(f"{player_dict['name']}'s health is {player_dict['health']}")

def round_calculation(player1, player2, battle_round, damage):
  # Decide round winner
  if player1['roll'] > player2['roll']:
    print(f"{player1['name']} wins round {battle_round}!")
    player2['health'] = player2['health'] - damage
  elif player1['roll'] < player2['roll']:
    print(f"{player2['name']} wins round {battle_round}!")
    player1['health'] = player1['health'] - damage
  else:
    print(f"Round {battle_round} was a tie! And they're both standing for the next round!")
  # Display health after round
  display_health(player1)
  display_health(player2)
  return(player1, player2)
  



print("⚔️ BATTLE TIME ⚔️")
print("")

player1 = character_creation()
print("Who are they battling?")
player2 = character_creation()
print(f"{player1['name']}\nHealth: {player1['health']}\nStrength: {player1['strength']}\
\nVS\n\
{player2['name']}\nHealth: {player2['health']}\nStrength: {player2['strength']}")
time.sleep(2)
print("May this battle go down in Legend...")
os.system('clear')

print("⚔️ BATTLE TIME ⚔️")
print("The battle begins!")

battle_round = 1
while True:
  print(f"Round {battle_round}!")
  # battle_roll
  battle_roll(player1,player2)
  # Damage
  damage = abs(player1['strength'] - player2['strength'] +1)
  # Proceed round
  round_calculation(player1, player2, battle_round, damage)
  # Check player health and loop throught the game
  if player1['health'] <= 0 or player2['health'] <= 0:
    if player1['health'] > player2['health']:
      died = player2['name']
      winner = player1['name']
    else:
      died = player1['name']
      winner = player2['name']
    print(f"{died} has died.")
    print(f"The hard battle was fought over {battle_round} rounds.")
    print(f"And the winner was {winner}!")
    exit()
  else:
    battle_round += 1
    print("And the battle continue...")
    time.sleep(3)
    os.system('clear')
    print("⚔️ BATTLE TIME ⚔️")
    continue
  

