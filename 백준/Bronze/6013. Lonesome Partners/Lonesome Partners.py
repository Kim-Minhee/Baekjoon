# Claude
N = int(input())
cows = []
for _ in range(N):
    cows.append(tuple(map(int, input().split())))

# 첫 번째 쌍으로 초기화
cow1, cow2 = 1, 2
max_dist_sq = (cows[0][0] - cows[1][0])**2 + (cows[0][1] - cows[1][1])**2

# 모든 쌍을 확인
for i in range(N-1):
    for j in range(i+1, N):
        dist_sq = (cows[i][0] - cows[j][0])**2 + (cows[i][1] - cows[j][1])**2
        if dist_sq > max_dist_sq:
            cow1, cow2 = i+1, j+1
            max_dist_sq = dist_sq

print(cow1, cow2)