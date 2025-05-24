# GPT
X, Y, I = map(int, input().split())

land = [[0]*X for _ in range(Y)]

for _ in range(I):
    X_LD, Y_LD, X_RU, Y_RU = map(int, input().split())
    for y in range(Y_LD - 1, Y_RU):
        for x in range(X_LD - 1, X_RU):
            land[y][x] = 1

print(sum(map(sum, land)))