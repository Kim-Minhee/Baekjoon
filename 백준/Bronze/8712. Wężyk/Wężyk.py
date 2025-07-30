# GPT 4o
N = int(input())

reverse = False
for n in range(1, N**2 + 1, N):
    row = list(range(n, n + N))
    if reverse:
        row.reverse()
    print(' '.join(map(str, row)))
    reverse = not reverse