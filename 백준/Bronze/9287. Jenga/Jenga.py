import sys
input = sys.stdin.readline

for t in range(1, int(input().strip()) + 1):
    r = 'Standing'
    for _ in range(int(input().strip())):
        G = input().strip()
        if '00' in G:
            r = 'Fallen'
    print(f'Case {t}: {r}')