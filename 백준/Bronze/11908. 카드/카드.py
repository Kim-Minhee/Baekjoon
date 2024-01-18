n, cards = int(input()), list(map(int, input().split()))
cards.sort()
print(sum(cards[:-1]))