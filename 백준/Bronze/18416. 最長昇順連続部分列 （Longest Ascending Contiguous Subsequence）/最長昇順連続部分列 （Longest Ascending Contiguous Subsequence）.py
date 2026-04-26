# Gemini 3.1 Pro
import sys

def solve():
    # 입력을 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    A = list(map(int, input_data[1:]))

    if n == 0:
        print(0)
        return

    max_len = 1
    current_len = 1

    # 두 번째 원소부터 이전 원소와 비교하며 순회합니다.
    for i in range(1, n):
        if A[i] >= A[i-1]:
            # 오름차순(같거나 큼)이 유지되면 길이를 1 증가
            current_len += 1
        else:
            # 숫자가 작아져서 오름차순이 끊기면 길이를 1로 초기화
            current_len = 1

        # 매번 최댓값을 갱신합니다.
        if current_len > max_len:
            max_len = current_len

    print(max_len)

if __name__ == "__main__":
    solve()