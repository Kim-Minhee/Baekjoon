A = list(input().split())
B = input()

cnt = 0
for a in A:
  if a!=B and a.startswith(B):
    cnt += 1
print(cnt)