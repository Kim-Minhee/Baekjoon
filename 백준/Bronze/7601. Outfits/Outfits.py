# GPT 4o
scenario_num = 1

while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break

    # 옷 목록 만들기
    becs_wardrobe = list(range(1, n + 1))  # 왼쪽부터 오른쪽
    cas_wardrobe = list(range(1, n + 1))   # 오른쪽부터 왼쪽

    # 버린 옷 제거
    becs_removed = int(input())
    cas_removed = int(input())

    if becs_removed != 0:
        becs_wardrobe.pop(becs_removed - 1)
    if cas_removed != 0:
        cas_wardrobe.pop(n - cas_removed)

    print(f"Scenario {scenario_num}")
    for day in range(1, d + 1):
        becs_choice, cas_choice = map(int, input().split())

        # 선택된 옷
        becs_outfit = becs_wardrobe[becs_choice - 1]
        cas_outfit = cas_wardrobe[-cas_choice]  # 오른쪽에서 세기 = 리스트 끝에서부터 세기

        if becs_outfit == cas_outfit:
            print(f"Day {day} ALERT")
        else:
            print(f"Day {day} OK")

    scenario_num += 1