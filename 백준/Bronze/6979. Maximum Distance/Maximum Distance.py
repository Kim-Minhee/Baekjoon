# GPT 4o
t = int(input())

for _ in range(t):
    n = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    max_dist = 0
    i, j = 0, 0

    while i < n and j < n:
        if j < i:
            j = i
        elif Y[j] >= X[i]:
            max_dist = max(max_dist, j - i)
            j += 1
        else:
            i += 1

    print(f"The maximum distance is {max_dist}\n")