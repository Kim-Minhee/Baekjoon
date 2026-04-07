import sys
input = sys.stdin.readline

I, H, P, E, N = map(int, input().split())
ratio = [I, H, P, E]
got_score = [0, 0, 0, 0]
total_score = [0, 0, 0, 0]
for _ in range(N):
    DATA = input().split(':')
    cat = DATA[0][0]
    got, total = map(int, DATA[1].split('/'))
    if cat == 'L':
        i = 0
    elif cat == 'H':
        i = 1
    elif cat == 'P':
        i = 2
    else:
        i = 3
    got_score[i] += got
    total_score[i] += total

r = 0
for i in range(4):
    r += ratio[i] * (got_score[i] / total_score[i])
print(int(r))