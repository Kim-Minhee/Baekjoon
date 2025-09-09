# GPT 5
# 카드 뒤집기 문제 풀이

cards = list(range(1, 21))  # 처음 카드 상태 [1, 2, ..., 20]

for _ in range(10):
    a, b = map(int, input().split())
    # 파이썬 슬라이싱은 끝 인덱스를 포함하지 않으므로 b 그대로 사용
    cards[a-1:b] = reversed(cards[a-1:b])

print(*cards)