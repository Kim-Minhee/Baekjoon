import sys
input = sys.stdin.readline

for n in range(1, int(input().strip()) + 1):
    I = input().split()
    print(f'Case #{n}: {" ".join(I[::-1])}')