import string

l = list(string.ascii_uppercase)
d = dict()
for i in range(0, 36):
  if i<10:
    d[str(i)] = i
  else:
    d[l[i-10]] = i

# 입력
N, B = map(str, input().split())

# 풀이
b = int(B)
r = 0
for i in range(len(N)):
  r += d[N[-i-1]]*b**i

# 출력
print(r)