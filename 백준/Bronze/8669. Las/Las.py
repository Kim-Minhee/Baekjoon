# GPT 4o
import sys
input = sys.stdin.readline

n = int(input())
max_thickness = dict()

for _ in range(n):
    g, r = map(int, input().split())
    if r not in max_thickness or g > max_thickness[r]:
        max_thickness[r] = g

print(len(max_thickness))