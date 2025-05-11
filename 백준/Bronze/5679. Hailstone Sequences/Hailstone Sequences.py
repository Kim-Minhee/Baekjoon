# GPT
while True:
    H = int(input())
    if H == 0:
        break

    max_h = H
    while H != 1:
        if H % 2 == 0:
            H //= 2
        else:
            H = 3 * H + 1
        max_h = max(max_h, H)
    print(max_h)