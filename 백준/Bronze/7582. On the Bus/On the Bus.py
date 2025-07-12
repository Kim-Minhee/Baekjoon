while True:
  INPUTS = input()
  if INPUTS=='# 0': break

  bus, z = INPUTS.split()
  z = int(z)
  P = int(input())
  S = int(input())

  cnt_current = P
  for _ in range(S):
    CNT_OUT, CNT_IN = map(int, input().split())
    cnt_current -= CNT_OUT
    cnt_current += CNT_IN
    cnt_current = min(cnt_current, z)

  print(bus, cnt_current)