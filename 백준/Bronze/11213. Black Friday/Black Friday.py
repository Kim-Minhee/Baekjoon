from collections import Counter
import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
counter = Counter(A)
if 1 not in counter.values():
    print('none')
else:
    for i in range(6, 0, -1):
        if counter.get(i, 0) == 1:
            print(A.index(i) + 1)
            break