# Gemini 2.5 Pro
import sys

def solve():
    """
    주어진 숫자 배열의 부분 배열 중 산술 평균이 가장 작은 값을 찾습니다.
    최소 평균은 항상 배열의 최소값과 같습니다.
    """
    try:
        # 첫 줄에서 숫자의 개수 n을 읽어옵니다.
        n = int(sys.stdin.readline())
        # 두 번째 줄에서 숫자 배열 a를 읽어옵니다.
        a = list(map(int, sys.stdin.readline().split()))
    except (ValueError, IndexError):
        return

    # 어떤 부분 배열의 평균도 그 부분 배열의 최소값보다 작을 수 없으므로,
    # 전체 배열의 최소값 하나로만 이루어진 부분 배열이 가장 작은 평균값을 가집니다.
    # 따라서, 배열의 최소값을 찾는 것이 정답입니다.
    if not a: # 입력 배열이 비어있는 경우에 대한 예외 처리
        return

    min_value = min(a)
    
    # 최종적으로 찾은 최소 평균값을 소수점 둘째 자리까지 출력합니다.
    print(f"{float(min_value):.2f}")

# 함수 실행
solve()