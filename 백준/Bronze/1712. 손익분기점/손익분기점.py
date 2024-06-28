# 입력
A, B, C = map(int, input().split())

# 풀이
if B>=C:
  r = -1
else:
  i = int(A/(C-B))
  if A+B*i<C*i:
    r = i
  else:
    r = i+1

# 출력
print(r)