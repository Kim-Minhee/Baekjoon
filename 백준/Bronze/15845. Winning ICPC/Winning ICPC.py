import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T = list(map(int, input().split()))
max_score, winner = 0, 1
for team in range(1, N + 1):
    S = list(map(int, input().split()))
    score = 0
    for i, s in enumerate(S):
        if T[i] == s:
            score += 1
    if score > max_score:
        max_score = score
        winner = team
print(winner)