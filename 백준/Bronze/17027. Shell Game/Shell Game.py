# GPT 5
import sys
input = sys.stdin.readline

N = int(input())
ops = [tuple(map(int, input().split())) for _ in range(N)]

answer = 0

# 초기 위치 1, 2, 3 모두 시도
for start in range(1, 4):
    pos = start
    score = 0
    
    for a, b, g in ops:
        # swap
        if pos == a:
            pos = b
        elif pos == b:
            pos = a
        
        # guess 체크
        if pos == g:
            score += 1
    
    answer = max(answer, score)

print(answer)