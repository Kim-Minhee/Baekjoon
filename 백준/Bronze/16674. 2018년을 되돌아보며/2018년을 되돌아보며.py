N = input()

num_2018 = [0]*10
not_num_2018 = [0]*10
for n in N:
  if n in '2018': num_2018[int(n)] += 1
  else: not_num_2018[int(n)] += 1

if sum(not_num_2018)==0: # 관련 있는 수
  if num_2018.count(0)==6: # 밀접한 수
    if len(set(num_2018))==2: # 묶여 있는 수
      print(8)
    else:
      print(2)
  else:
    print(1)
else: # 관련 없는 수
  print(0)