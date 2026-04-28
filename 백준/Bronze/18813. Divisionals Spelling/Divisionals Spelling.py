# GPT 5
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

limit = chr(ord('A') + m - 1)

cnt = 0

for _ in range(n):
    w = input().strip()
    
    # 조건 1: 문자 범위
    if any(c > limit for c in w):
        continue
    
    # 조건 2: 중복 없음
    if len(set(w)) != len(w):
        continue
    
    cnt += 1

print(cnt)