# Gemini 2.5 Pro
import sys

def solve():
    """
    주어진 순열이 반등차(anti-arithmetic) 순열인지 판별합니다.
    """
    try:
        # 첫 줄에서 테스트 케이스의 개수 T를 읽습니다.
        num_test_cases = int(sys.stdin.readline())
    except (ValueError, IndexError):
        return

    # 각 테스트 케이스를 순회합니다.
    for case_num in range(1, num_test_cases + 1):
        try:
            # 순열의 길이 n과 순열 자체를 읽습니다.
            n = int(sys.stdin.readline())
            p = list(map(int, sys.stdin.readline().split()))
            
            # 등차수열을 찾았는지 여부를 기록할 플래그 변수입니다.
            found_series = False
            
            # 모든 가능한 세 인덱스 조합 (i < j < k)을 확인합니다.
            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        # p[i], p[j], p[k]가 등차수열을 이루는지 확인합니다.
                        # 2 * p[j] == p[i] + p[k]
                        if p[j] - p[i] == p[k] - p[j]:
                            found_series = True
                            # 하나라도 찾으면 더 이상 확인할 필요가 없습니다.
                            break
                    if found_series:
                        break
                if found_series:
                    break
            
            # 결과 출력
            if found_series:
                print(f"Case #{case_num}: NO")
            else:
                print(f"Case #{case_num}: YES")

        except (ValueError, IndexError):
            # 테스트 케이스 중간에 입력이 잘못된 경우를 대비합니다.
            continue

# 메인 함수 실행
solve()