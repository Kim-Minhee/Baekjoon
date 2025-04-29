for _ in range(int(input())):
  K, P = input().split()
  k = [ord(key)-65 for key in K]

  r = ''
  len_k = len(k)
  for i, p in enumerate(P):
    num = ord(p)+k[i%len_k]
    if 90<num:
      num -= 26
    r += chr(num)
  print('Ciphertext:', r)