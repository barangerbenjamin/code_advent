groups = open("day_6/input.txt").read().split('\n\n')

total = 0

for group in groups:
  letters = []
  group_l = group.split('\n')
  if '' in group_l:
    group_l.remove('')
  if len(group_l) == 1:
    total += len(set([char for char in group.replace('\n', '')]))
  else:
    join_group = ''.join(group_l)
    print(set(join_group))
    print(join_group)
    for l in set(join_group):
      if join_group.count(l) >= len(group_l):
        total += 1

print(total)
