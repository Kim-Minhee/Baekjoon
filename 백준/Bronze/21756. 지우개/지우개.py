n_list = [i for i in range(1, int(input())+1)]

while len(n_list)>1:
  for i in range(0, len(n_list), 2):
    n_list[i] = 0

  n_tmp = []
  for n in n_list:
    if n!=0: n_tmp.append(n)
  n_list = n_tmp

print(n_list[0])