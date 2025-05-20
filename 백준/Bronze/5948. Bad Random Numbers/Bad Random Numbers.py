def random_num(num):
  len_num = len(str(num))
  if len_num==1:
    return 0
  elif len_num==2:
    return int(str(num)[0])**2
  else:
    return int(str(num)[-3:-1])**2

N = int(input())

nums = []
i = 0
while True:
  i += 1
  N = random_num(N)
  if N not in nums:
    nums.append(N)
  else:
    print(i)
    break