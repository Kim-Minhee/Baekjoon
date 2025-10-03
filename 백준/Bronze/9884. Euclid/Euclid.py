import sys
input = sys.stdin.readline

A, B = map(int, input().split())
while A != B:
    a = max(A, B) - min(A, B)
    b = min(A, B)
    A = a
    B = b
print(B)