import sys
input = sys.stdin.readline

while True:
    I = input().strip()
    if I == '#':
        break
    
    num = I.split()[1]
    x = []
    for i, n in enumerate(num[:-1]):
        if n == num[i + 1] and n not in x:
            x.append(n)
    if len(x) == 2:
        print(f'{x[0]} {x[0]} glued and {x[1]} {x[1]} glued')
    elif len(x) == 1:
        print(f'{x[0]} {x[0]} glued')