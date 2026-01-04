# GPT 5.2
import sys
input = sys.stdin.readline

def count_blue(S, prefix, K):
    """
    무한 반복 문자열에서
    1번부터 K번까지의 'B' 개수
    """
    L = len(S)
    full = K // L
    rest = K % L
    return full * prefix[L] + prefix[rest]

T = int(input())
for t in range(1, T + 1):
    S = input().strip()
    I, J = map(int, input().split())

    # prefix[i] = S의 앞 i글자에서 B 개수
    prefix = [0] * (len(S) + 1)
    for i, ch in enumerate(S):
        prefix[i + 1] = prefix[i] + (1 if ch == 'B' else 0)

    result = count_blue(S, prefix, J) - count_blue(S, prefix, I - 1)
    print(f"Case #{t}: {result}")