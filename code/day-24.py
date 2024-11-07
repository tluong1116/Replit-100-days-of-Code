import random
# Print game introduction
print("Infinity Dice 🎲")
print("")
# Function to roll the dice
def roll_dice(sides):
  return(random.randint(1, sides))
  
# Ask for numbers of sides
sides = int(input("How many side?: "))

# Main loop
while True:
  roll = roll_dice(sides) # Roll the dice
  print(f"You rolled {roll}.\n") # Print the result
  # Repeat loop or not
  again = input("Roll again? (y/n): ")
  if again.lower() == 'n' or again.lower() == 'no':
    break
  else:
    continue
  
