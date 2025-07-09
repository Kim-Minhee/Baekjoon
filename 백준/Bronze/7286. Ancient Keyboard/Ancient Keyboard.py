# Gemini 2.5 Pro
import sys

def solve_ancient_device():
    """
    고대 장치의 출력을 시뮬레이션하는 문제를 해결합니다.
    """
    try:
        # 첫 줄에서 테스트 케이스의 수를 읽어옵니다.
        num_test_cases = int(sys.stdin.readline())
    except (ValueError, IndexError):
        return

    # 각 테스트 케이스에 대해 반복합니다.
    for _ in range(num_test_cases):
        try:
            # 현재 테스트 케이스의 이벤트 수를 읽어옵니다.
            num_events = int(sys.stdin.readline())
        except (ValueError, IndexError):
            continue

        key_events = []
        max_time = 0
        # n개의 이벤트를 읽어 리스트에 저장합니다.
        for _ in range(num_events):
            try:
                key, start_time, end_time = sys.stdin.readline().split()
                start_time, end_time = int(start_time), int(end_time)
                key_events.append((key, start_time, end_time))
                # 시뮬레이션이 필요한 최대 시간을 기록합니다.
                if end_time > max_time:
                    max_time = end_time
            except (ValueError, IndexError):
                continue

        output_chars = []
        # 0초부터 max_time - 1초까지 시뮬레이션을 진행합니다.
        for t in range(max_time):
            active_led_count = 0
            # 현재 시간 t에 활성화된 이벤트가 몇 개인지 셉니다.
            for event in key_events:
                # LED는 start_time부터 end_time - 1까지 켜져 있습니다.
                if event[1] <= t < event[2]:
                    active_led_count += 1
            
            # 켜진 LED가 1개 이상일 경우에만 문자를 추가합니다.
            if active_led_count > 0:
                # 1 -> 'A', 2 -> 'B', ...
                char_to_add = chr(ord('A') + active_led_count - 1)
                output_chars.append(char_to_add)

        # 최종적으로 만들어진 문자열을 출력합니다.
        print("".join(output_chars))

# 함수 실행
solve_ancient_device()