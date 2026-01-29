# GPT 5.1
import sys
input = sys.stdin.readline

# 초기 덱 구성
deck = {
    2: 4,
    3: 4,
    4: 4,
    5: 4,
    6: 4,
    7: 4,
    8: 4,
    9: 4,
    10: 16,  # 10 + J + Q + K
    11: 4    # Ace
}

N = int(input().strip())
sum_cards = 0
remain = deck.copy()

# 이미 뽑은 카드 제거
for _ in range(N):
    v = int(input().strip())
    sum_cards += v
    remain[v] -= 1

# 남은 여유 X
X = 21 - sum_cards

gt = 0  # 값 > X
le = 0  # 값 ≤ X

for value, count in remain.items():
    if value > X:
        gt += count
    else:
        le += count

# 조건 판단
if gt >= le:
    print("DOSTA")   # STOP
else:
    print("VUCI")    # DRAW