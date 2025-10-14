# GPT 5
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    K = int(input())
    counts = []
    while K > 0:
        counts.append(K % 3)
        K //= 3

    # 출력 형식: 맨 높은 차원부터 (마지막부터) 출력
    print(" ".join(map(str, counts[::-1])) if counts else "0")