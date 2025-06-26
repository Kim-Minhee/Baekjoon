for i in range(int(input())):
  line = list(input().split())
  filterd = []
  for word in line:
    if len(word)==4:
      word = '****'
    filterd.append(word)
  if i!=0:
    print()
  print(' '.join(filterd))