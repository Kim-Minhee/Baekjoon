# Gemini 3.1 Pro
import sys
input = sys.stdin.readline

# 최솟값과 최댓값을 구하기 위한 초기값 설정
first = 1440
last = 0

for _ in range(int(input().strip())):
    H, M = map(int, input().split(':'))
    time = H * 60 + M
    
    # 혼잡 시간대(390분 ~ 1140분) 안에 들어오는 기록만 처리
    if 390 <= time <= 1140:
        if time < first:
            first = time
        if time > last:
            last = time

# 유효한 기록이 단 하나도 없어서 초기값이 그대로인 경우
if first == 1440:
    print(0)
# 유효한 기록이 있다면 이미 390~1140 사이임이 보장되므로, 
# 10시(600분)와 16시(960분)를 기준으로만 요금을 판별합니다.
elif first <= 600 and last <= 960:
    print(24000)
elif first <= 600 and last >= 961:
    print(36000)
elif first >= 601 and last <= 960:
    print(16800)
elif first >= 601 and last >= 961:
    print(24000)