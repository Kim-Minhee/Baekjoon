# 함수
def divisor(num):
  divisors = list()
  for i in range(1, int(num**(1/2))+1):
    if num%i==0:
      divisors.append(i)
      if i!=num//i:
        divisors.append(num//i)
  return divisors

# 입력
N = int(input())
L = list(map(int, input().split()))

# 풀이
divisors = []
for l in L:
  divisors += divisor(l)

r = []
for d in set(divisors):
  if d not in r and divisors.count(d)==N:
    r.append(d)
r.sort()

# 출력
for i in r:
  print(i)