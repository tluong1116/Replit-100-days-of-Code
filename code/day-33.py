todo = []
choice_list = [1,2,3,4]

def print_list(list_):
  print()
  for i in list_:
    print(i)
  print()

def print_choice():
  while True:
    choice = int(input("What would you like to do? (1 = add, 2 = remove, 3 = view, 4 = quit) "))
    if choice not in choice_list:
      print("Please enter valid choice")
      continue
    else:
      return choice
      break

def remove_item(item, list_):
  if item in list_:
    list_.remove(item)
    print(f"{item} removed")
  else:
    print(f"{item} is not in list")
    

while True:
  choice = print_choice()
  if choice == 1:
    todo.append(input("What would you like to add? "))
  elif choice == 2:
    if not todo:
      print("The list is empty, there is nothing to remove")
    else:
      item = input("What would you like to remove? ")
      remove_item(item, todo)
  elif choice == 3:
    print_list(todo)
  elif choice == 4:
    break
