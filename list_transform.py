list1 = ['2018-01-01', 'yandex', 'cpc', 100]
list1.reverse()
dict1 = list1[0]
for i in list1[1:]:
  dict1 = {i: dict1}
print(dict1)