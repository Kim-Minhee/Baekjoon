import sys
input = sys.stdin.readline

for n in range(1, int(input().strip()) + 1):
    R, C, W, H = map(int, input().split())
    p = []
    sep = ('+' + '-' * W) * C + '+'
    pat = ('|' + '*' * W) * C + '|'
    
    print(f'Case #{n}:')
    for _ in range(R):
        print(sep)
        for _ in range(H):
            print(pat)
    print(sep)