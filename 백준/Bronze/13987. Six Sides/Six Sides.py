import sys
input = sys.stdin.readline

P1 = list(map(int, input().split()))
P2 = list(map(int, input().split()))

play = 0
p1_win = 0
for p1 in P1:
    for p2 in P2:
        if p1 == p2:
            continue
        if p1 > p2:
            p1_win += 1
        play += 1
print(f'{p1_win / play:.5f}')