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
  print('��������� ����:', '\n')
  # print(together)
  for pair in together:
    print(pair)
    print(f'{pair[0]} & {pair[1]}')
else:
  print("���-�� ����� �������� ��� ����")

# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# if len(boys) != len(girls):
#     print('����-�� �� ���������� ����!')
# pairs = zip(sorted(boys), sorted(girls))
# print('��������� ����: ')
# for boy, girl in pairs:
#     print(f'{boy} � {girl}')