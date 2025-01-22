max_cnt = 0
for _ in range(int(input())):
  C = input()
  cnt = C.count('for')
  cnt += C.count('while')
  if cnt>max_cnt:
    max_cnt = cnt

print(max_cnt)