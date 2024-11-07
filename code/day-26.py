from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu : "))
    if stop_playback == 2:
      source.paused = True # let's pause the file 
      return # let's go back from this play() subroutine
    else: 
      continue

while True:
  # clear the screen
  os.system('clear')
  # Show the menu
  print("Menu")
  print("Press 1 to Play")
  print("Press 2 to Exit")
  print("")
  time.sleep(1)
  print("Press anything else to see the menu again")
  # take user's input
  try:
    user_input = int(input())
    # check whether you should call the play() subroutine depending on user's input
    if user_input == 2:
      exit()
    elif user_input == 1:
      play()
    else:
      continue
  except ValueError as e:
    continue
      
