import sys
input = sys.stdin.readline

coor = list()
for _ in range(int(input().strip())):
    coor.append(tuple(map(float, input().split())))

for _ in range(int(input().strip())):
    P = int(input().strip())
    I = list(map(int, input().split()))
    from_x, from_y = coor[I[0]]
    dist = 0
    for i in I[1:]:
        to_x, to_y = coor[i]
        dist += ((to_x - from_x) ** 2 + (to_y - from_y) ** 2) ** 0.5
        from_x, from_y = to_x, to_y
    print(int(dist + 0.5))