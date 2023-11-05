cnt = 0
while 1:
  try:
    s = input()
    cnt += 1
  except EOFError:
    break
print(cnt)