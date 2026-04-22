# GPT 5
import sys
input = sys.stdin.readline

S = input().strip()

cur = 'A'
ans = 0

for c in S:
    diff = abs(ord(c) - ord(cur))
    ans += min(diff, 26 - diff)
    cur = c

print(ans)