# GPT 5
import sys
input = sys.stdin.readline

def to_min(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m

n = int(input())

times = []

for _ in range(n):
    t = to_min(input().strip())
    # CP 시간만 포함 (6:30 ~ 19:00)
    if 390 <= t <= 1140:
        times.append(t)

# CP 내 기록이 없으면 요금 없음
if not times:
    print(0)
    exit()

first = min(times)
last = max(times)

# 기준 시간
t1 = 10 * 60      # 10:00 = 600
t2 = 16 * 60      # 16:00 = 960

# 조건 분기
if first <= t1:
    if last <= t2:
        print(24000)
    else:
        print(36000)
else:
    if last <= t2:
        print(16800)
    else:
        print(24000)