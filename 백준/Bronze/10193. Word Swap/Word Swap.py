import sys
input = sys.stdin.readline

for _ in range(int(input())):
    W1, W2 = input().split()
    coin = 0
    for i in range(len(W1)):
        if W1[i] < W2[i]:
            coin -= ord(W2[i]) - ord(W1[i])
        elif W1[i] > W2[i]:
            coin += ord(W1[i]) - ord(W2[i])

    if coin > 0:
        print(f'Swapping letters to make {W1} look like {W2} earned {coin} coins.')
    elif coin == 0:
        print(f'Swapping letters to make {W1} look like {W2} was FREE.')
    else:
        print(f'Swapping letters to make {W1} look like {W2} cost {-coin} coins.')