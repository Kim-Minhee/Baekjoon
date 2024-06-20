# 입력
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 풀이
seal = list()
for b in B:
  while b>A[0]:
      seal.append(A[0])
      del A[0]
  A[0] -= b

# 출력
print(sum(seal)+sum(A))