# Gemini 2.5 Pro
import sys

def solve_tournament():
    """
    각 테스트 케이스에 대해 토너먼트의 최종 우승자 수를 계산합니다.
    """
    try:
        # 첫 줄에서 테스트 케이스의 수를 읽어옵니다.
        num_test_cases = int(sys.stdin.readline())
    except (ValueError, IndexError):
        return

    # 각 테스트 케이스에 대해 반복합니다.
    for _ in range(num_test_cases):
        try:
            # 참가자 수(n)와 그룹 크기(k)를 읽어옵니다.
            n, k = map(int, sys.stdin.readline().split())
        except (ValueError, IndexError):
            continue

        # k=1인 경우, 아무도 탈락하지 않으므로 모든 참가자가 우승합니다.
        if k == 1:
            print(n)
            continue

        # 참가자 수가 그룹 크기보다 작아질 때까지 시뮬레이션을 반복합니다.
        while n >= k:
            # 현재 n에 대한 몫(q)을 계산합니다. 이것이 한 라운드의 탈락자 수입니다.
            q = n // k
            
            # 몫 q가 변하지 않는 여러 라운드를 한 번에 건너뛰는 최적화 로직입니다.
            # 몫이 바뀌기까지 필요한 라운드 수를 계산합니다.
            rounds_to_jump = (n % k) // q + 1
            
            # 해당 라운드 수만큼의 총 탈락자 수를 한 번에 뺍니다.
            n -= rounds_to_jump * q

        # 최종적으로 남은 참가자 수가 우승자의 수가 됩니다.
        print(n)

# 함수 실행
solve_tournament()