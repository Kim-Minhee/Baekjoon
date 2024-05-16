a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
s = list()
for _ in range(10):
  s.append(['.']*20)
N = int(input())
for i in range(N):
  seat = input()
  r = a.index(seat[0])
  c = int(seat[1:])-1
  s[r][c] = 'o'
for i in range(10):
  p = ''
  for j in range(20):
    p += s[i][j]
  print(p)