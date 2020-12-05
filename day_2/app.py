f = open("input.txt", "r")
passwords = [x for x in f]

def is_valid(pos1, pos2, letter, passwd):
  if passwd[pos1] == letter and passwd[pos2] == letter:
    return False
  elif passwd[pos1] == letter:
    return True
  elif passwd[pos2] == letter:
    return True
  

count = 0
for password in passwords:
  letter = password.replace(":", '').split(" ")[1]
  passwd = password.replace(":", '').split(" ")[2]
  pos1 = int(password.replace(":", '').split(" ")[0].split('-')[0])
  pos2 = int(password.replace(":", '').split(" ")[0].split('-')[1])
  
  if is_valid(pos1 - 1, pos2 - 1, letter, passwd):
    count += 1

print(count)
