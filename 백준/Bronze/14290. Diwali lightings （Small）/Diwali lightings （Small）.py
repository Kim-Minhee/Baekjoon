import sys
input = sys.stdin.readline

for t in range(1, int(input().strip()) + 1):
    S = input().strip()
    I, J = map(int, input().split())
    S *= J // len(S) + 1
    cnt_b = S[I - 1: J].count('B')
    print(f'Case #{t}: {cnt_b}')