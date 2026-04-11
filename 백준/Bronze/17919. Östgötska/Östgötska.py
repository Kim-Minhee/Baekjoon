import sys
input = sys.stdin.readline

S = list(input().split())
cnt = 0
for s in S:
    if 'ae' in s:
        cnt += 1
if cnt / len(S) >= 0.4:
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')