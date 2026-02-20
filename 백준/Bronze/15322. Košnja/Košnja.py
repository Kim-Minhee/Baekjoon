# Gemini 3 Pro
import sys

def solve():
    # 빠른 입출력
    input = sys.stdin.readline

    try:
        # 테스트 케이스 수 K
        k_str = input().strip()
        if not k_str: return
        K = int(k_str)

        # 각 테스트 케이스 처리
        for _ in range(K):
            N, M = map(int, input().split())

            # 핵심 공식: 2 * min(N, M) - 2
            ans = 2 * min(N, M) - 2
            print(ans)

    except ValueError:
        pass

if __name__ == '__main__':
    solve()