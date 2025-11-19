import sys
input = sys.stdin.readline

card_score = {'A':(11, 11),
              'K':(4, 4),
              'Q':(3, 3),
              'J':(20, 2),
              'T':(10, 10),
              '9':(14, 0),
              '8':(0, 0),
              '7':(0, 0)}

N, B = input().split()
total_score = 0
for _ in range(int(N) * 4):
    C = input().strip()
    sign, pattern = C[0], C[1]
    if pattern == B:
        total_score += card_score[sign][0]
    else:
        total_score += card_score[sign][1]
print(total_score)