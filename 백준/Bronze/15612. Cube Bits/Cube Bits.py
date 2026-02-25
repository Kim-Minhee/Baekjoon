import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    V = int(input().strip())
    if V == 0:
        print(0)
        continue
    
    base3 = []
    while V > 0:
        V, m = divmod(V, 3)
        base3.append(str(m))
    print(''.join(base3[::-1]))