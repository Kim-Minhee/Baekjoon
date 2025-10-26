from math import gcd

M = int(input())
direction = 0  # 0: 시계, 1: 반시계
num, den = 1, 1  # 현재 회전 비율 (num/den)

for _ in range(M):
    a, b, s = map(int, input().split())
    # 비율 업데이트
    num *= b
    den *= a
    # 방향 업데이트 (XOR)
    direction ^= s

# 약분
g = gcd(num, den)
num //= g
den //= g

# 첫 번째 바퀴가 1회전이므로, 마지막 바퀴는 num/den 회전
# 항상 정수라 가정됨
print(direction, num // den)
