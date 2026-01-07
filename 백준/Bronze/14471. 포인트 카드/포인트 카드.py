# GPT 5.2
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

costs = []
for _ in range(M):
    A, B = map(int, input().split())
    costs.append(max(0, N - A))

total_cost = sum(costs)
max_cost = max(costs)

# M-1장 이상을 살리기 위한 최소 비용
answer = total_cost - max_cost

print(answer)