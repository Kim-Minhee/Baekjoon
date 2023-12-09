n = int(input())
c = s = 100
for _ in range(n):
  c_, s_ = map(int, input().split())
  if c_>s_:
    s -= c_
  elif s_>c_:
    c -= s_
print(c)
print(s)