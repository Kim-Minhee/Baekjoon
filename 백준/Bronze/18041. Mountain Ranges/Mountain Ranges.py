# Gemini 3.1 Pro
import sys

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    x = int(input_data[1])
    altitudes = list(map(int, input_data[2:]))

    if n == 0:
        print(0)
        return

    max_viewpoints = 1  # 전체에서 방문 가능한 최대 전망대 수
    current_count = 1   # 현재 경로에서 방문 중인 전망대 수

    # 두 번째 전망대부터 이전 전망대와 비교하며 순회
    for i in range(1, n):
        # 인접한 두 전망대의 고도 차이 계산
        diff = altitudes[i] - altitudes[i-1]

        if diff <= x:
            # 고도 차이가 X 이하라면 계속 이동 가능
            current_count += 1
        else:
            # X를 초과하면 현재 경로는 여기서 종료, 새로 시작
            current_count = 1

        # 최댓값 갱신
        if current_count > max_viewpoints:
            max_viewpoints = current_count

    print(max_viewpoints)

if __name__ == "__main__":
    solve()