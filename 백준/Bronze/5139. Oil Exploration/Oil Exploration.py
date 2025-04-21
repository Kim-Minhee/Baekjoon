# GPT
for k in range(int(input())):
    h, w = map(int, input().split())
    sea_map = [input() for _ in range(h)]

    costs = []
    for col in range(w):
        cost = 0
        found_oil = False

        # 위에서부터 아래로 탐색
        for row in range(h):
            cell = sea_map[row][col]
            if cell == 'X':
                found_oil = True
                break
            elif cell == 'H':
                cost += 3
            elif cell == 'S':
                cost += 1

        # 결과 저장
        if found_oil:
            costs.append(str(cost))
        else:
            costs.append('N')

    # 출력 형식
    if k != 0:
        print()
    print(f'Data Set {k+1}:')
    print(' '.join(costs))