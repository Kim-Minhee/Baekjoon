cnt = 0
for i in range(8):
  s = input()
  if i%2==0:
    l = [0, 2, 4, 6]
  else:
    l = [1, 3, 5, 7]
  for j in l:
    if s[j]=='F':
      cnt += 1
print(cnt)