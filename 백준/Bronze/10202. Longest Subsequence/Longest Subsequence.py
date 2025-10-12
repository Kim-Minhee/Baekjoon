# GPT 5
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    data = input().split()
    ox = ''.join(data[1:])
    max_x = max((len(x) for x in ox.split('O')), default=0)
    print(f"The longest contiguous subsequence of X's is of length {max_x}")