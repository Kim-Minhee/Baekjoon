cnt = 0
for i in range(1, int(input())+1):
  l = list(map(int, list(str(i))))
  if i%sum(l)==0:
    cnt += 1
print(cnt)