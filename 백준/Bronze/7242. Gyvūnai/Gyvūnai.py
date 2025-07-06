# Gemini 2.5 Pro
import sys

def time_to_minutes(hours, minutes):
    """시간과 분을 총 분으로 변환하는 함수"""
    return hours * 60 + minutes

def minutes_to_time(total_minutes):
    """총 분을 시간과 분으로 변환하는 함수"""
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return hours, minutes

def solve_hike_timing():
    """
    모든 동물이 활동하는 최적의 시간 구간을 찾는 메인 함수
    """
    try:
        # 첫 줄에서 동물의 수를 읽어옵니다.
        num_animals = int(sys.stdin.readline())
    except (ValueError, IndexError):
        return

    if num_animals <= 0:
        print("NE")
        return

    # 첫 번째 동물의 활동 시간을 기준으로 초기 공통 구간을 설정합니다.
    try:
        h_start, min_start, h_end, min_end = map(int, sys.stdin.readline().split())
        # 공통 구간의 시작은 '가장 늦은 시작 시간'
        latest_start_time = time_to_minutes(h_start, min_start)
        # 공통 구간의 끝은 '가장 이른 종료 시간'
        earliest_end_time = time_to_minutes(h_end, min_end)
    except (ValueError, IndexError):
        # 첫 번째 입력부터 잘못된 경우
        print("NE")
        return

    # 나머지 동물들의 활동 시간을 처리하며 공통 구간을 갱신합니다.
    for _ in range(num_animals - 1):
        try:
            h_start, min_start, h_end, min_end = map(int, sys.stdin.readline().split())
            current_start = time_to_minutes(h_start, min_start)
            current_end = time_to_minutes(h_end, min_end)

            # 시작 시간은 더 늦은 시간으로, 종료 시간은 더 이른 시간으로 갱신합니다.
            latest_start_time = max(latest_start_time, current_start)
            earliest_end_time = min(earliest_end_time, current_end)
        except (ValueError, IndexError):
            # 중간 입력이 잘못된 경우, 공통 구간이 없다고 간주할 수 있음
            print("NE")
            return

    # 최종적으로 유효한 공통 구간이 있는지 확인합니다.
    # 시작 시간이 종료 시간보다 작아야 유효한 구간입니다.
    if latest_start_time < earliest_end_time:
        print("TAIP")
        # 결과를 다시 시, 분 형태로 변환합니다.
        final_h_start, final_min_start = minutes_to_time(latest_start_time)
        final_h_end, final_min_end = minutes_to_time(earliest_end_time)
        print(final_h_start, final_min_start, final_h_end, final_min_end)
    else:
        print("NE")

# 함수 실행
solve_hike_timing()