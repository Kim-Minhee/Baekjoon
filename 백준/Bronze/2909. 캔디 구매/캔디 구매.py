# 입력
C, K = map(int, input().split())

# 풀이
r = int(C/10**K+0.5)
r *= 10**K

# 출력
print(r)