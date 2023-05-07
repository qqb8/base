boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
  boys.sort()
  girls.sort()
  # print(boys)
  # print(girls)
  together = zip(boys, girls)
  together = list(together)
  names1, names2, names3, names4, names5 = together
  print('Идеальные пары:', '\n')
  # print(together)
  for pair in together:
    print(pair)
    print(f'{pair[0]} & {pair[1]}')
else:
  print("Кто-то может остаться без пары")

# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# if len(boys) != len(girls):
#     print('Кому-то не достанется пары!')
# pairs = zip(sorted(boys), sorted(girls))
# print('Идеальные пары: ')
# for boy, girl in pairs:
#     print(f'{boy} и {girl}')