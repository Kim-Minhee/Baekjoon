# GPT
N, M = map(int, input().split())

votes = [0] * M

for _ in range(N):
    V = list(map(int, input().split()))
    for i in range(M):
        votes[i] += V[i]

# 정렬: (-투표 수, 장소 번호) 로 정렬
result = sorted(range(1, M+1), key=lambda x: (-votes[x-1], x))

print(*result)