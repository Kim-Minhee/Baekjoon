import string

# 입력
P, C = input(), input()

# 풀이
a, a_ = dict(), dict()
for i, k in enumerate(list(string.ascii_lowercase)):
  a[k] = i+1
  a_[i+1] = k

c, r = len(C), ''
for i, p in enumerate(P):
  if p==' ':
    r += ' '
  else:
    n = a[p]-a[C[i%c]]
    if n<=0:
      n += 26
    r += a_[n]

# 출력
print(r)