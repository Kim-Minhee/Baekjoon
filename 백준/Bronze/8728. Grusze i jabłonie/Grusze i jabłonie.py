N = int(input())
A = list(map(int, input().split()))

pears, apples = [], []
for i, a in enumerate(A):
    if a==0:
        pears.append(i)
    else:
        apples.append(i)

dist1 = abs(pears[0]-apples[-1])
dist2 = abs(pears[-1]-apples[0])

print(max(dist1, dist2))