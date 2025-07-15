while True:
  LINE = input()
  if LINE=='#': break

  x, y = 0, 0
  score_a, score_b = 0, 0
  for winner in LINE:
    if winner=='A':
      score_a += 1
    else:
      score_b += 1

    if score_a>=4 and score_a-score_b>=2:
      x += 1
      score_a, score_b = 0, 0
    elif score_b>=4 and score_b-score_a>=2:
      y += 1
      score_a, score_b = 0, 0

  print(f'A {x} B {y}')