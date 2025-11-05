# Gemini 2.5 Pro
import sys
import math

def solve():
    """
    베를린 장벽을 허무는 데 필요한 시간을 계산합니다.
    """
    try:
        # 첫 줄에서 데이터 세트의 수 K를 읽습니다.
        num_datasets = int(sys.stdin.readline())
    except (ValueError, IndexError):
        return

    # K개의 데이터 세트를 순회합니다.
    for data_set_num in range(1, num_datasets + 1):
        try:
            # n, s, p 값을 읽습니다.
            n, s, p = map(int, sys.stdin.readline().split())

            total_length = 0

            # 첫 번째 기준점을 읽습니다.
            x_prev, y_prev = map(int, sys.stdin.readline().split())

            # n개의 벽 조각에 대해 길이를 계산합니다.
            for _ in range(n):
                # 다음 점을 읽습니다.
                x_curr, y_curr = map(int, sys.stdin.readline().split())

                # 수평 또는 수직 조각의 길이를 계산합니다.
                # (둘 중 하나는 항상 0이 됩니다)
                segment_length = abs(x_curr - x_prev) + abs(y_curr - y_prev)
                total_length += segment_length

                # 현재 점을 다음 계산을 위한 이전 점으로 업데이트합니다.
                x_prev, y_prev = x_curr, y_curr

            # 2. 총 작업 시간을 계산합니다. (총 길이 * 미터당 시간)
            total_person_hours = total_length * s

            # 3. p명으로 나누어 실제 걸리는 시간을 계산합니다.
            required_time = total_person_hours / p

            # 4. 결과를 정수로 올림 처리합니다.
            final_time = math.ceil(required_time)

            # --- 결과 출력 ---
            print(f"Data Set {data_set_num}:")
            print(final_time)

            # 각 데이터 세트 사이에 빈 줄을 출력합니다.
            if data_set_num < num_datasets:
                print()

        except (ValueError, IndexError, EOFError):
            # 데이터 세트 처리 중 오류가 발생하면 다음으로 넘어갑니다.
            continue

# 메인 함수 실행
solve()