import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
gis = [A[0]]
l, r = 0, 1
while r < N:
    left, right = A[l], A[r]
    if left < right:
        gis.append(right)
        l = r
    r += 1
print(len(gis))
print(*gis)