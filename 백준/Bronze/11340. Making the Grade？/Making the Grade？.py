# Gemini 2.5 Pro
import sys
import math

def solve():
    """
    총 평균이 90점 이상이 되기 위해 필요한 최소 기말고사 점수를 계산합니다.
    """
    try:
        # 첫 줄에서 테스트 케이스의 개수를 읽습니다.
        num_test_cases = int(sys.stdin.readline())
    except (ValueError, IndexError):
        # 입력이 없거나 잘못된 형식일 경우 함수를 종료합니다.
        return

    # 각 테스트 케이스를 순회합니다.
    for _ in range(num_test_cases):
        try:
            # 프로젝트, 레포트, 중간고사 점수를 읽습니다.
            project, paper, midterm = map(int, sys.stdin.readline().split())

            # 90점 평균을 위해 필요한 총점을 9000점으로 설정합니다 (모든 가중치에 100을 곱함).
            target_total_score = 9000
            
            # 현재까지 확보한 점수를 계산합니다.
            current_score = (project * 15) + (paper * 20) + (midterm * 25)
            
            # 기말고사에서 받아야 하는 최소 점수를 계산합니다 (가중치 40 적용).
            needed_from_final = target_total_score - current_score

            # 만약 이미 90점을 넘었거나, 기말고사가 0점이어도 90점이 된다면
            # 필요한 최소 점수는 0점입니다.
            if needed_from_final <= 0:
                print(0)
                continue

            # 기말고사 점수로 변환하기 위해 가중치(40)로 나눕니다.
            min_final_score = needed_from_final / 40
            
            # 기말고사 점수는 정수여야 하므로, 소수점이 나오면 올림(ceil) 처리합니다.
            # 예를 들어 89.1점이 필요하면, 90점을 받아야 합니다.
            required_int_score = math.ceil(min_final_score)

            # 계산된 점수가 100점을 초과하면 불가능합니다.
            if required_int_score > 100:
                print("impossible")
            else:
                print(required_int_score)

        except (ValueError, IndexError):
            # 테스트 케이스 중간에 입력이 잘못된 경우를 대비합니다.
            continue

# 메인 함수 실행
solve()