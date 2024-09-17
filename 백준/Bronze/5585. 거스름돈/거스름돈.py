# 입력
M = int(input())

# 풀이
coin = [500, 100, 50, 10, 5, 1]
t = 1000-M
r = 0
for c in coin:
  r += t//c
  t %= c

# 출력
print(r)