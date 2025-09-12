import sys
input = sys.stdin.readline

alphabet = 'abcdefghijklmnopqrstuvwxyz'

while True:
    D, M, Y = map(int, input().split())
    if D == M == Y == 0:
        break
    I = input().strip()

    s = (D + M + Y) % 25 + 1
    r = []
    for i in I:
        if i not in alphabet:
            r.append(i)
        else:
            r.append(alphabet[alphabet.index(i) - s])
    
    print(''.join(r))