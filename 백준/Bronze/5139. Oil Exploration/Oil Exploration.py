for k in range(int(input())):
  h, w = map(int, input().split())
  layers = ''.join(input() for _ in range(h))
  layers_trans = ''
  for i in range(w):
    layers_trans += layers[i]
    for j in range(1, h):
      layers_trans += layers[i+w*j]

  costs = []
  for l in range(0, h*w, h):
    layer_trans = layers_trans[l:l+h]
    if 'X' not in layer_trans:
      costs.append('N')
    else:
      cost = 0
      for layer in layer_trans:
        if layer=='H':
          cost += 3
        elif layer=='S':
          cost += 1
        elif layer=='X':
          break
      costs.append(str(cost))

  if k!=0: print()
  print(f'Data Set {k+1}:')
  print(*costs)