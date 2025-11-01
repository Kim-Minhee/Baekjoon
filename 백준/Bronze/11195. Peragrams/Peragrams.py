from collections import Counter
import sys
input = sys.stdin.readline

counter = Counter(input().strip())
only_one = False
remove = 0
for cnt in counter.values():
    if cnt % 2 != 0:
        if not only_one:
            only_one = True
        else:
            remove += 1
print(remove)