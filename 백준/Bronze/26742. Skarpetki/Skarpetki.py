b, c = 0, 0
s = list(input())
for s_ in s:
  if s_=='B':
    b += 1
  else:
    c += 1
print(b//2+c//2)