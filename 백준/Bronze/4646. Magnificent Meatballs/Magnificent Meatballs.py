while True:
  S = list(map(int, input().split()))
  if S==[0]:
    break

  n, half = S[0], sum(S[1:])//2
  sam, ella = 0, 0
  sam_index, ella_index = -1, -1
  for i in range(1, n):
    sam += S[i]
    if sam==half:
      sam_index = i
      break
    elif sam>half:
      break

  for i in range(n, 0, -1):
    ella += S[i]
    if ella==half:
      ella_index = i
      break
    elif ella>half:
      break

  if ella_index-sam_index==1:
    print(f'Sam stops at position {sam_index} and Ella stops at position {ella_index}.')
  else:
    print('No equal partitioning.')