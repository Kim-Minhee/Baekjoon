r_name = ''
for _ in range(int(input())):
  i_name = input()
  if len(i_name)!=3: pass
  elif r_name=='': r_name = i_name
  elif len(i_name)<len(r_name) and r_name.startswith(i_name): r_name = i_name
  else:
    names = [i_name, r_name]
    if names==sorted(names): r_name = i_name

print(r_name)