# Gemini 2.5 Pro
import sys

def solve_circular_dna():
    """
    주어진 원형 DNA 서열로부터 사전 순으로 가장 작은 선형 서열을 찾습니다.
    """
    try:
        # 첫 줄에서 테스트 케이스의 수를 읽어옵니다.
        num_test_cases = int(sys.stdin.readline())
    except (ValueError, IndexError):
        return

    # 각 테스트 케이스에 대해 반복합니다.
    for _ in range(num_test_cases):
        # 한 줄을 읽어와서 DNA 서열로 사용합니다.
        sequence = sys.stdin.readline().strip()
        seq_len = len(sequence)

        # 모든 가능한 회전된 서열을 저장할 리스트를 생성합니다.
        # 리스트 컴프리헨션을 사용하여 간결하게 표현합니다.
        all_rotations = [sequence[i:] + sequence[:i] for i in range(seq_len)]

        # 생성된 모든 서열 중에서 사전 순으로 가장 작은 것을 찾아 출력합니다.
        print(min(all_rotations))

# 함수 실행
solve_circular_dna()