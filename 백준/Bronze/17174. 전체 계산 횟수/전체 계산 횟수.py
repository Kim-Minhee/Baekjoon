n, m = map(int, input().split())
cnt = n
while n:
  n //= m
  cnt += n
print(cnt)