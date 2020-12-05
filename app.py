f = open("input.txt", "r")
passwords = [x for x in f]

def is_valid(minimum, maximum, letter, passwd):
  if passwd.count(letter) >= minimum and passwd.count(letter) <= maximum:
    return True

count = 0
for password in passwords:
  letter = password.replace(":", '').split(" ")[1]
  passwd = password.replace(":", '').split(" ")[2]
  minimum = int(password.replace(":", '').split(" ")[0].split('-')[0])
  maximum = int(password.replace(":", '').split(" ")[0].split('-')[1])
  
  if is_valid(minimum, maximum, letter, passwd):
    count += 1

print(count)
