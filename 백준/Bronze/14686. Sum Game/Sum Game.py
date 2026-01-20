import sys
input = sys.stdin.readline

N = int(input().strip())
SW = list(map(int, input().split()))
SM = list(map(int, input().split()))
k = 0
sw_score, sm_score = 0, 0
for i in range(N):
    sw_score += SW[i]
    sm_score += SM[i]
    if sw_score == sm_score:
        k = i + 1
print(k)