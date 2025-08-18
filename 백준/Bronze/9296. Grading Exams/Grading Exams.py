for c in range(1, int(input())+1):
    L = int(input())
    K, S = input(), input()
    r = 0
    for i in range(L):
        if K[i]!=S[i]:
            r += 1
    print(f'Case {c}: {r}')