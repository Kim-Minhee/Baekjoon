import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = input().strip()
n = N // 4
for _ in range(K % 3):
    a = S[:n]
    b = S[n:3 * n]
    c = S[3 * n:]
    S = a + c + b
print(S)