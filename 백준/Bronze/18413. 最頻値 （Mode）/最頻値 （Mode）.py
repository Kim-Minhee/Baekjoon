from collections import Counter
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
counter = Counter(A)
print(max(counter.values()))