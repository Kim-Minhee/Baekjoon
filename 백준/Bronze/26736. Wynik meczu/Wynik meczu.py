s = list(input())
a, b = 0, 0
for s_ in s:
  if s_=='A':
    a += 1
  else:
    b += 1
print(f'{a} : {b}')