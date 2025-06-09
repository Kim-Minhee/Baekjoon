def decoding(alphabet, s):
  uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  i = (uppers.index(alphabet)-s)%26
  return uppers[i]

K, W = int(input()), input()

r = ''.join(decoding(w, 3*(i+1)+K) for i, w in enumerate(W))
print(r)