# 입력
N = int(input())
B = list(map(int, input().split()))

# 풀이
A = [B[0]]
for i, b in enumerate(B[1:], 1):
  a = b*(i+1)-sum(A[:i])
  A.append(a)

# 출력
print(*A)