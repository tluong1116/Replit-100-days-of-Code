import random

# Function to roll the dice
def roll_dice(sides):
  return(random.randint(1, sides))

def health_stat():
  heatlh = roll_dice(6) * roll_dice(8)
  return(heatlh)

# Print game introduction
print("Character Stats Generator")
print("")

# Main loop
while True:
  name = input("Name your warrior: ")
  heatlh = health_stat()
  print(f"Their health is: {heatlh}hp")
  # Repeat loop or not
  play = input("Play again? (y/n): ")
  if play.lower() == 'n' or play.lower() == 'no':
    break
  else:
    continue
