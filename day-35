import os, time
# Initiate to do list
todo = ["Go Eat", "Go To The Doctor"]
choice_list = [1,2,3,4,5,6]

def print_choice(choice_list):
  while True:
    choice = int(input("What would you like to do? (1 = add, 2 = edit, 3 = remove, 4 = view, 5 = quit, 6 = delete the list) "))
    if choice not in choice_list:
      print("Please enter valid choice")
      continue
    else:
      return choice
      break
      
def print_list(list_):
  print()
  for i in range(len(list_)):
    print(f"{i+1}: {list_[i]}")
  print()


def add_item(list_):
  item = input("What would you like to add? ").title()
  if item in todo:
    print(f"{item} is already in to do list")
  else:
    list_.append(item)

def remove_item(item, list_):
  # If item is in list, confirm if user want to remove it. Only remove if we get back yes
  if item in list_:
    question = input("Are you sure you want to remove this? (y/n) ")
    if question.lower()[0] == "y":
      list_.remove(item)
      print(f"{item} removed")
    else:
      pass
  # If item is not in list
  else:
    print(f"{item} is not in list")

def edit_item(list_):
  print("Here is the list of items in the list:")
  print_list(list_)
  while True:
    idx = int(input("What item number do you want to edit? (Enter 0 for cancel) "))
    if idx == 0:
      break
    elif idx not in range(1, len(list_)+1):
      print("Please enter valid item number")
      continue
    else:
      new_item = input("What would you like to change it to? ").title()
      list_[idx-1] = new_item
      break
  
while True:
  choice = print_choice(choice_list)
  # Add
  if choice == 1:
    add_item(todo)
  # Edit
  if choice == 2:
    edit_item(todo)
  # Remove
  elif choice == 3:
    if not todo:
      print("The list is empty, there is nothing to remove")
    else:
      item = input("What would you like to remove? (Enter c for cancel) ")
      if item == 'c':
        os.system('clear')
        continue
      else:
        remove_item(item, todo)
  # View Item
  elif choice == 4:
    print_list(todo)
  # Quit Program
  elif choice == 5:
    break
  # Delete the list
  elif choice == 6:
    question = input("Are you sure? (y/n) ")
    if question.lower()[0] == "y":
      todo.clear()
      print("List deleted")
    else:
      continue
  time.sleep(1)
  os.system('clear')

