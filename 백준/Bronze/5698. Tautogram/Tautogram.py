# GPT
while True:
    S = input().lower()
    if S == '*':
        break

    words = S.split()
    first = words[0][0]
    print('Y' if all(w[0] == first for w in words) else 'N')