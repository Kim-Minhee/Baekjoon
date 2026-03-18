# GPT 5
import sys
input = sys.stdin.readline

t, p = map(int, input().split())

# v 계산
if p >= 20:
    v = (100 - p) / t
else:
    v = (120 - 2 * p) / t

# 남은 시간 계산
if p >= 20:
    ans = (p + 20) / v
else:
    ans = (2 * p) / v

print(ans)