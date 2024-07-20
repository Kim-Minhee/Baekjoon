# 입력
N = int(input())
X = list(map(int, input().split()))

# 풀이
X.sort()
r = 0
for i in range(N):
  r += X[i]*((2*i)-2*(N-i-1))

# 출력
print(r)