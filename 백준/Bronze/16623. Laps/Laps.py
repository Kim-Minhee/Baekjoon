# GPT 5
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

laps = 0

for i in range(1, m):
    if A[i] < A[i-1]:
        laps += 1

print(laps)