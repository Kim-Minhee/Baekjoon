import sys
input = sys.stdin.readline

while True:
    S = input().strip()
    if S == 'ENDOFINPUT':
        break
    M = input().rstrip('\n')
    E = input().strip()
    
    plain = []
    for m in M:
        if 'A' <= m <= 'Z':
            plain.append(chr(((ord(m) - 5) - ord('A')) % 26 + ord('A')))
        else:
            plain.append(m)
    print(''.join(plain))