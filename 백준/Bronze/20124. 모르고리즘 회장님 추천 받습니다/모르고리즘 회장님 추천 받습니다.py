n, v = str(), int()

for i in range(int(input())):
  N, V = input().split()  
  if i==0:
    n = N
    v = int(V)
  else:
    if int(V)>v:
      n = N
      v = int(V)
    elif int(V)==v:
      n_list = [n, N]
      n_list.sort()
      n = n_list[0]

print(n)