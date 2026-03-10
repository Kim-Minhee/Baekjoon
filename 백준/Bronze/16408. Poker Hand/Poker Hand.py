import sys
input = sys.stdin.readline

rank = 'A23456789TJQK'
cnt = [0] * len(rank)
cards = [card[0] for card in input().split()]
for c in cards:
    cnt[rank.index(c)] += 1
print(max(cnt))