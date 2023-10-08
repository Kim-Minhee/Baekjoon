s = list()
for i in range(5):
  s.append(sum(list(map(int, input().split()))))
m = max(s)
print(s.index(m)+1, m)