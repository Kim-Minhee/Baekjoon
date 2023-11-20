n = int(input())
for _ in range(n):
  t = input()
  if t[(len(t)//2-1)]!=t[(len(t)//2)]:
    print('Do-it-Not')
  else:
    print('Do-it')