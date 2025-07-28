# Gemini 2.5 Pro
import sys

def solve_oldest_tree_candidates():
    """
    가장 늙은 나무의 후보 수를 찾습니다.
    이는 숲에 있는 고유한 나무 종의 수와 같습니다.
    """
    try:
        # 첫 줄에서 나무의 총 수를 읽어옵니다.
        num_trees = int(sys.stdin.readline())
    except (ValueError, IndexError):
        # 입력이 비었거나 숫자가 아닌 경우 등 예외 처리
        return

    # 고유한 나무 종 번호를 저장하기 위해 set을 사용합니다.
    unique_species = set()

    # 각 나무의 정보를 처리합니다.
    for _ in range(num_trees):
        try:
            # 한 줄을 읽어와서 굵기(g)와 종(r)으로 분리합니다.
            # 이 문제에서는 종(r) 정보만 필요합니다.
            g, r = map(int, sys.stdin.readline().split())

            # 종 번호를 set에 추가합니다. 중복된 값은 자동으로 무시됩니다.
            unique_species.add(r)
        except (ValueError, IndexError):
            # 줄이 비었거나 형식이 잘못된 경우 다음 나무로 넘어갑니다.
            continue

    # 후보의 수는 고유한 종의 수와 같으므로, set의 크기를 출력합니다.
    print(len(unique_species))

# 함수 실행
solve_oldest_tree_candidates()