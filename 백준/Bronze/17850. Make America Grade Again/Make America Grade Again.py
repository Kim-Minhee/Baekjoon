# GPT 5
import sys
input = sys.stdin.readline

l, h, p, e, n = map(int, input().split())

# 카테고리별 (얻은 점수, 총점)
score = {
    'Lab': [0, 0],
    'Hw': [0, 0],
    'Proj': [0, 0],
    'Exam': [0, 0]
}

for _ in range(n):
    line = input().strip()
    
    # "Lab 1: 15/20" 파싱
    left, right = line.split(':')
    cat = left.split()[0]
    r, s = map(int, right.strip().split('/'))
    
    score[cat][0] += r
    score[cat][1] += s

# 최종 계산
result = 0.0

result += l * (score['Lab'][0] / score['Lab'][1])
result += h * (score['Hw'][0] / score['Hw'][1])
result += p * (score['Proj'][0] / score['Proj'][1])
result += e * (score['Exam'][0] / score['Exam'][1])

# 버림
print(int(result))