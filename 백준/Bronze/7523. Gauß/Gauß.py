# Gemini 2.5 Pro
import sys

def solve_gauss_summation():
    """
    가우스의 등차수열 합 공식을 사용하여 n부터 m까지의 합을 계산합니다.
    """
    try:
        # 첫 줄에서 테스트 케이스의 수를 읽어옵니다.
        num_test_cases = int(sys.stdin.readline())
    except (ValueError, IndexError):
        # 입력이 비었거나 숫자가 아닌 경우 등 예외 처리
        return

    # 각 테스트 케이스를 처리합니다.
    for i in range(1, num_test_cases + 1):
        try:
            # 한 줄을 읽어와서 n과 m으로 분리합니다.
            n, m = map(int, sys.stdin.readline().split())
        except (ValueError, IndexError):
            # 줄이 비었거나 형식이 잘못된 경우 다음 테스트 케이스로 넘어갑니다.
            continue

        # 등차수열의 합 공식을 사용합니다.
        # 합 = (항의 개수) * (첫 항 + 마지막 항) / 2
        # 항의 개수 = m - n + 1
        num_terms = m - n + 1
        sum_first_last = n + m
        
        # 파이썬의 정수 나눗셈(//)을 사용하여 결과를 계산합니다.
        # (num_terms * sum_first_last)는 항상 2로 나누어 떨어집니다.
        total_sum = (num_terms * sum_first_last) // 2

        # 요구된 형식에 맞춰 결과를 출력합니다.
        print(f"Scenario #{i}:")
        print(total_sum)

        # 마지막 테스트 케이스가 아니라면 빈 줄을 추가합니다.
        if i < num_test_cases:
            print()

# 함수 실행
solve_gauss_summation()