import sys
input = sys.stdin.readline

L = list(map(int, input().split()))
L.sort()

tri = set()
for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            l1, l2, l3 = L[i], L[j], L[k]
            if l1 + l2 > l3:
                tri.add((l1, l2, l3))
print(len(tri))