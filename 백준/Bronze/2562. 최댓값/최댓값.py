num_d, cnt = dict(), 1
for _ in range(9):
  n = int(input())
  num_d[n] = cnt
  cnt += 1
m = max(list(num_d.keys()))
print(m)
print(num_d[m])