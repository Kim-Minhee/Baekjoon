# 함수
def divisor(num):
  r = set()
  if num==1: return 0
  if num<=3: return 1
  for i in range(1, int(num**(1/2)+1)):
    if num%i==0:
      r.add(i)
      r.add(num//i)
  return sum(r)

# 입력
T = int(input())
N = list(map(int, input().split()))

# 풀이
for n in N:
  r = divisor(n)
  r -= n
  
  # 출력
  if r==n: print('Perfect')
  elif r<n: print('Deficient')
  else: print('Abundant')