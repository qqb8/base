queries = [
  "�������� ������� ������",
  "������� ������",
  "����� ����",
  "���� �������",
  "������� ���� �����",
  "���� �� ������",
  "������� ��� �����",
  "���"
]

i = 0

dict1 = dict()
list1 = list()

for string in queries:
  list1.append(len(string.split()))
  dict1.setdefault(len(string.split()))
  i += 1
for k in dict1.keys():
  print(f'���� {k}: {round(list1.count(k) / i * 100)}')