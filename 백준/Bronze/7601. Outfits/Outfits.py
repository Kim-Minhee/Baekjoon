import sys

def solve_wardrobe_problem():
    """
    Becs와 Cas가 같은 날 같은 옷을 입는지 확인하는 문제를 해결합니다.
    """
    scenario_num = 1
    while True:
        try:
            # 시나리오의 첫 줄에서 n과 d를 읽어옵니다.
            line = sys.stdin.readline()
            if not line: break
            n, d = map(int, line.split())
        except (ValueError, IndexError):
            break

        # 종료 조건: n과 d가 모두 0이면 루프를 빠져나갑니다.
        if n == 0 and d == 0:
            break

        # --- 옷장 초기화 ---
        # 0부터 n-1까지의 물리적 인덱스로 옷장을 채웁니다.
        becs_wardrobe = list(range(n))
        cas_wardrobe = list(range(n))

        # --- 버린 옷 처리 ---
        # Becs가 버린 옷
        becs_removed = int(sys.stdin.readline())
        if becs_removed != 0:
            # Becs는 왼쪽부터 세므로, r-1 인덱스를 제거합니다.
            becs_wardrobe.pop(becs_removed - 1)

        # Cas가 버린 옷
        cas_removed = int(sys.stdin.readline())
        if cas_removed != 0:
            # Cas는 오른쪽부터 r번째 옷을 버립니다.
            # 이는 물리적으로 n-r 인덱스에 해당하는 옷입니다.
            physical_index_to_remove = n - cas_removed
            cas_wardrobe.remove(physical_index_to_remove)

        # --- 결과 출력 시작 ---
        print(f"Scenario {scenario_num}")
        scenario_num += 1

        # d일 동안의 선택을 확인합니다.
        for day in range(1, d + 1):
            becs_choice, cas_choice = map(int, sys.stdin.readline().split())

            # 각자가 선택한 옷의 '물리적 인덱스'를 찾습니다.
            # Becs: 왼쪽부터 b번째 -> 현재 리스트의 b-1 인덱스
            physical_outfit_becs = becs_wardrobe[becs_choice - 1]

            # Cas: 오른쪽부터 c번째 -> 현재 리스트의 뒤에서 c번째
            cas_current_len = len(cas_wardrobe)
            physical_outfit_cas = cas_wardrobe[cas_current_len - cas_choice]

            # 두 물리적 인덱스를 비교하여 결과를 결정합니다.
            if physical_outfit_becs == physical_outfit_cas:
                result = "ALERT"
            else:
                result = "OK"
            
            print(f"Day {day} {result}")

# 함수 실행
solve_wardrobe_problem()