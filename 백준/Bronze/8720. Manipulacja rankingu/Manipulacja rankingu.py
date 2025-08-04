N, M = map(int, input().split())

dymowka, rank_dymowka, same_dymowka = 0, 1, 1
for i in range(N):
    S = list(map(int, input().split()))

    if i==0:
        weights = [0 if score==0 else 2000 for score in S]

    score = 0
    for j, s in enumerate(S):
        score += weights[j]*s
    
    if i==0:
        dymowka = score
    elif score>dymowka:
        rank_dymowka += 1
    elif score==dymowka:
        same_dymowka += 1

print(rank_dymowka, same_dymowka)