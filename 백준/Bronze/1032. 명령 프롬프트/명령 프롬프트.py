n, files = int(input()), []

for _ in range(n):
  f = input()
  files.append(f)

name = list(map(str, files[0]))

for i in range(len(name)):
  for j in range(len(files)):
    if (j != len(files)-1) and (name[i] != files[j+1][i]):
      name[i] = '?'
      break

print(''.join(name))