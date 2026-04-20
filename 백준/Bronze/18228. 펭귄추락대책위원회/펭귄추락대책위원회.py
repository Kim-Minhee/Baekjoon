import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
left, right = 0, N - 1
index_p = A.index(-1)
if 1 in A:
    index_1 = A.index(1)
    if index_1 < index_p:
        left = index_1
    else:
        right = index_1
if N in A:
    index_n = A.index(N)
    if index_n < index_p:
        left = index_n
    else:
        right = index_n
r = min(A[left:index_p]) + min(A[index_p + 1:right + 1])
print(r)