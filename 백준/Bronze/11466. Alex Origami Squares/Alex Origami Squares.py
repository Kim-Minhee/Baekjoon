import sys
input = sys.stdin.readline

H, W = map(int, input().split())
l1 = min(H / 3, W)
l2 = min(H, W / 3)
l3 = min(H, W) / 2
print(max(l1, l2, l3))