# 함수
def cal(num, N):
  sum_base = 0
  while num>0:
    num, mod = divmod(num, N)
    sum_base += int(mod)
  return sum_base

# 풀이
for n in range(1000, 10000):
  n10, n12, n16 = cal(n, 10), cal(n, 12), cal(n, 16)
  if n10==n12==n16:
    print(n)