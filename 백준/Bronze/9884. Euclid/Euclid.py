A, B = map(int, input().split())
while B:
    A, B = B, A % B
print(A)