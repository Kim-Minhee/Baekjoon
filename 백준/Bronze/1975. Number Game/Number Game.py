import sys
input = sys.stdin.readline

# 함수
def f(n):
  r = 0
  for i in range(2, n+1):
    t = n
    while t%i==0:
      r += 1
      t //= i            
  return r

# 풀이
l = [f(i) for i in range(1001)]

for _ in range(int(input())):
  # 입력
  n = int(input())

  # 출력
  print(l[n])