# GPT 5
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

count = [0] * (M + 1)

for x in A:
    count[x] += 1

print(max(count))