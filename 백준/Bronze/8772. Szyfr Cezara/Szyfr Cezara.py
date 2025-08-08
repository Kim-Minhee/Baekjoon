alphabet = 'abcdefghijklmnopqrstuvwxyz'

for _ in range(int(input())):
    N = int(input())
    S = input()
    F = input()

    k = alphabet.index(S[0]) - alphabet.index(F)
    if k<0:
        k += 26

    r = []
    for s in S:
        ori = alphabet.index(s)-k
        if ori<0:
            ori += 26
        r.append(alphabet[ori])
    print(''.join(r))