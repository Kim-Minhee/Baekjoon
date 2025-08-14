for _ in range(int(input())):
    S = input()
    s = S
    for i in range(1, len(S)):
        s = min(s, S[i:]+S[:i])
    print(s)