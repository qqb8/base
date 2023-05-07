geo_logs = [
  {'visit1' : ["Москва", "Россия"]},
  {'visit2' : ["Дели", "Индия"]},
  {'visit3' : ["Владимир", "Россия"]},
  {'visit4' : ["Лиссабон", "Португалия"]},
  {'visit5' : ["Париж", "Франция"]},
  {'visit6' : ["Лиссабон", "Португалия"]},
  {'visit7' : ["Тула", "Россия"]},
  {'visit8' : ["Тула", "Россия"]},
  {'visit9' : ["Курск", "Россия"]},
  {'visit10' : ["Архангельск", "Россия"]}
]
geo_logs_rus = []

for visit in geo_logs:
  for val in visit.values():
    if 'Россия' in val:
      geo_logs_rus.append(visit)
      
for visit_rus in geo_logs_rus:
  print(visit_rus)