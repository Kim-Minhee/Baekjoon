# Gemini 2.5 Pro
import sys

def solve():
    """
    각 마을의 평균 힘과, 평균을 초과하는 사람들의 비율을 계산하는 문제를 해결합니다.
    (부동소수점 오차 방지 및 'round half up' 반올림 규칙 적용)
    """
    try:
        # 첫 줄에서 테스트 케이스의 개수 T를 읽습니다.
        num_test_cases = int(sys.stdin.readline())
    except (ValueError, IndexError):
        # 입력이 없거나 잘못된 형식일 경우 함수를 종료합니다.
        return

    # 각 테스트 케이스를 순회합니다.
    for _ in range(num_test_cases):
        try:
            # 한 줄을 읽고 공백을 기준으로 나눈 뒤, 각 값을 정수로 변환합니다.
            data = list(map(int, sys.stdin.readline().split()))
            
            # 첫 번째 숫자는 사람 수 N, 나머지는 각 사람의 힘(power)입니다.
            n = data[0]
            powers = data[1:]

            # 1. 모든 사람의 힘의 합을 구합니다.
            total_power = sum(powers)
            
            # 2. 평균 힘을 계산합니다.
            average_power = total_power / n

            # 3. 평균 힘보다 더 큰 힘을 가진 사람의 수를 셉니다.
            #    부동소수점 오차를 피하기 위해 정수 연산으로 비교합니다.
            above_average_count = 0
            for power in powers:
                if power * n > total_power:
                    above_average_count += 1
            
            # 4. 백분율을 계산합니다.
            percentage = (above_average_count / n) * 100

            # 5. "round half up" 규칙에 따라 소수점 셋째 자리까지 반올림합니다.
            #    f-string의 기본 반올림은 "round half to even"이므로 수동으로 처리합니다.
            #    값에 0.0005를 더하고 소수점 셋째 자리에서 잘라내는 방식 등을 사용할 수 있으나,
            #    아래 방식이 부동소수점 오차에 더 강건합니다.
            average_power_rounded = int(average_power * 1000 + 0.5) / 1000
            percentage_rounded = int(percentage * 1000 + 0.5) / 1000

            # 6. 예시 출력 형식에 맞춰 평균과 백분율을 함께 출력합니다.
            #    이미 반올림된 값을 .3f로 포맷팅하여 항상 세 자리를 유지하도록 합니다.
            print(f"{average_power_rounded:.3f} {percentage_rounded:.3f}%")

        except (ValueError, IndexError, ZeroDivisionError):
            # 테스트 케이스 중간에 입력이 잘못되거나 N이 0인 경우를 대비합니다.
            continue

# 메인 함수 실행
solve()