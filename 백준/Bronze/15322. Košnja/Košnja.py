# GPT 5
import sys
input = sys.stdin.readline

K = int(input())

for _ in range(K):
    N, M = map(int, input().split())
    print(2 * (min(N, M) - 1))