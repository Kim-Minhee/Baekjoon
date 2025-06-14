# GPT 4o
P1, P2, P3, TP = int(input()), int(input()), int(input()), int(input())

max_p1, max_p2, max_p3 = TP // P1, TP // P2, TP // P3
case_cnt = 0
for p1 in range(max_p1 + 1):
  for p2 in range(max_p2 + 1):
    for p3 in range(max_p3 + 1):
      total_points = p1 * P1 + p2 * P2 + p3 * P3
      if p1 + p2 + p3 != 0 and total_points<=TP:
        case_cnt += 1
        print(f'{p1} Brown Trout, {p2} Northern Pike, {p3} Yellow Pickerel')
print(f'Number of ways to catch fish: {case_cnt}')