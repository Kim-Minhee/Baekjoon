parking = [0]*101

# 입력
A, B, C = map(int, input().split())
for _ in range(3):
  I, O = map(int, input().split())
  for i in range(I, O):
    parking[i] += 1

# 풀이
pay = 0
for p in parking[1:]:
  if p==1:
    pay += A
  elif p==2:
    pay += 2*B
  elif p==3:
    pay += 3*C

# 출력
print(pay)