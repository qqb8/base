stats = {
  'facebook' : 55,
  'yandex' : 120,
  'vk' : 115,
  'google' : 99,
  'email' : 42,
  'ok' : 98
}

sorted_values = sorted(stats.values())
sorted_stats = {}

for i in sorted_values:
  for k in stats.keys():
    if stats[k] == i:
      sorted_stats[k] = stats[k]
      break
sorted_stats = list(sorted_stats)
print(sorted_stats[-1])