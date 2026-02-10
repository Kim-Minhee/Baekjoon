import sys
input = sys.stdin.readline

T1, T2 = input().rstrip(), input().rstrip()
S = int(input().strip())
RCD = input().strip()

x, y = 0, 0
win = str()
for idx, rcd in enumerate(RCD):
    if rcd == 'S':
        continue
    if rcd == 'H':
        if idx % 2 == 0:
            x += 1
        else:
            y += 1
    elif rcd == 'D':
        if idx % 2 == 0:
            x += 2
        else:
            y += 2
    else:
        if idx % 2 == 0:
            y += 1
        else:
            x += 1
    
    if x >= 7:
        win = T1
        x = 7
        break
    elif y >= 7:
        win = T2
        y = 7
        break

print(f'{T1} {x} {T2} {y}.', end = ' ')
if win == T1:
    print(f'{T1} has won.')
elif win == T2:
    print(f'{T2} has won.')
elif x > y:
    print(f'{T1} is winning.')
elif x < y:
    print(f'{T2} is winning.')
else:
    print(f'All square.')