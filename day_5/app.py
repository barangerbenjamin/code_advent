import math

boardings = open("day_5/input.txt").read().split('\n')
boardings.pop()

max_row = 127
max_col = 7


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]
seats = []
for boarding in boardings:
  rows = list(range(0, 128))
  cols = list(range(0, 8))
  row_code = boarding[0:7]
  col_code = boarding[-3:]
  for index, letter in enumerate(row_code):
    front, back = split_list(rows)
    rows = front if letter == 'F' else back
  for index, letter in enumerate(col_code):
    front, back = split_list(cols)
    cols = front if letter == 'L' else back
  seats.append(rows[0] * 8 + cols[0])

print(max(seats))
