cards = [i for i in range(21)]

for _ in range(10):
    A, B = map(int, input().split())
    reversed = cards[A:B + 1][::-1]
    cards[A:B + 1] = reversed

print(' '.join(str(i) for i in cards[1:]))