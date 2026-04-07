# GPT 5
import sys
input = sys.stdin.readline

N = int(input().strip())
ops = [tuple(map(int, input().split())) for _ in range(N)]

answer = 0

# 초기 위치 1, 2, 3 모두 시도
for start in [1, 2, 3]:
    pos = start
    score = 0
    
    for a, b, g in ops:
        # 위치 업데이트 (swap)
        if pos == a:
            pos = b
        elif pos == b:
            pos = a
        
        # 맞췄는지 확인
        if pos == g:
            score += 1
    
    answer = max(answer, score)

print(answer)