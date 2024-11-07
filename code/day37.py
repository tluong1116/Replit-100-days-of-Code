while True:
  first = input("Please input your first name: ")
  if len(first) < 3 or first.isnumeric():
    print("Please enter valid choice")
    continue
  else:
    break

while True:
  last = input("Please input your last name: ")
  if len(last) < 3 or last.isnumeric():
    print("Please enter valid choice")
    continue
  else:
    break

starwar_firstname = first[0].upper() + first[1:3] + last[0].lower() + last[1:3]

while True:
  mother_maiden = input("Please input your mother's maiden name: ")
  if len(mother_maiden) < 2 or mother_maiden.isnumeric():
    print("Please enter valid choice")
    continue
  else:
    break

while True:
  city = input("Please input your city name: ")
  if len(city) < 3 or city.isnumeric():
    print("Please enter valid choice")
    continue
  else:
    break

starwar_lastname = mother_maiden[0].upper() + mother_maiden[1] + city[-3:].lower()

print("Your star war name is {} {}".format(starwar_firstname, starwar_lastname))
