# GPT 5.1
import sys
input = sys.stdin.readline

text = input().strip().upper()

# A~Z 빈도 저장
count = [0] * 26

for ch in text:
    if 'A' <= ch <= 'Z':
        count[ord(ch) - ord('A')] += 1

# 출력
for i in range(26):
    letter = chr(ord('A') + i)
    stars = '*' * count[i]
    print(f"{letter} | {stars}")