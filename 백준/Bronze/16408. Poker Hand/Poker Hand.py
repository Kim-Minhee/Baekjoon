# GPT 5
import sys
input = sys.stdin.readline

cards = input().split()

count = {}

for card in cards:
    r = card[0]
    count[r] = count.get(r, 0) + 1

print(max(count.values()))