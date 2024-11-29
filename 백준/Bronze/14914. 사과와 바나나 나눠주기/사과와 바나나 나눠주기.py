# 입력
A, B = map(int, input().split())

# 풀이
divisor_A = []
for i in range(1, int(A**(1/2)+1)):
  if A%i==0:
    divisor_A.append(i)
    if A//i not in divisor_A:
      divisor_A.append(A//i)

divisor_AB = []
for a in divisor_A:
  if B%a==0:
    divisor_AB.append(a)

divisor_AB.sort()

# 출력
for d in divisor_AB:
  print(d, A//d, B//d)