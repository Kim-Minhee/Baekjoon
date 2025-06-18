str_idx = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_idx = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]

for _ in range(int(input())):
  P = input().replace('-', '')

  phone = ''
  for p in P[:10]:
    if p.isdigit():
      phone += p
    else:
      idx = str_idx.index(p.upper())
      phone += str(num_idx[idx])

    if len(phone)==3 or len(phone)==7:
      phone += '-'

  print(phone)