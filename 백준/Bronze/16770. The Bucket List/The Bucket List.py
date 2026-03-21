# GPT 5
import sys
input = sys.stdin.readline

N = int(input())

events = []

for _ in range(N):
    s, t, b = map(int, input().split())
    events.append((s, b))   # 시작 → +b
    events.append((t, -b))  # 끝 → -b

# 시간순 정렬
events.sort()

cur = 0
ans = 0

for time, val in events:
    cur += val
    ans = max(ans, cur)

print(ans)