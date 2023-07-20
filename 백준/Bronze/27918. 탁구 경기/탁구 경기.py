n, win = int(input()), list()
for _ in range(n):
  w = input()
  win.append(w)

d, p = 0, 0
for w in win:
  if w=='D':
    d += 1
  else:
    p += 1
  if abs(d-p)>=2:
    break
print(f'{d}:{p}')