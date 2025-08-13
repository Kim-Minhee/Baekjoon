for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    total_b = 0
    for i, a in enumerate(A):
        total_b += sum(1 for b in A[:i] if b<=a)
    print(total_b)