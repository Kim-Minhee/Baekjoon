from collections import Counter
import sys
input = sys.stdin.readline

counter = Counter(input().strip())
cnt = sorted(list(counter.values()), reverse=True)
print(sum(cnt[2:]))