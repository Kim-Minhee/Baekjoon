N = int(input())
F = list(map(int, input().split()))
C = int(input())
cnt = 0
for f in F:
  cnt += f//C
  if f%C!=0:
    cnt += 1
print(C*cnt)