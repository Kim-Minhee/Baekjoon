# GPT 5.1
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

seen = set()
count = 0

for x in arr:
    if K - x in seen:
        count += 1
    seen.add(x)

print(count)