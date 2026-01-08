import sys
input = sys.stdin.readline

N = int(input().strip())
V = list(map(int, input().split()))
print(sum(V) - max(V))