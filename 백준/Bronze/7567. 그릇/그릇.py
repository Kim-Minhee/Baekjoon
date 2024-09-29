# 입력
P = input()

# 풀이
r = 10
for i in range(1, len(P)):
  if P[i]!=P[i-1]:
    r += 10
  else:
    r += 5

# 출력
print(r)