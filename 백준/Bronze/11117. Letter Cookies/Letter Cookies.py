from collections import Counter
import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    ch = input()
    for _ in range(int(input().strip())):
        ch_cnt = Counter(ch)
        w_cnt = Counter(input())
        chk = True
        for k, v in w_cnt.items():
            if k not in ch_cnt.keys() or v > ch_cnt[k]:
                chk = False
                break
        print('YES' if chk else 'NO')