# GPT 5
import sys
from itertools import combinations

lengths = list(map(int, sys.stdin.readline().split()))

count = 0

for a, b, c in combinations(lengths, 3):
    sides = sorted([a, b, c])
    if sides[0] + sides[1] > sides[2]:
        count += 1

print(count)