# 입력
for _ in range(int(input())):
  N = int(input())

  # 풀이
  re = int(str(N)[::-1])
  hap = N+re
  re2 = int(str(hap)[::-1])

  # 출력
  if hap==re2:
    print('YES')
  else:
    print('NO')