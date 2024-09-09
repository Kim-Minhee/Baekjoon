# 입력
E, F, C = map(int, input().split())

# 풀이
e = E+F
can = 0
while e>=C:
  n = e//C
  can += n
  e %= C
  e += n

# 출력
print(can)