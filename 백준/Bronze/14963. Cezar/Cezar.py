import sys
input = sys.stdin.readline

cards = {1:0, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:16, 11:4}

sum_cards = 0
for _ in range(int(input().strip())):
    C = int(input().strip())
    sum_cards += C
    cards[C] -= 1

x = 21 - sum_cards
over_x = sum(cards[i] for i in range(min(11, x + 1), 12))
under_x = sum(cards[i] for i in range(1, min(x + 1, 12)))
if over_x >= under_x:
    print('DOSTA')
else:
    print('VUCI')