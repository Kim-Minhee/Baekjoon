# GPT 5
from collections import Counter

s = input().strip()  # 문자열 입력
count = Counter(s)   # 각 문자 개수 세기

# 홀수 개수 문자의 개수를 센다
odd_count = sum(1 for v in count.values() if v % 2 == 1)

# 홀수가 여러 개라면, 그 중 하나만 남기고 나머지를 제거해야 함
# 홀수가 0개나 1개라면 제거할 필요 없음
print(max(0, odd_count - 1))