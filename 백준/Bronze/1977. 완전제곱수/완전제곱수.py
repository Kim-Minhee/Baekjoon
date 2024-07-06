import math

# 입력
M, N = int(input()), int(input())

# 풀이
i = math.ceil(M**(1/2))
if i**2>=M and i**2<=N:
  mi, hab = i**2, i**2
  while 1:
    i += 1
    if i**2<=N:
      hab += i**2
    else:
      break

  # 출력
  print(hab)
  print(mi)
else:
  print(-1)