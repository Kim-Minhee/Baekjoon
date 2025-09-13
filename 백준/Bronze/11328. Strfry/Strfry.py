from collections import Counter
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A, B = input().split()
    if Counter(A) == Counter(B):
        print('Possible')
    else:
        print('Impossible')