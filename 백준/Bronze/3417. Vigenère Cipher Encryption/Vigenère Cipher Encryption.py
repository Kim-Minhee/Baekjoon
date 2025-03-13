# GPT
while True:
    K = input()
    if K=='0': break

    P = input()
    c = ''.join(
        chr((ord(p)-65+ord(K[i%len(K)])-65+1)%26+65) for i, p in enumerate(P)
    )

    print(c)