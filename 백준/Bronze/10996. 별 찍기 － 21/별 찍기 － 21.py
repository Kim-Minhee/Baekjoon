# 입력
N = int(input())

# 풀이
l1 = '* '*(N//2+1)
l2 = ' *'*(N//2+1)

if N%2==1:
  for _ in range(N):
    print(l1[:N])
    print(l2[:N-1])
else:
  for _ in range(N):
    print(l1[:N-1])
    print(l2[:N])