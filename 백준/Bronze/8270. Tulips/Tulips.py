# Gemini 2.5 Pro
import sys

def solve_missing_tulips():
    """
    정원에 없는 튤립 품종의 수를 계산하는 문제를 해결합니다.
    """
    TOTAL_TULIP_SPECIES = 15000

    try:
        # 첫 줄에서 화단의 수를 읽어옵니다. (이 값은 실제 계산에는 사용되지 않습니다)
        num_beds = int(sys.stdin.readline())
        
        # 두 번째 줄에서 각 화단의 튤립 품종 번호를 리스트로 읽어옵니다.
        garden_tulips_list = list(map(int, sys.stdin.readline().split()))
    except (ValueError, IndexError):
        # 입력이 비었거나 형식이 잘못된 경우 0을 출력하거나,
        # 문제 조건에 따라 적절히 처리합니다. 여기서는 빈 결과를 가정합니다.
        print(TOTAL_TULIP_SPECIES)
        return

    # 리스트를 set으로 변환하여 정원에 있는 '고유한' 튤립 품종만 남깁니다.
    # set은 중복된 요소를 자동으로 제거해주는 자료구조입니다.
    unique_tulips_in_garden = set(garden_tulips_list)

    # 정원에 있는 고유한 품종의 수를 계산합니다.
    count_of_unique_tulips = len(unique_tulips_in_garden)

    # 전체 품종 수에서 정원에 있는 품종 수를 빼서 부족한 수를 계산합니다.
    missing_species_count = TOTAL_TULIP_SPECIES - count_of_unique_tulips

    # 최종 결과를 출력합니다.
    print(missing_species_count)

# 함수 실행
solve_missing_tulips()