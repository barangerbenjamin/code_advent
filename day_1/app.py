f = open("input.txt", "r")
numbers = [int(x) for x in f]



for index, num in enumerate(numbers):
  for j in numbers[index + 1:-1]:
    for k in numbers[index + 1:-1]:
      # print(num)
      if num + j + k == 2020:
        print(num * j * k)
