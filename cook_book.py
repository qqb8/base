person = 5
cook_book = [
  ['�����',
    [
      ['���������', 100, '��.'],
      ['�������', 50, '��.'],
      ['������', 50, '��.'],
      ['�������', 30, '��.'],
      ['�������', 70, '��.'],
    ]
  ],
  ['�����',  
    [
      ['���', 50, '��.'],
      ['������', 50, '��.'],
      ['�����', 100, '��.'],
      ['�����', 30, '��.'],
      ['�������', 30, '��.'],
      ['�����', 20, '��.'],
    ],
  ],
  ['��������� ������',
    [
      ['�����', 60, '��.'],
      ['����', 60, '��.'],
      ['������', 60, '��.'],
      ['�����', 10, '��.'],
      ['���', 50, '��.'],  
    ]
  ]
]

for names, cook in cook_book:
  print(f'{names}:')
  # print(cook)
  for cookie in cook:
    print(cookie[0], end = ' ')
    print(cookie[1] * person, end = ' ')
    print(cookie[2], )
  print()

# person = int(input())

# new_cook_book = []
# for dish, ingredients in cook_book:
#     print(dish)
#     for ingredient in ingredients:
#         ingredient_name = ingredient[0]
#         ingredient_count = ingredient[1] * person
#         ingredient_measure = ingredient[2]
#         print(f'{ingredient_name}, {ingredient_count}{ingredient_measure}')
#     print()