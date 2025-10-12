import sys
input = sys.stdin.readline

for _ in range(int(input())):
    DATA = input().split()
    ox = ''.join(DATA[1:])
    max_x = 0
    for x in ox.split('O'):
        if x != '' and max_x < len(x):
            max_x = len(x)
    print(f"The longest contiguous subsequence of X's is of length {max_x}")