# GPT 5
import sys
input = sys.stdin.readline

T = int(input().strip())
for tc in range(1, T + 1):
    # 읽을 때 빈 줄이 들어올 수 있으니 처리
    n_line = input().strip()
    while n_line == "":
        n_line = input().strip()
    n = int(n_line)

    perm_line = input().strip()
    while perm_line == "":
        perm_line = input().strip()
    perm = list(map(int, perm_line.split()))

    is_anti = True
    # 모든 i < j < k 쌍 검사
    for i in range(n):
        if not is_anti:
            break
        for j in range(i + 1, n):
            if not is_anti:
                break
            for k in range(j + 1, n):
                if perm[i] + perm[k] == 2 * perm[j]:
                    is_anti = False
                    break

    print(f"Case #{tc}: {'YES' if is_anti else 'NO'}")