# GPT 5 수정
from collections import Counter
import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    ch = input().strip()
    ch_cnt = Counter(ch)  # 상자 문자 카운트는 한 번만 계산
    for _ in range(int(input().strip())):
        w_cnt = Counter(input().strip())  # 단어 카운트
        chk = True
        for k, v in w_cnt.items():
            if k not in ch_cnt or v > ch_cnt[k]:
                chk = False
                break
        print('YES' if chk else 'NO')