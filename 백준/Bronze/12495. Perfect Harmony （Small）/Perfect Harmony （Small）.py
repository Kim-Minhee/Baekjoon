# GPT 5.1
import sys
input = sys.stdin.readline

T = int(input().strip())

for t in range(1, T + 1):
    N, L, H = map(int, input().split())
    F = list(map(int, input().split()))

    answer = None

    # Jeff가 선택 가능한 모든 음 X 검사
    for X in range(L, H + 1):
        ok = True
        for f in F:
            # 조화 조건: 한쪽이 다른 쪽의 약수/배수
            if not (f % X == 0 or X % f == 0):
                ok = False
                break
        if ok:
            answer = X
            break

    if answer is None:
        print(f"Case #{t}: NO")
    else:
        print(f"Case #{t}: {answer}")