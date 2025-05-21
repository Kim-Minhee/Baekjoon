# Gemini 2.5 Pro
def time_to_minutes(time_str):
    """HH:MM 형식의 시간 문자열을 분으로 변환합니다."""
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

while True:
    N = int(input())
    if N == 0:
        break

    total_accumulated_time = 0  # 누적 총 주행 시간 (분)
    total_accumulated_night_time = 0  # 누적 야간 주행 시간 (분)
    rule_violated_over_2h = False  # 2시간 초과 규칙 위반 여부

    for _ in range(N):
        sunrise_str, sunset_str, start_str, finish_str = input().split()

        sunrise_m = time_to_minutes(sunrise_str)
        sunset_m = time_to_minutes(sunset_str)
        start_m = time_to_minutes(start_str)
        finish_m = time_to_minutes(finish_str)

        current_driving_duration = finish_m - start_m
        total_accumulated_time += current_driving_duration

        if current_driving_duration > 120:
            rule_violated_over_2h = True

        # 현재 주행에서 실제 야간 운전 시간 계산
        actual_night_component_before_sunrise = 0
        if start_m < sunrise_m: # 일출 전에 시작한 경우
            overlap_end = min(finish_m, sunrise_m)
            actual_night_component_before_sunrise = max(0, overlap_end - start_m)

        actual_night_component_after_sunset = 0
        if finish_m > sunset_m: # 일몰 후에 종료한 경우
            overlap_start = max(start_m, sunset_m)
            actual_night_component_after_sunset = max(0, finish_m - overlap_start)
        
        total_actual_night_overlap_for_this_drive = actual_night_component_before_sunrise + actual_night_component_after_sunset

        # 야간 주행 판정: 실제 야간 운전 시간이 주행 시간의 절반 이상인가?
        if total_actual_night_overlap_for_this_drive * 2 >= current_driving_duration:
            total_accumulated_night_time += current_driving_duration
            
    # 최종 판정
    if total_accumulated_time >= 50 * 60 and \
       total_accumulated_night_time >= 10 * 60 and \
       not rule_violated_over_2h:
        print('PASS')
    else:
        print('NON')