import math

# 입력
R, B = map(int, input().split())

# 풀이
l = math.ceil((R+B)**(1/2))
while 1:
  w = (R+4-2*l)/2
  if l*w==R+B:
    break
  l += 1

# 출력
print(l, int(w))