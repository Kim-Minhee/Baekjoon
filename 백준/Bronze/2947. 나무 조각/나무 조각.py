num = list(map(int, input().split()))
while True:
  for i in range(4):
    if num[i]>num[i+1]:
      num[i], num[i+1] = num[i+1], num[i]
      print(*num)
  if num == [1, 2, 3, 4, 5]:
    break