import sys
input = sys.stdin.readline

years = []
for i in range(2018, 10001, 13):
    years += [i, i + 2, i + 4, i + 6, i + 8, i + 11]

Y = int(input().strip())
if Y in years:
    print('yes')
else:
    print('no')