# GPT 5
import sys
input = sys.stdin.readline

fenrir = input().strip()
n = len(fenrir)

# 기본 구조
res = list("AHOW")

# 길이를 Fenrir보다 길게 만들기
while len(res) <= n:
    res.append('O')
    res.append('W')

print(''.join(res))