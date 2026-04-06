# GPT 5
import sys
input = sys.stdin.readline

n = int(input())

# 자릿수
length = len(str(n))

# 기준 값 (10^(length-1))
base = 10 ** (length - 1)

# 첫 자리 숫자
d = n // base

# 후보 두 개
low = d * base
high = (d + 1) * base

# 더 가까운 값 선택
if abs(n - low) < abs(high - n):
    print(low)
else:
    print(high)