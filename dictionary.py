geo_logs = [
  {'visit1' : ["������", "������"]},
  {'visit2' : ["����", "�����"]},
  {'visit3' : ["��������", "������"]},
  {'visit4' : ["��������", "����������"]},
  {'visit5' : ["�����", "�������"]},
  {'visit6' : ["��������", "����������"]},
  {'visit7' : ["����", "������"]},
  {'visit8' : ["����", "������"]},
  {'visit9' : ["�����", "������"]},
  {'visit10' : ["�����������", "������"]}
]
geo_logs_rus = []

for visit in geo_logs:
  for val in visit.values():
    if '������' in val:
      geo_logs_rus.append(visit)
      
for visit_rus in geo_logs_rus:
  print(visit_rus)