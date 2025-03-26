while True:
  KM = input()
  if KM=='0': break

  k, m = map(int, KM.split())
  selected = list(map(int, input().split()))
  check = True
  for _ in range(m):
    C = list(map(int, input().split()))

    num = 0
    for c in C[2:]:
      if c in selected:
        num += 1
    if num<C[1]:
      check = False

  if check:
    print('yes')
  else:
    print('no')