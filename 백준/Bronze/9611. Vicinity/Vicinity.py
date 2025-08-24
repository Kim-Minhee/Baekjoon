N = int(input())
p = [[]]
for _ in range(N):
    p.append(list(map(int, input().split())))

for _ in range(int(input())):
    I, DV = map(int, input().split())
    xi, yi = p[I][0], p[I][1]

    cnt = 0
    for i in range(1, N+1):
        if i != I:
            x, y = p[i][0], p[i][1]
            d = ((xi - x) ** 2 + (yi - y) ** 2) ** 0.5
            if d <= DV:
                cnt += 1
    print(cnt)