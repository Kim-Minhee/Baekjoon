import sys
input = sys.stdin.readline

teams = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']

N = int(input().strip())
max_k, team_idx = -1, -1
for i in range(9):
    temp_k = max(list(map(int, input().split())))
    if temp_k > max_k:
        team_idx = i
        max_k = temp_k
print(teams[team_idx])