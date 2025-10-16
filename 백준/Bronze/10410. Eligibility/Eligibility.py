import sys
input = sys.stdin.readline

for _ in range(int(input())):
    DATA = input().split()
    if int(DATA[1].split('/')[0]) >= 2010 or int(DATA[2].split('/')[0]) >= 1991:
        r = 'eligible'
    elif int(DATA[3]) > 40:
        r = 'ineligible'
    else:
        r = 'coach petitions'
    print(DATA[0], r)