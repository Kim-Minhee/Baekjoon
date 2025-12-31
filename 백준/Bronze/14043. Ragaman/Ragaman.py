# GPT 5.2
import sys
from collections import Counter

input = sys.stdin.readline

A = input().strip()
B = input().strip()

cntA = Counter(A)
cntB = Counter(B)

stars = cntB.get('*', 0)

# B에서 '*'가 아닌 문자들을 A에서 "소비"할 수 있어야 한다.
for ch, need in cntB.items():
    if ch == '*':
        continue
    if cntA[ch] < need:
        print('N')
        break
    cntA[ch] -= need
else:
    # 길이가 같으므로 남은 문자의 총합은 stars와 같아야 함
    if sum(cntA.values()) == stars:
        print('A')
    else:
        print('N')