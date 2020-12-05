f = open("day_3/input.txt", "r")
mapping = [x for x in f]

tree_count = 0
max_row = len(mapping) - 1

# def l(right=3, down=1):
#   tree_count = 0
#   initial = 1
#   i = 0
#   while i <= max_row:
#     for i in range(1, max_row):
#       position = mapping[i][initial + right -1]
#       if position == "#":
#         tree_count += 1
#       initial += right
#       i += down
#   return tree_count


def ok(right=3, down=1):
  r = 0
  c = 0
  t = 0
  while r <= max_row:
    pos = mapping[r][c]
    if pos == "#":
      t += 1
    r += down
    c += right
  return t

for t in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
  print(ok(right=t[0], down=t[1]))
# print(l(7, 1))


